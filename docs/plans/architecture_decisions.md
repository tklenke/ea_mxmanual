# Architecture Decisions

This document records architectural decisions made during the design of the ea_mxmanual maintenance manual. It captures the reasoning behind structural choices so future sessions can understand intent rather than just outcome.

**Note to Architect:** After the TOC audit is complete, create a task for the Writer to migrate this document into the Otterwiki under a dedicated Architecture folder. Update `claude/content_development_overview.md` to reference the Otterwiki location.

---

## Manual Scope

**Decision:** This is a maintenance manual only. Fabrication and build content is out of scope.

**Reasoning:** The aircraft is built. The manual is for the owner/maintainer performing ongoing maintenance and inspection. Build procedures are not needed and would create confusion about what applies to a completed aircraft.

**Effect on TOC:**
- Removed `flight-controls-fabrication-notes` (was Section 10)
- Removed `flipping-fuselage` (was Section 5)

---

## Section 5: Servicing as Master Index

**Decision:** Section 5 is a master index of all servicing tasks, not a collection of procedures. Each entry describes the task, its service interval, and points to the full procedure in its home section.

**Reasoning:** A maintainer planning a service event needs a single place to see everything that requires attention. Duplicating procedures in Section 5 would create maintenance burden and risk of conflicting information.

**Effect:** Procedures like oil change live in Section 12 (Power Plant). Section 5 lists "Oil and Filter" with interval and a pointer to Section 12.

---

## Section 6: Inspection Structure

**Decision:** Three inspection tiers:
- 6.1 Annual Condition Inspection — single comprehensive checklist page
- 6.2 Post-Cross-Country Check — focused on stress/extended use items
- 6.3 Periodic Check — mid-season, broader than 6.2 but lighter than annual

**Reasoning:** Experimental aircraft under annual condition inspection only. The 6.2 and 6.3 tiers reflect practical maintenance intervals (roughly 10 hours and 50 hours of flying) without implying FAA-mandated tach-time requirements.

**Note:** 6.1 kept as a single page (not broken into sub-pages by system) to preserve its utility as a checklist. If it grows unwieldy, reconsider at next architectural review.

---

## Section 15 Folded into Section 16

**Decision:** Section 15 (Instruments) is eliminated. Instrument content is covered in Section 16 (Avionics).

**Reasoning:** The aircraft has a full glass panel (GDU 460 PFD, G5 backup, GEA 24 EIS). The traditional instruments/avionics boundary assumes steam gauges. On this aircraft, the displays and the avionics generating the data are the same hardware. Splitting them across two sections would force arbitrary decisions about where content belongs and require cross-referencing for every topic.

---

## Weight and Balance as Standalone Section

**Decision:** Weight and Balance is its own top-level section, not a sub-section of Section 3 (Aircraft General).

**Reasoning:** W&B is a recurring maintenance task with its own procedures, not just background information. It warrants a dedicated section so a maintainer can find it directly.

---

## Section 1: Remove Meta-Content

**Decision:** Removed `Instructions for development of Design and Troubleshooting Documentation` from Section 1.

**Reasoning:** This was guidance for Claude/Tom during manual development, not content for a maintainer. It does not belong in the published manual.

---

## Section 2: Safety Precautions Structure

**Decision:** Five pages covering hazards specific to this aircraft:
- Electrical Safety
- Fire and Fuel Hazards
- Composite Material Hazards
- Fluids and Chemicals
- General Shop Safety

**Reasoning:** Kept aircraft-specific. Generic shop safety content excluded. Composite material hazards included because fiberglass dust and epoxy are present in both repair work and routine inspection of this airframe.

---

## Section 3: Aircraft General Structure

**Decision:** Three pages:
- 3.1 General Layout and Configuration
- 3.2 Aircraft Dimensions and Weight
- 3.3 Systems Overview

**Reasoning:** 3.3 added to give a maintainer context before diving into individual systems. A high-level summary with cross-references reduces the chance of someone working on a system without understanding how it fits into the whole.

---

## Section 4: Ground Handling Structure

**Decision:** Four pages:
- 4.1 Towing Procedures
- 4.2 Jacking and Leveling
- 4.3 Tiedown and Parking
- 4.4 Storage

**Reasoning:** Tiedown separated from Jacking (previously misplaced as a sub-page of 4.2). Storage added as a maintenance task in its own right (fuel stabilizer, pitot cover, control locks, etc.).

---

## Section 5: Servicing Index Contents

**Decision:** The following tasks are indexed in Section 5 (each with interval and pointer to home section):

- Fueling
- Oil and Filter
- Spark Plugs
- Air Filter
- Cooling System
- Propeller
- Fuel Filters
- Brakes (fluid and pads)
- Tires and Wheels
- Battery Service (main and brownout)
- Pitot/Static System
- Control Surface Hinges and Linkages
- Canopy and Door Seals
- Exterior Finish
- Lighting
- Interior (seats and seat belts)
- Avionics Software Updates
- Wing Removal and Installation
