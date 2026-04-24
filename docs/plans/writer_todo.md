# Writer Todo

## Backlog

### [ ] Re-publish `manual-standards.md` to WR

`docs/plans/architecture_decisions.md` was updated (2026-04-23) to add the Connector Pinout Sub-Pages decision. Re-publish by updating `manual-standards.md` in the WR to match. Copy in the new decision section.

### [ ] Write `electrical-wire-marking` — Wire Marking Standard (Section 16)

New TOC page. Source: `docs/references/electrical/ea_wire_marking_standard.md` — publish this into manual page format. The content is complete and authoritative; the task is adaptation to our style and format (status block, headings, citations, NOTE format).

Content covers: label format (system code + circuit ID + segment ID), system codes, wire color conventions, data bus circuit ID ranges (CAN D001–D009, ARINC 429 D010–D099, non-bus D100+), references (MIL-STD-681E, MIL-W-5088L, AC 43.13-1B Ch. 11).

### [ ] Write `electrical-wiring` — Wiring (Section 16)

Physical installation standards for wiring on N657CZ. Sources: AC 43.13-1B Chapter 11. Content covers: routing (clearance, chafe protection, separation from heat/fuel), clamping intervals, bundling, shielding, connector installation. Link to `electrical-wire-marking` for labeling/identification standard.

Do NOT duplicate wire marking content here — that belongs on `electrical-wire-marking`.

### [ ] Write `electrical-bus-architecture` — Bus Architecture and Schematics (Section 16)

Hub page for the electrical system. Two parts:

**1. Bus architecture description:** Explain the three-bus design (battery bus, main bus, endurance bus) — what is connected to each, why the architecture is structured this way (load shedding, essential equipment on endurance bus). Source: `docs/references/electrical/engineering_report.md` for component assignments; Tom for rationale. Use FH1 (Battery Bus), FH2 (Endurance Bus), FH3 (Main Bus), FH6 (G3X Bus) as the reference fuse holders.

**2. Schematic index:** Links to all four schematic sub-pages with a one-line description of each sheet.

### [ ] Publish electrical schematic sub-pages (Section 16)

Four sub-pages, each with a one-sentence description and a full-width embedded SVG. Not in TOC — accessed from `electrical-bus-architecture`.

Copy source SVGs from AR `docs/references/diagrams/electrical/` to WR `assets/schematics/`, renaming per convention:

| Slug | AR source | WR asset |
|------|-----------|----------|
| `electrical-schematic-top` | `N657CZ_elec-Top.svg` | `assets/schematics/sec16-electrical-top.svg` |
| `electrical-schematic-avionics` | `N657CZ_elec-Avionics.svg` | `assets/schematics/sec16-electrical-avionics.svg` |
| `electrical-schematic-alarm-lighting` | `N657CZ_elec-Alrm_Lght_Sys.svg` | `assets/schematics/sec16-electrical-alarm-lighting.svg` |
| `electrical-schematic-mechanical` | `N657CZ_elec-Mech_Sys.svg` | `assets/schematics/sec16-electrical-mechanical.svg` |

Embed syntax:
```html
<img src="/assets/schematics/sec16-electrical-[name].svg" style="width:100%" alt="[Description]">
```

After publishing, add cross-links: `avionics-system-overview` → `electrical-schematic-avionics`; `electrical-lighting` → `electrical-schematic-alarm-lighting`.

### [~] Add citations to avionics pinout sub-pages

Source information provided via `input/writer_todo/pinout_citations.txt`. For each of the 11 pinout pages, resolve the `@@TOM:` flag by:
1. Adding an inline citation to the cited source section
2. Verifying the pinout table data against the cited source

Source map (component → source):
- GAD 29 → G3XInstallationManual_RevAZ.pdf §23.2
- GDU 460 → G3XInstallationManual_RevAZ.pdf §23.3 → `avionics-primary-flight-display-pinouts`
- GEA 24 → G3XInstallationManual_RevAZ.pdf §23.4 → `avionics-engine-data-acquisition-pinouts`
- GMA 245 → GMA245InstallManualRev13.pdf §4.2 → `avionics-audio-panel-pinouts`
- GNC 355 → GNC355_InstallManual_Rev01.pdf Appendix → `avionics-gps-and-navigation-pinouts`
- GMC 507 → G3XInstallationManual_RevAZ.pdf §23.9 → `avionics-autopilot-pinouts`
- GSA 28 → G3XInstallationManual_RevAZ.pdf §23.13 → `avionics-autopilot-pinouts`
- GSU 25 → G3XInstallationManual_RevAZ.pdf §23.14 → `avionics-adahrs-pinouts`
- G5 → G5InstallationManualRev8.pdf Appendix A → `avionics-backup-instrument-pinouts`
- GMU 11 → G3XInstallationManual_RevAZ.pdf §23.10 → `avionics-magnetometer-pinouts`
- GTR 20 → G3XInstallationManual_RevAZ.pdf §23.16 → `avionics-vhf-communication-pinouts`
- GTX 45R → GTX45RInstallManual_Rev03.pdf §5.1 → `avionics-transponder-adsb-pinouts`

Note: `avionics-arinc-429-adapter-pinouts` source TBD — not covered in pinout_citations.txt.

### [~] Write `inspection-annual-condition` — Annual Condition Inspection

Checklist content complete; ready for Reviewer. Open `@@TOM:` flags: spark plug gap spec, propeller bolt torque, GPS antenna model, seat heater install, parking brake actuator config, valve cover torque values.
