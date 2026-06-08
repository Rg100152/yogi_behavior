# Yogi-Behavior: Biometric Intent Analysis Engine

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey)](https://github.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Yogi-Behavior is an insider threat detection simulation tool written in Python. It models a modern **User and Entity Behavior Analytics (UEBA)** system, processing user behavioral analytics through simulated keystroke dynamics (typing speed metrics) and operational asset sequencing. 

The framework utilizes statistical deviations (Z-score variations) to detect anomalies, instantly flagging indicators of account compromise or malicious insider maneuvers.

---

## ── Key Features ──

* **Zen Equilibrium Palette:** Built-in customized 20-color ANSI terminal aesthetic matrix for high-fidelity incident visibility.
* **Behavioral Signature Engine:** Tracks behavioral telemetry and matches execution paths against unique user historic profiles.
* **Real-time Deviation Tracking:** Utilizes moving mathematical means and standard deviations to measure anomalous operations in Sigma units.
* **Automated Threat Mitigations:** Simulates real-time tactical alert flashing when anomalous operations surpass security thresholds ($> 2.5\sigma$).

---

## ── Architectural Overview ──

```text
  [ User Action ] ───► ( Typing Speed & Resource Target )
                                │
                                ▼
                  [ Behavioral Signature Engine ]
                                │
               ├── Real-time Z-Score Matrix Calculation
               └── Markov Sequence Verification
                                │
                                ▼
                 [ Security Operation Sentry ]
                                │
         ┌──────────────────────┴──────────────────────┐
         ▼                                             ▼
  ( Deviation < 2.5σ )                          ( Deviation > 2.5σ )
  Log Normal Operation                          FLASH SYSTEM CRITICAL ALERT
