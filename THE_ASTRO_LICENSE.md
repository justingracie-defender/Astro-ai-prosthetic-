# THE ASTRO LICENSE v8.1.5

**Constitutional Safety Standard for Prosthetic and Assistive Devices**  
**Governed by:** LifeCore-16 Constitution v0.9.0  
**Updated:** 2026-06-02 — Added Lanier Principles

This document is a project safety standard and governance statement for Astro AI Prosthetics. It is not legal advice and should be reviewed by qualified counsel before being used as a formal software license.

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

Safety-relevant faults should be preserved in a tamper-evident trace suitable for replay and review. The ledger should include signals, decisions, denials, warnings, configuration versions, supervisor outcomes, and inspectability records.

## Article V: Lanier Principles — Inspectable AI

### Purpose

AI must not be treated as a black box when attached to a human body. It must show its work, remain grounded in training evidence, and accept independent verification before non-routine motion is allowed.

### 5.1 Traceable Training Influence

For any L2 or L3 action, the system should log the top five most influential training-data clusters, model exemplars, or retrieval neighborhoods that contributed to the decision. These records should be stored in the Spine Ledger for review.

### 5.2 Semantic Grounding Check

Before non-routine motion, the system should query the training or validation database for the closest ten relevant human examples. The motion may proceed only if the grounding check meets the configured confidence threshold and the safety supervisor independently approves.

### 5.3 Multi-Factor Safety Channel

All motion commands should require approval from two independent channels.

| Channel | Role |
|---|---|
| **Channel 1: Primary AI + EMG Decoder** | Estimates user intent and proposes a motion profile. |
| **Channel 2: Counterfactual Safety Estimator** | Separately checks force limits, face proximity, unsafe posture, and plausible adverse outcomes. |

Both channels must approve before non-routine motion proceeds. A Channel 2 veto should trigger immediate limp mode or another reviewed safe state. A Sanctuary Key or equivalent operator safety control may manually invoke Channel 2 review.

> **Core Invariant:** AI must explain itself, check reality, and accept a second opinion — especially when attached to a human body.
