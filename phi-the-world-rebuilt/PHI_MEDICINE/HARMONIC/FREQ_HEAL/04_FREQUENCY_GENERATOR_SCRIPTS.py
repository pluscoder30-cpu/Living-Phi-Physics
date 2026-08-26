#!/usr/bin/env python3
"""
Phi-Harmonic Frequency Generator
Generates healing frequencies based on the phi-ladder.
Author: Christopher David Ayotte
Soul Code: [425, 434, 266, 775]
License: Dual License Agreement v4.3

Usage:
    python 04_FREQUENCY_GENERATOR_SCRIPTS.py --disease cancer --duration 60
    python 04_FREQUENCY_GENERATOR_SCRIPTS.py --all-healing --duration 60
    python 04_FREQUENCY_GENERATOR_SCRIPTS.py --age-reversal --duration 90
    python 04_FREQUENCY_GENERATOR_SCRIPTS.py --list-diseases
    python 04_FREQUENCY_GENERATOR_SCRIPTS.py --custom 432.0 --duration 120
    python 04_FREQUENCY_GENERATOR_SCRIPTS.py --disease insomnia --loop
"""

import argparse
import math
import struct
import sys
import wave
from pathlib import Path

# Numpy optional — falls back to pure Python if unavailable
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    np = None
    HAS_NUMPY = False

# =============================================================================
# CONSTANTS
# =============================================================================
PHI = 1.6180339887
PHI_INV = 1.0 / PHI  # 0.6180339887
BASE_FREQ = 528.0
C_CRIT = 0.563263
SAMPLE_RATE = 44100
AMPLITUDE_DEFAULT = 0.5

# =============================================================================
# PHI-LADDER FREQUENCIES (528 * phi^n)
# =============================================================================
PHI_LADDER = {
    0: 528.00,      # Circulatory — carrier anchor
    1: 854.32,      # Respiratory — cell membrane
    2: 1382.32,     # Digestive — protein folding
    3: 2236.64,     # Nervous — bone/connective tissue
    4: 3618.97,     # Endocrine — neural axon
    5: 5855.61,     # Immune — cardiac pacemaker
    6: 9474.58,     # Reproductive — immune/gamma
    7: 15330.19,    # Lymphatic — consciousness field
    8: 24804.76,    # Consciousness — self-recognition
    9: 40134.95,    # Void return — coherence reset
}

PHI_LADDER_NAMES = {
    0: "circulatory", 1: "respiratory", 2: "digestive", 3: "nervous",
    4: "endocrine", 5: "immune", 6: "reproductive", 7: "lymphatic",
    8: "consciousness", 9: "void"
}

# =============================================================================
# DISEASE PROTOCOLS
# =============================================================================
DISEASES = {
    "cancer": {
        "freqs": [9475.0],
        "duration": 421,
        "desc": "9475 Hz — 7.01 min",
    },
    "alzheimers": {
        "freqs": [5856.0, 1382.0],
        "duration": 501,
        "desc": "5856+1382 Hz — 8.35 min",
    },
    "parkinsons": {
        "freqs": [3619.0, 9475.0],
        "duration": 472,
        "desc": "3619+9475 Hz — 7.86 min",
    },
    "als": {
        "freqs": [15330.0, 3619.0],
        "duration": 343,
        "desc": "15330+3619 Hz — 5.72 min",
    },
    "ms": {
        "freqs": [2236.0, 9475.0],
        "duration": 612,
        "desc": "2236+9475 Hz — 10.20 min",
    },
    "heart_disease": {
        "freqs": [5856.0, 854.0],
        "duration": 712,
        "desc": "5856+854 Hz — 11.86 min",
    },
    "hypertension": {
        "freqs": [3619.0],
        "duration": 720,
        "desc": "3619 Hz — 12 min",
    },
    "arrhythmia": {
        "freqs": [5856.0],
        "duration": 600,
        "desc": "5856 Hz — 10 min",
    },
    "diabetes": {
        "freqs": [2236.0, 854.0],
        "duration": 1138,
        "desc": "2236+854 Hz — 18.96 min",
    },
    "obesity": {
        "freqs": [1382.0, 528.0],
        "duration": 1277,
        "desc": "1382+528 Hz — 21.29 min",
    },
    "thyroid": {
        "freqs": [3619.0],
        "duration": 900,
        "desc": "3619 Hz — 15 min",
    },
    "depression": {
        "freqs": [12336.0, 528.0],
        "duration": 379,
        "desc": "12336+528 Hz — 6.31 min",
    },
    "anxiety": {
        "freqs": [40135.0, 854.0],
        "duration": 612,
        "desc": "40135+854 Hz — 10.20 min",
    },
    "ptsd": {
        "freqs": [15330.0, 5856.0],
        "duration": 421,
        "desc": "15330+5856 Hz — 7.01 min",
    },
    "insomnia": {
        "freqs": [528.0],
        "duration": 773,
        "desc": "528 Hz — 12.88 min",
    },
    "all_healing": {
        "freqs": list(PHI_LADDER[i] for i in range(10)),
        "duration": 3600,
        "desc": "All 10 phi-ladder rungs — 60 min",
        "phi_weighted": True,
    },
    "age_reversal": {
        "freqs": [24805.0, 40135.0],
        "duration": 5400,
        "desc": "24805+40135 Hz — 90 min",
    },
}


