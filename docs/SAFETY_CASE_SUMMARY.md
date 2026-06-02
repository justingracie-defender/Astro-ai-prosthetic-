# Safety Case Summary — Astro — AI Prosthetics v8.1.4

**Top-Level Claim:** Astro should maintain safe operation under foreseeable research, simulation, and pre-human validation conditions when deterministic safety limits, human veto, hardware force limiting, and limp-mode behavior are correctly implemented.

| Hazard | Initial Mitigation | Evidence Target |
|---|---|---|
| Excessive force to user or bystander | Hardware force cap target, deterministic supervisor, and limp mode | Boundary tests, mannequin force logs, and hardware verification. |
| Unintended motion | Human veto, confidence threshold, and no-motion default on uncertainty | Unit tests, fault injection, and red-team reports. |
| Failure during use | Daily self-test, recalibration lockout, and Spine Ledger | Diagnostic logs and replayable fault traces. |
| Environmental stress | Cold, heat, humidity, vibration, and interference validation | Environmental chamber reports and stress-test records. |
| Overtrust or premature deployment | Clear warnings and review gates | README status, risk register, and release checklist. |
| Black-box AI influence | Traceable training influence, semantic grounding, and independent safety channel | Article V and future Spine Ledger entries. |

## Residual Risk

Residual risk includes unknown emergent faults, sensor ambiguity, mechanical wear, model drift, and unvalidated human factors. These risks should be reduced through simulation, hardware-in-the-loop testing, clinician review, independent safety review, and documented release gates.
