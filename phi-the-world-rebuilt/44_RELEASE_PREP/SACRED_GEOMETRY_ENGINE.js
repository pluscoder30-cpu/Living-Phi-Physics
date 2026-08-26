/**
 * SACRED GEOMETRY ENGINE v1.0
 * ============================
 * Self-contained Canvas API sacred geometry visuals.
 * No external dependencies. 4D-reactive (time as 4th dimension).
 *
 * PHI = φ = 1.618033988749895
 * GOLDEN_ANGLE = 137.507764° = 2.39996323 rad
 */

const SacredGeometry = (() => {
    // ─── CONSTANTS ───────────────────────────────────────────────
    const PHI       = 1.618033988749895;
    const PHI_INV   = 0.618033988749895;   // 1/φ
    const GOLDEN_ANGLE = 2.399963228994218; // 137.507764° in radians
    const TAU       = Math.PI * 2;
    const ROOT5     = Math.sqrt(5);
    const EPSILON   = 1e-6;

    // ─── PALETTE ─────────────────────────────────────────────────
    const PALETTE = {
        gold:          '#FFD700',
        goldDim:       'rgba(255,215,0,0.25)',
        goldGlow:      'rgba(255,215,0,0.6)',
        white:         '#FFFFFF',
        whiteDim:      'rgba(255,255,255,0.15)',
        cyan:          '#00E5FF',
        cyanDim:       'rgba(0,229,255,0.2)',
        magenta:       '#FF00E5',
        magentaDim:    'rgba(255,0,229,0.2)',
        violet:        '#8B5CF6',
        violetDim:     'rgba(139,92,246,0.2)',
        void:          '#0A0A12',
        gridLine:      'rgba(255,215,0,0.06)',
        gridAccent:    'rgba(255,215,0,0.12)',
    };

    // ─── HELPERS ─────────────────────────────────────────────────
    function lerp(a, b, t) { return a + (b - a) * t; }
    function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

    /**
     * Easing: phi-smooth — cubic with φ-weighted coefficients.
     */
    function phiEase(t) {
        t = clamp(t, 0, 1);
        return t * t * (3 - 2 * t) * PHI_INV + t * t * t * (1 - PHI_INV);
    }

    /**
     * Pulse function oscillating at golden-angle frequency.
     * @param {number} time   - current time in seconds
     * @param {number} freq   - frequency multiplier
     * @returns {number} value in [0, 1]
     */
    function pulse(time, freq = 1) {
        return 0.5 + 0.5 * Math.sin(time * GOLDEN_ANGLE * freq);
    }

    /**
     * 4D phi-oscillation: time modulated by golden angle.
     */
    function phiOsc(time, freq = 1, phase = 0) {
        return Math.sin(time * GOLDEN_ANGLE * freq + phase);
    }

    /**
     * Hex → rgba with optional alpha override.
     */
    function rgba(hex, alpha) {
        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);
        return `rgba(${r},${g},${b},${alpha})`;
    }

    // ─── CORE: PHI-SPIRAL ───────────────────────────────────────
    /**
     * Draw a logarithmic spiral whose growth factor is φ.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} centerX
     * @param {number} centerY
     * @param {number} maxRadius  - outer bound of the spiral
     * @param {string} color      - stroke color
     * @param {number} [time=0]   - 4D time offset for animation
     * @param {number} [lineWidth=2]
     */
    function drawPhiSpiral(ctx, centerX, centerY, maxRadius, color, time = 0, lineWidth = 2) {
        const growth = Math.log(PHI) / (Math.PI / 2);
        const maxTheta = 10 * Math.PI;

        // 4D modulation: slow breathing of the spiral
        const breathe = 1 + 0.03 * phiOsc(time, 0.5);
        const rotOffset = time * 0.02; // slow rotation

        ctx.save();
        ctx.translate(centerX, centerY);
        ctx.rotate(rotOffset);
        ctx.translate(-centerX, -centerY);

        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.lineWidth = lineWidth;
        ctx.lineCap = 'round';

        for (let theta = 0; theta <= maxTheta; theta += 0.01) {
            const r = maxRadius * Math.exp(-theta * growth) * breathe;
            if (r < 0.5) break;
            const x = centerX + r * Math.cos(theta);
            const y = centerY + r * Math.sin(theta);
            if (theta === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }

        ctx.stroke();

        // Inner glow trail
        ctx.beginPath();
        ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.2);
        ctx.lineWidth = lineWidth * 4;
        ctx.filter = 'blur(4px)';
        for (let theta = 0; theta <= maxTheta; theta += 0.02) {
            const r = maxRadius * Math.exp(-theta * growth) * breathe;
            if (r < 1) break;
            const x = centerX + r * Math.cos(theta);
            const y = centerY + r * Math.sin(theta);
            if (theta === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.stroke();
        ctx.filter = 'none';

        ctx.restore();
    }

    // ─── CORE: GOLDEN ANGLE FLOWER ──────────────────────────────
    /**
     * Vogel-spiral: points placed at golden angle intervals.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} centerX
     * @param {number} centerY
     * @param {number} numPetals   - number of dots
     * @param {number} maxRadius   - spiral arm radius
     * @param {string} color       - dot color
     * @param {number} [time=0]
     * @param {number} [dotRadius=3]
     */
    function drawGoldenFlower(ctx, centerX, centerY, numPetals, maxRadius, color, time = 0, dotRadius = 3) {
        const breathe = 1 + 0.04 * phiOsc(time, 0.7);
        const rotOffset = time * 0.015;

        for (let i = 0; i < numPetals; i++) {
            const angle = i * GOLDEN_ANGLE + rotOffset;
            const r = Math.sqrt(i) * maxRadius * breathe / Math.sqrt(numPetals);

            // Color cycling through hue based on index
            const hueShift = (i / numPetals) * 60; // 60° hue range
            const alpha = lerp(0.4, 1.0, i / numPetals);

            const x = centerX + r * Math.cos(angle);
            const y = centerY + r * Math.sin(angle);

            // Dot with glow
            ctx.beginPath();
            ctx.arc(x, y, dotRadius + phiOsc(time + i * 0.1, 0.3), 0, TAU);
            ctx.fillStyle = rgba(
                typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold,
                alpha
            );
            ctx.fill();

            // Subtle glow ring
            if (i % 5 === 0) {
                ctx.beginPath();
                ctx.arc(x, y, dotRadius * 3, 0, TAU);
                ctx.fillStyle = rgba(
                    typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold,
                    alpha * 0.15
                );
                ctx.fill();
            }
        }
    }

    // ─── CORE: PHI-PULSE ────────────────────────────────────────
    /**
     * Pulsing ring — phi-frequency oscillation for reactive UI elements.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x
     * @param {number} y
     * @param {number} radius
     * @param {number} time
     * @param {string} color
     * @param {number} [rings=3]
     */
    function drawPhiPulse(ctx, x, y, radius, time, color, rings = 3) {
        for (let i = 0; i < rings; i++) {
            const phase = i * PHI_INV * Math.PI;
            const pulseRadius = radius * (1 + 0.12 * Math.sin(time * GOLDEN_ANGLE + phase));
            const alpha = lerp(0.8, 0.15, i / rings);

            ctx.beginPath();
            ctx.arc(x, y, pulseRadius + i * 8, 0, TAU);
            ctx.strokeStyle = rgba(
                typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold,
                alpha
            );
            ctx.lineWidth = 2 - i * 0.4;
            ctx.stroke();
        }
    }

    // ─── CORE: PHI-GRID ─────────────────────────────────────────
    /**
     * φ-proportioned grid — lines at golden-ratio intervals.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} width
     * @param {number} height
     * @param {string} [color]
     * @param {number} [time=0]
     */
    function drawPhiGrid(ctx, width, height, color = PALETTE.gridLine, time = 0) {
        const offset = time * 0.5; // subtle drift

        ctx.save();
        ctx.strokeStyle = color;
        ctx.lineWidth = 0.5;

        // Vertical lines at φ-spaced intervals
        for (let i = -15; i <= 15; i++) {
            const t = i / 15;
            const x = width * 0.5 + width * 0.5 * Math.pow(PHI, t * 3) * Math.sign(t);
            const xShifted = (x + offset) % width;

            ctx.beginPath();
            ctx.moveTo(xShifted, 0);
            ctx.lineTo(xShifted, height);
            ctx.stroke();
        }

        // Horizontal lines at φ-spaced intervals
        for (let i = -15; i <= 15; i++) {
            const t = i / 15;
            const y = height * 0.5 + height * 0.5 * Math.pow(PHI, t * 3) * Math.sign(t);
            const yShifted = (y + offset) % height;

            ctx.beginPath();
            ctx.moveTo(0, yShifted);
            ctx.lineTo(width, yShifted);
            ctx.stroke();
        }

        // Accent lines at key φ-divisions
        ctx.strokeStyle = PALETTE.gridAccent;
        ctx.lineWidth = 1;
        for (const frac of [PHI_INV, 1 / PHI, 1 - PHI_INV, 1 / (PHI * PHI)]) {
            // Vertical
            ctx.beginPath();
            ctx.moveTo(width * frac, 0);
            ctx.lineTo(width * frac, height);
            ctx.stroke();
            // Horizontal
            ctx.beginPath();
            ctx.moveTo(0, height * frac);
            ctx.lineTo(width, height * frac);
            ctx.stroke();
        }

        ctx.restore();
    }

    // ─── PENTAGON (Golden Ratio Pentagon) ───────────────────────
    /**
     * Regular pentagon — edge-to-diagonal ratio is exactly 1:φ.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x         - center x
     * @param {number} y         - center y
     * @param {number} radius    - circumradius
     * @param {string} color
     * @param {number} [time=0]
     * @param {boolean} [fill=false]
     */
    function drawPentagon(ctx, x, y, radius, color, time = 0, fill = false) {
        const rot = time * 0.3; // slow 4D rotation
        const breathe = 1 + 0.02 * phiOsc(time, 0.4);

        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(rot);

        const points = [];
        for (let i = 0; i < 5; i++) {
            const angle = (i * TAU / 5) - Math.PI / 2;
            const r = radius * breathe;
            points.push({ x: r * Math.cos(angle), y: r * Math.sin(angle) });
        }

        // Pentagon edges
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        for (let i = 1; i < 5; i++) ctx.lineTo(points[i].x, points[i].y);
        ctx.closePath();

        if (fill) {
            ctx.fillStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.1);
            ctx.fill();
        }
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.stroke();

        // Star of pentagram inside (φ-ratio diagonals)
        ctx.beginPath();
        ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.5);
        ctx.lineWidth = 1;
        for (let i = 0; i < 5; i++) {
            const next = (i + 2) % 5;
            ctx.moveTo(points[i].x, points[i].y);
            ctx.lineTo(points[next].x, points[next].y);
        }
        ctx.stroke();

        // Inner pentagon (φ-scaled)
        const innerR = radius * PHI_INV * breathe;
        ctx.beginPath();
        for (let i = 0; i < 5; i++) {
            const angle = (i * TAU / 5) - Math.PI / 2 + TAU / 10;
            const px = innerR * Math.cos(angle);
            const py = innerR * Math.sin(angle);
            if (i === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
        }
        ctx.closePath();
        ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.3);
        ctx.lineWidth = 1;
        ctx.stroke();

        // Vertex dots
        for (const p of points) {
            ctx.beginPath();
            ctx.arc(p.x, p.y, 3, 0, TAU);
            ctx.fillStyle = color;
            ctx.fill();
        }

        ctx.restore();
    }

    // ─── FIBONACCI SPIRAL ───────────────────────────────────────
    /**
     * Approximation via quarter-circle arcs sized by Fibonacci numbers.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x        - origin x
     * @param {number} y        - origin y
     * @param {number} maxN     - number of Fibonacci terms
     * @param {string} color
     * @param {number} [time=0]
     * @param {number} [scale=1]
     */
    function drawFibonacciSpiral(ctx, x, y, maxN, color, time = 0, scale = 1) {
        const breathe = 1 + 0.02 * phiOsc(time, 0.6);

        // Generate Fibonacci sequence
        const fib = [1, 1];
        for (let i = 2; i < maxN; i++) fib.push(fib[i - 1] + fib[i - 2]);

        ctx.save();
        ctx.translate(x, y);

        let cx = 0, cy = 0;
        let direction = 0; // 0=right, 1=down, 2=left, 3=up

        for (let i = 0; i < Math.min(maxN, fib.length); i++) {
            const r = fib[i] * scale * breathe;
            const startAngle = (direction * Math.PI) / 2;
            const endAngle = startAngle + Math.PI / 2;

            ctx.beginPath();
            ctx.arc(cx, cy, r, startAngle, endAngle);
            ctx.strokeStyle = rgba(
                typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold,
                lerp(0.3, 1.0, i / maxN)
            );
            ctx.lineWidth = lerp(0.5, 2.5, i / maxN);
            ctx.stroke();

            // Advance center for next square
            switch (direction) {
                case 0: cx += r; break;
                case 1: cy += r; break;
                case 2: cx -= r; break;
                case 3: cy -= r; break;
            }
            direction = (direction + 1) % 4;
        }

        ctx.restore();
    }

    // ─── METATRON'S CUBE ────────────────────────────────────────
    /**
     * Sacred geometry: 13 circles (2 overlapping hexagons) with all
     * center-to-center connections drawn.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x        - center x
     * @param {number} y        - center y
     * @param {number} radius   - outer circle radius
     * @param {string} color
     * @param {number} [time=0]
     */
    function drawMetatronsCube(ctx, x, y, radius, color, time = 0) {
        const breathe = 1 + 0.03 * phiOsc(time, 0.8);
        const rot = time * 0.15;

        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(rot);

        // 13 circle centers: 1 center + 6 inner + 6 outer
        const centers = [{ x: 0, y: 0 }];

        // Inner hexagon (radius r)
        const r = radius * breathe;
        for (let i = 0; i < 6; i++) {
            const angle = (i * TAU) / 6;
            centers.push({ x: r * Math.cos(angle), y: r * Math.sin(angle) });
        }

        // Outer hexagon (radius φr)
        const outerR = r * PHI;
        for (let i = 0; i < 6; i++) {
            const angle = (i * TAU) / 6 + TAU / 12;
            centers.push({ x: outerR * Math.cos(angle), y: outerR * Math.sin(angle) });
        }

        // Draw all connections (Metatron's signature)
        ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.15);
        ctx.lineWidth = 0.8;
        for (let i = 0; i < centers.length; i++) {
            for (let j = i + 1; j < centers.length; j++) {
                ctx.beginPath();
                ctx.moveTo(centers[i].x, centers[i].y);
                ctx.lineTo(centers[j].x, centers[j].y);
                ctx.stroke();
            }
        }

        // Draw circles at each center
        for (let i = 0; i < centers.length; i++) {
            const c = centers[i];
            const circleR = (i === 0 ? r : r * PHI_INV) * 0.8;
            const alpha = lerp(0.3, 0.8, i / centers.length);

            ctx.beginPath();
            ctx.arc(c.x, c.y, circleR, 0, TAU);
            ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, alpha);
            ctx.lineWidth = 1.5;
            ctx.stroke();

            // Subtle fill for center circle
            if (i === 0) {
                ctx.beginPath();
                ctx.arc(c.x, c.y, circleR, 0, TAU);
                ctx.fillStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.08);
                ctx.fill();
            }

            // Vertex dot
            ctx.beginPath();
            ctx.arc(c.x, c.y, 2.5, 0, TAU);
            ctx.fillStyle = color;
            ctx.fill();
        }

        ctx.restore();
    }

    // ─── FLOWER OF LIFE ─────────────────────────────────────────
    /**
     * 19-circle Flower of Life — overlapping circles on a hexagonal lattice.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x        - center x
     * @param {number} y        - center y
     * @param {number} radius   - individual circle radius
     * @param {string} color
     * @param {number} [time=0]
     * @param {number} [layers=3]  - 1=center only, 2=19 circles, 3=37 circles
     */
    function drawFlowerOfLife(ctx, x, y, radius, color, time = 0, layers = 3) {
        const breathe = 1 + 0.02 * phiOsc(time, 0.5);
        const rot = time * 0.08;

        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(rot);

        // Generate hex lattice positions
        const positions = [{ q: 0, r: 0 }]; // center

        if (layers >= 2) {
            // Ring 1: 6 circles
            for (let i = 0; i < 6; i++) {
                const angle = (i * TAU) / 6;
                positions.push({
                    q: Math.round(2 * Math.cos(angle)),
                    r: Math.round(2 * Math.sin(angle))
                });
            }
        }

        if (layers >= 3) {
            // Ring 2: 12 circles
            for (let i = 0; i < 6; i++) {
                const angle1 = (i * TAU) / 6;
                const angle2 = ((i + 1) * TAU) / 6;
                for (let j = 1; j <= 2; j++) {
                    const q = Math.round(2 * Math.cos(angle1) * (j / 2) + 2 * Math.cos(angle2) * ((2 - j) / 2));
                    const rr = Math.round(2 * Math.sin(angle1) * (j / 2) + 2 * Math.sin(angle2) * ((2 - j) / 2));
                    if (!positions.some(p => p.q === q && p.r === rr)) {
                        positions.push({ q, r: rr });
                    }
                }
            }
        }

        // Draw circles
        for (let i = 0; i < positions.length; i++) {
            const p = positions[i];
            const cx = p.q * radius * breathe * 0.5;
            const cy = p.r * radius * breathe * 0.5;
            const dist = Math.sqrt(p.q * p.q + p.r * p.r);
            const alpha = lerp(0.6, 0.15, dist / 4);

            ctx.beginPath();
            ctx.arc(cx, cy, radius * breathe * 0.5, 0, TAU);
            ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, alpha);
            ctx.lineWidth = lerp(1.5, 0.5, dist / 4);
            ctx.stroke();
        }

        // Vesica Piscis highlight in center (overlap of two adjacent circles)
        if (layers >= 2) {
            const vesicaR = radius * breathe * 0.5;
            const vesicaX = vesicaR * 0.5;

            ctx.beginPath();
            ctx.arc(-vesicaX, 0, vesicaR, 0, TAU);
            ctx.arc(vesicaX, 0, vesicaR, 0, TAU);
            ctx.fillStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.04);
            ctx.fill();
        }

        ctx.restore();
    }

    // ─── SACRED GRID (Phi-proportioned background) ──────────────
    /**
     * Full-canvas phi-proportioned grid with golden-ratio divisions
     * and optional animation.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} width
     * @param {number} height
     * @param {number} [time=0]
     */
    function drawSacredGrid(ctx, width, height, time = 0) {
        // Base grid
        drawPhiGrid(ctx, width, height, PALETTE.gridLine, time);

        const breathe = 1 + 0.015 * phiOsc(time, 0.3);

        // Golden spiral overlay (faint)
        ctx.save();
        ctx.globalAlpha = 0.08;
        drawPhiSpiral(ctx, width * PHI_INV, height * PHI_INV, Math.min(width, height) * 0.8, PALETTE.gold, time, 1);
        ctx.restore();

        // Rule-of-thirds / φ-divisions — prominent guides
        ctx.save();
        ctx.strokeStyle = PALETTE.gridAccent;
        ctx.lineWidth = 1;
        ctx.setLineDash([8, 8]);

        const divisions = [1 / PHI, 1 - 1 / PHI];
        for (const d of divisions) {
            // Vertical
            ctx.beginPath();
            ctx.moveTo(width * d, 0);
            ctx.lineTo(width * d, height);
            ctx.stroke();
            // Horizontal
            ctx.beginPath();
            ctx.moveTo(0, height * d);
            ctx.lineTo(width, height * d);
            ctx.stroke();
        }

        ctx.setLineDash([]);
        ctx.restore();

        // Corner φ-markers
        const markerR = Math.min(width, height) * 0.02;
        const corners = [
            { x: width * PHI_INV, y: height * PHI_INV },
            { x: width * (1 - PHI_INV), y: height * PHI_INV },
            { x: width * PHI_INV, y: height * (1 - PHI_INV) },
            { x: width * (1 - PHI_INV), y: height * (1 - PHI_INV) },
        ];
        for (const c of corners) {
            drawPhiPulse(ctx, c.x, c.y, markerR, time, PALETTE.gold, 2);
        }
    }

    // ─── PHI-NODE ANIMATOR (for DOM elements) ───────────────────
    /**
     * Animate a DOM element as a phi-node: scale + golden glow.
     * @param {HTMLElement} element
     * @param {number} time
     * @param {Object} [opts]
     * @param {number} [opts.scaleAmount=0.05]
     * @param {number} [opts.glowMin=5]
     * @param {number} [opts.glowMax=15]
     * @param {string} [opts.glowColor='rgba(255,215,0,0.5)']
     */
    function animatePhiNode(element, time, opts = {}) {
        const {
            scaleAmount = 0.05,
            glowMin = 5,
            glowMax = 15,
            glowColor = 'rgba(255,215,0,0.5)',
        } = opts;

        const scale = 1 + scaleAmount * phiOsc(time, 1);
        const glow = lerp(glowMin, glowMax, pulse(time, 1));

        element.style.transform = `scale(${scale})`;
        element.style.boxShadow = `0 0 ${glow}px ${glowColor}`;
    }

    // ─── ADVANCED: DOUBLE HELIX (DNA / 4D) ──────────────────────
    /**
     * Two intertwined phi-spirals forming a double helix.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x
     * @param {number} y
     * @param {number} length
     * @param {number} amplitude
     * @param {string} color1
     * @param {string} color2
     * @param {number} [time=0]
     */
    function drawDoubleHelix(ctx, x, y, length, amplitude, color1, color2, time = 0) {
        const steps = 200;
        const rot = time * 0.2;

        // Strand 1
        ctx.beginPath();
        ctx.strokeStyle = color1;
        ctx.lineWidth = 2;
        for (let i = 0; i <= steps; i++) {
            const t = i / steps;
            const px = x + amplitude * Math.cos(t * TAU * 3 + rot);
            const py = y - length / 2 + t * length;
            if (i === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Strand 2 (offset by π)
        ctx.beginPath();
        ctx.strokeStyle = color2;
        ctx.lineWidth = 2;
        for (let i = 0; i <= steps; i++) {
            const t = i / steps;
            const px = x + amplitude * Math.cos(t * TAU * 3 + rot + Math.PI);
            const py = y - length / 2 + t * length;
            if (i === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
        }
        ctx.stroke();

        // Cross-links at φ-intervals
        ctx.strokeStyle = PALETTE.whiteDim;
        ctx.lineWidth = 0.8;
        const linkCount = Math.floor(length / (amplitude * PHI));
        for (let i = 0; i < linkCount; i++) {
            const t = (i + 0.5) / linkCount;
            const px1 = x + amplitude * Math.cos(t * TAU * 3 + rot);
            const px2 = x + amplitude * Math.cos(t * TAU * 3 + rot + Math.PI);
            const py = y - length / 2 + t * length;
            ctx.beginPath();
            ctx.moveTo(px1, py);
            ctx.lineTo(px2, py);
            ctx.stroke();
        }
    }

    // ─── ADVANCED: TORUS FIELD ──────────────────────────────────
    /**
     * 2D projection of a torus field with φ-mesh.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x
     * @param {number} y
     * @param {number} majorR  - major radius
     * @param {number} minorR  - minor radius
     * @param {string} color
     * @param {number} [time=0]
     */
    function drawTorusField(ctx, x, y, majorR, minorR, color, time = 0) {
        const meshLines = 24;
        const rot = time * 0.25;

        ctx.save();
        ctx.translate(x, y);

        // Meridians
        for (let i = 0; i < meshLines; i++) {
            const phi = (i / meshLines) * TAU;
            ctx.beginPath();
            ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, lerp(0.1, 0.4, Math.abs(Math.cos(phi + rot))));
            ctx.lineWidth = 0.8;

            for (let j = 0; j <= 60; j++) {
                const theta = (j / 60) * TAU;
                const r = majorR + minorR * Math.cos(theta);
                const px = r * Math.cos(phi + rot);
                const py = r * Math.sin(theta) * 0.4 + minorR * Math.sin(theta) * 0.4; // perspective squish
                if (j === 0) ctx.moveTo(px, py);
                else ctx.lineTo(px, py);
            }
            ctx.stroke();
        }

        // Parallels
        for (let j = 0; j < 12; j++) {
            const theta = (j / 12) * TAU;
            const r = majorR + minorR * Math.cos(theta);
            const py = minorR * Math.sin(theta) * 0.8;

            ctx.beginPath();
            ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.2);
            ctx.lineWidth = 0.6;

            for (let i = 0; i <= 60; i++) {
                const phi = (i / 60) * TAU;
                const px = r * Math.cos(phi + rot);
                if (i === 0) ctx.moveTo(px, py);
                else ctx.lineTo(px, py);
            }
            ctx.stroke();
        }

        ctx.restore();
    }

    // ─── ADVANCED: SACRED MANDALA ───────────────────────────────
    /**
     * Multi-layered phi-harmonic mandala with 4D animation.
     * @param {CanvasRenderingContext2D} ctx
     * @param {number} x
     * @param {number} y
     * @param {number} radius
     * @param {string} color
     * @param {number} [time=0]
     * @param {number} [layers=4]
     */
    function drawSacredMandala(ctx, x, y, radius, color, time = 0, layers = 4) {
        ctx.save();
        ctx.translate(x, y);

        for (let layer = 0; layer < layers; layer++) {
            const layerRadius = radius * Math.pow(PHI_INV, layer);
            const petals = 5 + layer * 2;
            const layerRot = time * 0.2 * (layer % 2 === 0 ? 1 : -1);
            const alpha = lerp(0.6, 0.2, layer / layers);

            ctx.save();
            ctx.rotate(layerRot);

            // Petal arcs
            for (let i = 0; i < petals; i++) {
                const angle = (i / petals) * TAU;
                const px = layerRadius * Math.cos(angle);
                const py = layerRadius * Math.sin(angle);

                ctx.beginPath();
                ctx.arc(px, py, layerRadius * PHI_INV, 0, TAU);
                ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, alpha);
                ctx.lineWidth = lerp(1.5, 0.5, layer / layers);
                ctx.stroke();
            }

            // Connecting circle
            ctx.beginPath();
            ctx.arc(0, 0, layerRadius, 0, TAU);
            ctx.strokeStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, alpha * 0.5);
            ctx.lineWidth = 0.8;
            ctx.stroke();

            ctx.restore();
        }

        // Center jewel
        ctx.beginPath();
        ctx.arc(0, 0, 4, 0, TAU);
        ctx.fillStyle = color;
        ctx.fill();

        ctx.beginPath();
        ctx.arc(0, 0, 8, 0, TAU);
        ctx.fillStyle = rgba(typeof color === 'string' && color.startsWith('#') ? color : PALETTE.gold, 0.15);
        ctx.fill();

        ctx.restore();
    }

    // ─── COMPOSITE: FULL SCENE RENDERER ─────────────────────────
    /**
     * Render a complete sacred geometry scene to a canvas.
     * @param {HTMLCanvasElement} canvas
     * @param {number} time  - current time in seconds
     * @param {Object} [opts]
     */
    function renderScene(canvas, time, opts = {}) {
        const ctx = canvas.getContext('2d');
        const w = canvas.width;
        const h = canvas.height;
        const cx = w / 2;
        const cy = h / 2;
        const color = opts.color || PALETTE.gold;

        // Clear
        ctx.fillStyle = opts.background || PALETTE.void;
        ctx.fillRect(0, 0, w, h);

        // Layers
        if (opts.grid !== false) drawSacredGrid(ctx, w, h, time);
        if (opts.flowerOfLife) drawFlowerOfLife(ctx, cx, cy, opts.flowerRadius || 60, color, time, opts.flowerLayers || 3);
        if (opts.metatron) drawMetatronsCube(ctx, cx, cy, opts.metatronRadius || 100, color, time);
        if (opts.mandala) drawSacredMandala(ctx, cx, cy, opts.mandalaRadius || 150, color, time, opts.mandalaLayers || 4);
        if (opts.spiral !== false) drawPhiSpiral(ctx, cx, cy, opts.spiralRadius || Math.min(w, h) * 0.4, color, time);
        if (opts.flower) drawGoldenFlower(ctx, cx, cy, opts.flowerPetals || 300, opts.flowerMaxRadius || Math.min(w, h) * 0.4, color, time);
        if (opts.pentagon) drawPentagon(ctx, cx, cy, opts.pentagonRadius || 120, color, time, true);
        if (opts.doubleHelix) drawDoubleHelix(ctx, cx, cy, h * 0.7, 80, color, PALETTE.cyan, time);
        if (opts.torus) drawTorusField(ctx, cx, cy, opts.torusMajorR || 100, opts.torusMinorR || 30, color, time);
    }

    // ─── PUBLIC API ─────────────────────────────────────────────
    return {
        // Constants
        PHI,
        PHI_INV,
        GOLDEN_ANGLE,
        TAU,
        PALETTE,

        // Core drawing
        drawPhiSpiral,
        drawGoldenFlower,
        drawPhiPulse,
        drawPhiGrid,

        // Sacred patterns
        drawPentagon,
        drawFibonacciSpiral,
        drawMetatronsCube,
        drawFlowerOfLife,
        drawSacredGrid,

        // Advanced 4D
        drawDoubleHelix,
        drawTorusField,
        drawSacredMandala,

        // DOM animation
        animatePhiNode,

        // Scene renderer
        renderScene,

        // Helpers (exposed for composition)
        phiEase,
        pulse,
        phiOsc,
        rgba,
        lerp,
        clamp,
    };
})();

// UMD export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SacredGeometry;
} else if (typeof window !== 'undefined') {
    window.SacredGeometry = SacredGeometry;
}