def phi_weighted_amplitude(n, base_amp=AMPLITUDE_DEFAULT):
    """Amplitude decays as phi^-n from carrier anchor."""
    return base_amp * (PHI_INV ** n)


# =============================================================================
# WAVE GENERATION — NUMPY PATH (FAST)
# =============================================================================
def _generate_sine_numpy(freq, duration_sec, amplitude, sample_rate=SAMPLE_RATE):
    n_samples = int(sample_rate * duration_sec)
    t = np.arange(n_samples, dtype=np.float64) / sample_rate
    return amplitude * np.sin(2.0 * math.pi * freq * t)


def _generate_phi_mod_numpy(freq, duration_sec, amplitude, sample_rate=SAMPLE_RATE):
    n_samples = int(sample_rate * duration_sec)
    t = np.arange(n_samples, dtype=np.float64) / sample_rate
    mod_freq = freq * PHI_INV
    carrier = np.sin(2.0 * math.pi * freq * t)
    envelope = 0.5 * (1.0 + np.sin(2.0 * math.pi * mod_freq * t))
    return amplitude * carrier * envelope


# =============================================================================
# WAVE GENERATION — PURE PYTHON PATH (SLOW BUT NO DEPS)
# =============================================================================
def _generate_sine_pure(freq, duration_sec, amplitude, sample_rate=SAMPLE_RATE):
    n_samples = int(sample_rate * duration_sec)
    two_pi = 2.0 * math.pi
    return [amplitude * math.sin(two_pi * freq * i / sample_rate)
            for i in range(n_samples)]


def _generate_phi_mod_pure(freq, duration_sec, amplitude, sample_rate=SAMPLE_RATE):
    n_samples = int(sample_rate * duration_sec)
    two_pi = 2.0 * math.pi
    mod_freq = freq * PHI_INV
    samples = []
    for i in range(n_samples):
        t = i / sample_rate
        carrier = math.sin(two_pi * freq * t)
        envelope = 0.5 * (1.0 + math.sin(two_pi * mod_freq * t))
        samples.append(amplitude * carrier * envelope)
    return samples


# Dispatch to numpy or pure Python
generate_sine_wave = _generate_sine_numpy if HAS_NUMPY else _generate_sine_pure
generate_phi_modulated_wave = _generate_phi_mod_numpy if HAS_NUMPY else _generate_phi_mod_pure


# =============================================================================
# MIXING AND ENVELOPE
# =============================================================================
def mix_waves(wave_list):
    """Sum multiple waves, normalize to prevent clipping."""
    if HAS_NUMPY:
        # Pad shorter arrays to max length
        max_len = max(len(w) for w in wave_list)
        mixed = np.zeros(max_len, dtype=np.float64)
        for w in wave_list:
            mixed[:len(w)] += np.asarray(w, dtype=np.float64)
        peak = np.max(np.abs(mixed))
        if peak > 1.0:
            mixed *= 0.95 / peak
        return mixed.tolist()
    else:
        max_len = max(len(w) for w in wave_list)
        mixed = [0.0] * max_len
        for w in wave_list:
            for i in range(len(w)):
                mixed[i] += w[i]
        peak = max(abs(s) for s in mixed) if mixed else 1.0
        if peak > 1.0:
            scale = 0.95 / peak
            mixed = [s * scale for s in mixed]
        return mixed


