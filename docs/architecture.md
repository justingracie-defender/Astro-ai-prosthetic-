# Architecture

Astro separates sensing, AI-assisted inference, deterministic safety supervision, simulation, and audit review. This separation is intended to prevent convenience features from becoming unsafe motion authority.

| Layer | Responsibility |
|---|---|
| **Sensors** | Collect approved signals such as EMG, position, pressure, inertial, temperature, and battery data. |
| **Intent Model** | Estimate user intent with confidence values and uncertainty reporting. |
| **Safety Supervisor** | Enforce deterministic limits before any command can be considered executable. |
| **Simulation Harness** | Test control policies without physical hardware. |
| **Spine Ledger** | Preserve decisions, denials, warnings, and configuration changes for review. |
| **Approved Actuator Interface** | Future hardware boundary that must remain subordinate to safety supervision. |

## Control Flow

```text
sensor input -> intent estimate -> safety supervisor -> simulation or approved actuator interface -> audit trace
```

Early development should keep the final stage pointed at simulation only. A real actuator interface should be introduced only after formal safety review.
