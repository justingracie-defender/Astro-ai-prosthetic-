# Astro AI Prosthetics

**Safe, high-performance AI-assisted prosthetic limbs and assistive devices.**

**Version:** v8.1.5 — Lanier Principles Integration  
**Safety License:** THE_ASTRO_LICENSE v8.1.5  
**Author:** Justin Gracie, Kingston ON, Canada  
**Governance:** LifeCore-16 Constitution v0.9.0, as developed in `prometheus-h`

> **Philosophy:** Speed belongs to human intent. Safety belongs to immutable hardware limits. AI must show its work.  
> **Core Promise:** Fast arms, safe faces. No slap. No lock-up. No mystery failures.

Astro AI Prosthetics is a research repository for AI-assisted prosthetic limb and assistive-device control. It is intentionally separate from the `prometheus-h` home-robot repository because a human-worn prosthetic system has different physics, hazards, review requirements, and validation obligations than a mobile or household robot.

## Safety Notice

This repository is **experimental**. It is not a medical device, not a certified prosthetic control system, not clinical advice, and not ready for unsupervised human use. Any future hardware integration or human testing must be reviewed by qualified clinicians, safety engineers, and applicable regulatory professionals before use.

## Vision

Astro delivers natural-speed prosthetic control with conservative safety validation and inspectable AI. Inspired by Jaron Lanier's emphasis on human agency and accountability in digital systems, the project treats AI control as something that must be traceable, grounded in real data, and independently checkable before it can influence motion. Every motion profile should be tested in simulation, instrumented mannequin trials, environmental stress cases, and adversarial red-team scenarios before it ever touches a person.

## Key Features

| Feature | Design Intent |
|---|---|
| **EMG + AI hybrid control** | Use AI to assist intent interpretation while preserving deterministic safety gates. |
| **Human veto path** | Keep human override outside model discretion and above ordinary control logic. |
| **Hardware force cap target** | Treat force limiting as a hardware-enforced boundary, not a model promise. |
| **Limp Mode on fault** | Prefer compliant safe failure over locked or rigid failure. |
| **Daily self-test** | Require a short diagnostic and recalibration lockout before normal operation. |
| **Environmental resilience testing** | Validate performance across Kingston-like cold, heat, humidity, vibration, and interference cases before real deployment. |
| **Spine Ledger** | Preserve fault traces for replay, review, and accountability. |
| **Lanier Principles** | Add traceable training influence, semantic grounding checks, and multi-factor safety review for non-routine motion. |

## Safety Governance

See [`THE_ASTRO_LICENSE.md`](THE_ASTRO_LICENSE.md) for the full constitutional safety standard.

| Article | Focus |
|---|---|
| **Article IV** | Prosthetic validation and safe failure. |
| **Article V** | Lanier Principles for inspectable AI. |

## Repository Structure

```text
Astro-ai-prosthetic-/
├── THE_ASTRO_LICENSE.md
├── docs/
│   ├── RED_TEAM_REPORT.md
│   ├── SAFETY_CASE_SUMMARY.md
│   ├── TRACEABILITY_MATRIX.md
│   ├── architecture.md
│   ├── risk_register.md
│   ├── safety.md
│   └── testing.md
├── src/
│   └── astro/
│       ├── __init__.py
│       ├── intent.py
│       ├── safety_supervisor.py
│       └── simulation.py
├── tests/
│   ├── test_intent.py
│   └── test_safety_supervisor.py
├── configs/
│   └── default_limits.yaml
├── pyproject.toml
└── requirements.txt
```

## Cross-Project Link

Astro integrates conceptually with LifeCore-16 governed home environments from `prometheus-h`, but it should not inherit home-robot assumptions automatically. The shared principle is simple: **same L0 safety philosophy, different physics**.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src pytest
```

## Status

Active development scaffold. Public visibility does not imply safety certification, clinical readiness, regulatory clearance, or production readiness.

**For the kids.** Fast when you want it. Safe and explainable when you need it.