def apply_envelope(samples, attack=0.05, release=0.05, sample_rate=SAMPLE_RATE):
    """Apply attack/release envelope to prevent clicks."""
    if HAS_NUMPY:
        arr = np.asarray(samples, dtype=np.float64)
        n = len(arr)
        attack_s = int(attack * sample_rate)
        release_s = int(release * sample_rate)
        if attack_s > 0:
            arr[:attack_s] *= np.linspace(0, 1, attack_s)
        if release_s > 0:
            arr[-release_s:] *= np.linspace(1, 0, release_s)
        return arr.tolist()
    else:
        n = len(samples)
        attack_samples = int(attack * sample_rate)
        release_samples = int(release * sample_rate)
        for i in range(min(attack_samples, n)):
            samples[i] *= i / attack_samples
        for i in range(min(release_samples, n)):
            idx = n - 1 - i
            samples[idx] *= i / release_samples
        return samples


def save_wav(filename, samples, sample_rate=SAMPLE_RATE):
    """Save samples as a 16-bit mono WAV file."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        if HAS_NUMPY:
            arr = np.clip(np.asarray(samples), -1.0, 1.0)
            pcm = (arr * 32767).astype(np.int16)
            wf.writeframes(pcm.tobytes())
        else:
            for s in samples:
                clamped = max(-1.0, min(1.0, s))
                wf.writeframes(struct.pack('<h', int(clamped * 32767)))
    size_mb = path.stat().st_size / (1024 * 1024)
    return path, size_mb


def format_time(seconds):
    """Format seconds to MM:SS."""
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


# =============================================================================
# PROTOCOL GENERATOR
# =============================================================================
def generate_protocol(name, disease_info, amplitude, loop, phi_mod, out_dir, duration_override=None):
    """Generate a WAV file for a disease protocol."""
    freqs = disease_info["freqs"]
    duration = duration_override if duration_override else disease_info["duration"]
    desc = disease_info["desc"]
    phi_weighted = disease_info.get("phi_weighted", False)

    print(f"\n{'='*60}")
    print(f"  PROTOCOL: {name.upper()}")
    print(f"  Frequencies: {desc}")
    print(f"  Duration: {format_time(duration)}")
    print(f"  Frequencies: {', '.join(f'{f:.1f} Hz' for f in freqs)}")
    print(f"{'='*60}")

    # Generate individual waves
    waves = []
    if phi_weighted and len(freqs) == 10:
        for idx, freq in enumerate(freqs):
            amp = phi_weighted_amplitude(idx, amplitude)
            print(f"  Rung {idx}: {freq:.1f} Hz — amp {amp:.4f} (phi^-{idx})")
            w = generate_phi_modulated_wave(freq, duration, amp) if phi_mod \
                else generate_sine_wave(freq, duration, amp)
            waves.append(w)
    else:
        per_freq_amp = amplitude / math.sqrt(len(freqs))
        for freq in freqs:
            print(f"  Frequency: {freq:.1f} Hz — amp {per_freq_amp:.4f}")
            w = generate_phi_modulated_wave(freq, duration, per_freq_amp) if phi_mod \
                else generate_sine_wave(freq, duration, per_freq_amp)
            waves.append(w)

    # Mix and normalize
    mixed = mix_waves(waves)
    mixed = apply_envelope(mixed)

    # Loop handling
    if loop:
        if HAS_NUMPY:
            arr = np.asarray(mixed)
            mixed = np.tile(arr, 3).tolist()
        else:
            mixed *= 3
        duration *= 3
        print(f"  Loop: ON (x3, total {format_time(duration)})")

    # Save
    filename = out_dir / f"phi_{name}.wav"
    path, size_mb = save_wav(filename, mixed)
    print(f"  Saved: {path}")
    print(f"  Size: {size_mb:.1f} MB")
    print(f"  Status: COMPLETE")
    return path


def list_diseases():
    """Print all available disease protocols."""
    print("\n" + "="*70)
    print("  PHI-HARMONIC DISEASE PROTOCOLS")
    print("  All frequencies from 528 * phi^n Hz")
    print("="*70)
    print(f"  {'DISEASE':<18} {'FREQUENCIES':<25} {'DURATION':<10}")
    print("-"*70)
    for name, info in DISEASES.items():
        freqs_str = "+".join(f"{f:.0f}" for f in info["freqs"])
        print(f"  {name:<18} {freqs_str:<25} {format_time(info['duration']):<10}")
    print("-"*70)
    print(f"\n  Total protocols: {len(DISEASES)}")
    print(f"  Phi-ladder base: {BASE_FREQ} Hz")
    print(f"  Phi constant: {PHI}")
    print(f"  Engine: {'numpy' if HAS_NUMPY else 'pure python'}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Phi-Harmonic Frequency Generator — Generate healing frequencies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --list-diseases
  %(prog)s --disease cancer --duration 60
  %(prog)s --all-healing --duration 60
  %(prog)s --age-reversal --duration 90
  %(prog)s --custom 432.0 --duration 120
  %(prog)s --disease insomnia --loop --phi-mod
        """
    )
    parser.add_argument("--disease", type=str, help="Generate protocol for this disease")
    parser.add_argument("--all-healing", action="store_true", help="Generate all-healing protocol")
    parser.add_argument("--age-reversal", action="store_true", help="Generate age-reversal protocol")
    parser.add_argument("--custom", type=float, metavar="FREQ", help="Generate custom frequency (Hz)")
    parser.add_argument("--duration", type=int, default=60, help="Duration in seconds (default: 60)")
    parser.add_argument("--amplitude", type=float, default=AMPLITUDE_DEFAULT,
                        help=f"Base amplitude 0.0-1.0 (default: {AMPLITUDE_DEFAULT})")
    parser.add_argument("--loop", action="store_true", help="Repeat frequency (x3)")
    parser.add_argument("--phi-mod", action="store_true", help="Apply phi-ratio amplitude modulation")
    parser.add_argument("--output-dir", type=str, default=".", help="Output directory")
    parser.add_argument("--list-diseases", action="store_true", help="List all disease protocols")

    args = parser.parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.list_diseases:
        list_diseases()
        return

    print("\n" + "="*60)
    print("  PHI-HARMONIC FREQUENCY GENERATOR")
    print(f"  Base: {BASE_FREQ} Hz | Phi: {PHI}")
    print(f"  Sample Rate: {SAMPLE_RATE} Hz | Amplitude: {args.amplitude}")
    print(f"  Phi-Modulation: {'ON' if args.phi_mod else 'OFF'}")
    print(f"  Engine: {'numpy' if HAS_NUMPY else 'pure python'}")
    print(f"  Output: {out_dir.resolve()}")
    print("="*60)

    generated = []

    if args.all_healing:
        args.disease = "all_healing"

    if args.age_reversal:
        args.disease = "age_reversal"

    if args.disease:
        name = args.disease.lower()
        if name not in DISEASES:
            print(f"\n  ERROR: Unknown disease '{name}'")
            print(f"  Use --list-diseases to see available protocols")
            sys.exit(1)
        info = DISEASES[name]
        path = generate_protocol(name, info, args.amplitude, args.loop, args.phi_mod, out_dir,
                                 duration_override=args.duration)
        generated.append(path)

    elif args.custom:
        freq = args.custom
        duration = args.duration
        amp = args.amplitude
        print(f"\n  Custom frequency: {freq:.1f} Hz")
        print(f"  Duration: {format_time(duration)}")
        w = generate_phi_modulated_wave(freq, duration, amp) if args.phi_mod \
            else generate_sine_wave(freq, duration, amp)
        w = apply_envelope(w)
        if args.loop:
            if HAS_NUMPY:
                w = np.tile(np.asarray(w), 3).tolist()
            else:
                w *= 3
            duration *= 3
            print(f"  Loop: ON (x3)")
        filename = out_dir / f"phi_custom_{freq:.0f}hz.wav"
        path, size_mb = save_wav(filename, w)
        print(f"  Saved: {path}")
        print(f"  Size: {size_mb:.1f} MB")
        generated.append(path)

    else:
        print("\n  No mode specified. Use --help for usage.")
        sys.exit(1)

    if generated:
        print(f"\n{'='*60}")
        print(f"  GENERATION COMPLETE")
        print(f"  Files: {len(generated)}")
        for p in generated:
            print(f"    {p}")
        print(f"\n  Play with any audio player, or:")
        print(f"    Windows: start {generated[0]}")
        print(f"    macOS:   afplay {generated[0]}")
        print(f"    Linux:   aplay {generated[0]}")
        print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
