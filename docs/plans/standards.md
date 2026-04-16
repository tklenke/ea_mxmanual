# Content Standards

This document defines formatting standards for the ea_mxmanual maintenance manual.

---

## NOTE Format

### General Note

Use a NOTE to call out important information that does not fit in the main flow of the procedure or description.

```
> **NOTE:** [Text of note here.]
```

**Example:**
> **NOTE:** Torque values apply to dry, unlubricated fasteners unless otherwise specified.

---

### Source Conflict Note

When a manufacturer Technical Data Sheet (TDS) conflicts with AC 43.13 and the TDS is followed, a source conflict NOTE is required.

```
> **NOTE:** This [procedure/specification/value] follows [TDS name] ([tds/filename]) rather
> than AC 43.13 ([ch##_p###]). Where these sources conflict, the manufacturer's Technical
> Data Sheet takes precedence. See both documents for full context.
```

**Fields:**
- `[procedure/specification/value]` — what specifically is affected (e.g., "cure time", "application procedure", "torque specification")
- `[TDS name]` — the common name of the TDS (e.g., "Permatex Thread Sealant TDS")
- `[tds/filename]` — the filename in `docs/references/tds/` (e.g., `Permatex_Thread_Sealant_TDS.pdf`)
- `[ch##_p###]` — the AC 43.13 chapter and page reference (e.g., `ch01_p001`)

**Example:**
> **NOTE:** This cure time follows the Permatex Thread Sealant TDS (`Permatex_Thread_Sealant_TDS.pdf`) rather than AC 43.13 (ch01_p001). Where these sources conflict, the manufacturer's Technical Data Sheet takes precedence. See both documents for full context.
