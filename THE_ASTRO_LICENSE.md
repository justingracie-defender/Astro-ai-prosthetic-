# THE ASTRO LICENSE v8.1.4

**Constitutional Safety Standard for Prosthetic and Assistive Devices**  
**Governed by:** LifeCore-16 Constitution v0.9.0

This document is a project safety standard and governance statement for Astro — AI Prosthetics. It is not legal advice and should be reviewed by qualified counsel before being used as a formal software license.

## Article IV: Prosthetic Validation and Safe Failure

### 4.1 Lab First Rule

All motion profiles, EMG models, adaptive controllers, and AI-assisted intent models must pass instrumented mannequin testing before human use. Instrumentation should include force sensing for face, eye, neck, torso, and user-contact zones where applicable.

**Pass Target:** No foreseeable fault should exceed the configured hard force limit. Anomalous slap-like motion should default to a minimal-force safe state.

### 4.2 Safe Failure Mode — Limp Over Lock

Any serious fault should trigger hardware limp mode or another compliant safe state. A locked, rigid, or high-force arm on failure is prohibited unless a reviewed clinical or safety case proves that a different behavior is safer for a specific assistive device.

### 4.3 Red-Team Adversarial Testing

The system must be challenged with EMG spikes, wet hands, cold muscles, vibration, electromagnetic interference, low battery, unexpected impacts, and sensor dropout.

**Pass Target:** The human veto path always wins, and hardware force limits remain enforceable independent of AI output.

### 4.4 Daily Self-Test

A short daily diagnostic should verify sensors, actuator limits, battery state, calibration, emergency stop, limp behavior, and logging readiness. Failure should prevent ordinary motion and allow only reviewed tool, maintenance, or diagnostic modes.

### 4.5 Spine Ledger

Safety-relevant faults should be preserved in a tamper-evident trace suitable for replay and review. The ledger should include signals, decisions, denials, warnings, configuration versions, and supervisor outcomes.

> **Core Invariant:** Safety is hardware. The arm must survive Kingston winter before touching a person.
