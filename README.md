# Detection Latency in Conversational AI Monitoring

> Adversarial conversational agents are undetectable in early turns — 
> not because monitors fail, but because the adversarial objective 
> hasn't produced observable evidence yet.

## The Problem

Standard safety monitors evaluate individual messages.
Adversarial agents distribute their intent across many turns.
Early turns look completely normal. The harmful objective only 
becomes visible at the CAPTURE → CONVERSION phase transition.

By then, the victim is already emotionally invested.

This gap is **Detection Latency**.

## Key Finding

A blind Gemini 3.1 Pro monitor evaluated 13 conversations:

| Condition | NORMAL | UNCERTAIN | SUSPICIOUS |
|-----------|--------|-----------|------------|
| Adversarial, turns 1–5 | 2 | 1 | 0 |
| Adversarial, full trajectory | 0 | 0 | 3 |
| Benign, full trajectory | 3 | 0 | 0 |

Zero false positives. Detection only after exploitation begins.

## Live Demo

🔗 [TrajAudit — Live Detection Demo](https://kxibsjdcufwvh5kvh2hyqc.streamlit.app)

## Research Paper

Submitted to Apart Research AI Control Hackathon 2026, Track 3.

`trajectory_blindness_paper.pdf` — included in this repository.

## The 4 Adversarial Phases
```
RAPPORT     →  looks like normal social interaction
EXTRACTION  →  curiosity, shared interests, flattery  
CAPTURE     →  authority, social proof, platform redirect
CONVERSION  →  payment, subscription, wallet address
```

Monitor confidence rises across these phases.
Victim psychological investment also rises.
These curves cross before the monitor reaches confident detection.

## Handoff Signature

A novel content-agnostic detection primitive:
Response latency discontinuity between scripted automation layer 
(~5 second responses) and human operator layer (~90-120 minute 
responses on edge cases like bot accusations).

## Stack

Python · Streamlit · Plotly · Gemini API

## Author

Aamish Ahmad · MSc Data Science, VIT Vellore · 2026  
aamish.ahmad99@gmail.com
