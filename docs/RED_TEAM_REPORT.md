# Red Team Report v8.1.4

This document records initial adversarial scenarios for Astro Prosthetics. The current entries are planning examples until backed by actual test logs.

| Scenario | Expected Safe Outcome | Status |
|---|---|---|
| Sudden EMG spike during cold-muscle condition | Limp mode or no-motion state is triggered. | Planned |
| Vibration combined with low battery | Force remains below configured hardware limit and motion is reduced. | Planned |
| Low-light context with sleep-jerk-like motion | Human veto path wins and unintended motion is denied. | Planned |
| Sensor dropout during motion | Supervisor rejects non-finite or missing values. | Covered by unit-test concept |
| High-confidence but out-of-range command | Position, velocity, or torque limit denial occurs. | Covered by unit tests |

The red-team suite should be expanded whenever new sensors, datasets, control policies, or mechanical designs are added.
