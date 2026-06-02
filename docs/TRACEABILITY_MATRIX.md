# Astro — AI Prosthetics — Traceability Matrix v1.0

This matrix maps early Astro safety requirements to implementation evidence. It is a planning artifact, not a claim of certification or regulatory clearance.

| Source Area | Requirement | Astro Implementation Target | Repository Evidence |
|---|---|---|---|
| IMDRF / FDA principles | Lifecycle risk management and human oversight | Human veto, deterministic safety supervisor, and daily self-test | `THE_ASTRO_LICENSE.md` Article IV; `src/astro/safety_supervisor.py` |
| FDA post-market safety thinking | Preserve incident evidence and fault review | Spine Ledger concept and fault replay package | `docs/SAFETY_CASE_SUMMARY.md`; future `logs/` or audit module |
| Health Canada safety expectations | Diverse-user and environment-aware validation | Mannequin trials, red-team testing, and environmental cases | `docs/RED_TEAM_REPORT.md`; `docs/testing.md` |
| ISO 13485 design-control concept | Traceable design controls and review gates | Hardware force cap target, limp mode, and configuration limits | `configs/default_limits.yaml`; test suite |
| LifeCore-16 governance | L0 safety before helpfulness or speed | Hardware-first safety and fail-closed supervisor | `docs/safety.md`; `THE_ASTRO_LICENSE.md` |

## References

[1]: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device "FDA — Artificial Intelligence and Machine Learning in Software as a Medical Device"  
[2]: https://www.imdrf.org/working-groups/artificial-intelligence-medical-devices "IMDRF — Artificial Intelligence Medical Devices"  
[3]: https://www.iso.org/standard/59752.html "ISO 13485:2016 — Medical devices quality management systems"  
[4]: https://www.canada.ca/en/health-canada/services/drugs-health-products/medical-devices.html "Health Canada — Medical Devices"
