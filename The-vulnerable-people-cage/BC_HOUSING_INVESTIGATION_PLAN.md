# BC Supportive Housing Operator Network Investigation Plan

## Objective
Map ALL supportive housing operators in British Columbia and their connections, including:
- Organization details (name, locations, units, funding)
- Incident reports (deaths, criminal investigations, lawsuits)
- Network connections between operators

## Phase 1: Primary Operator Research (15 searches)

| # | Search Query | Target Data |
|---|--------------|-------------|
| 1 | BC Housing supportive housing operators list | Official BC Housing provider database |
| 2 | BC supportive housing providers complete list | Comprehensive operator registry |
| 3 | BC Housing funded non-profit operators | Non-profit operators with provincial funding |
| 4 | Lookout Society housing operations | Units, locations, funding |
| 5 | RainCity Housing operations | Units, locations, funding |
| 6 | Atira Women's Resource Society housing | Units, locations, funding |
| 7 | PHS Community Services operations | Units, locations, funding |
| 8 | Lu'ma Native Housing operations | Units, locations, funding |
| 9 | M'akola Housing Society operations | Units, locations, funding |
| 10 | CMHA supportive housing BC | Units, locations, funding |
| 11 | John Howard Society BC operations | Units, locations, funding |
| 12 | Salvation Army supportive housing BC | Units, locations, funding |
| 13 | Purpose Society housing | Units, locations, funding |
| 14 | Options Community Services housing | Units, locations, funding |
| 15 | BCNPHA member organizations list | BC Non-Profit Housing Association members |

## Phase 2: Incident & Legal Research (5 searches)

| # | Search Query | Target Data |
|---|--------------|-------------|
| 16 | BC supportive housing death incidents | Deaths in facilities |
| 17 | BC supportive housing criminal investigations | Criminal probes |
| 18 | BC supportive housing lawsuits | Legal actions |
| 19 | BC Housing death in custody | Deaths under BC Housing |
| 20 | BC supportive housing overdose deaths | Overdose-related fatalities |

## Phase 3: Data Collection Structure

For each operator, create record:
```json
{
  "organization_name": "",
  "locations": [],
  "number_of_units": 0,
  "funding_source": "",
  "death_incidents": [],
  "criminal_investigations": [],
  "lawsuits": [],
  "connections": []
}
```

## Phase 4: Network Mapping

Identify connections:
- Shared board members
- Common funding sources
- Joint ventures
- Contractual relationships
- Geographic overlap

## Tools to Use
- websearch: For initial discovery
- webfetch: For full page content extraction
- Write to file: For compiling final report

## Output
Comprehensive markdown report with:
1. Executive summary
2. Operator profiles (15+ organizations)
3. Incident database
4. Network visualization (text-based)
5. Source citations