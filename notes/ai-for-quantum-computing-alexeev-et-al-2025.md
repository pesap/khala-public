---
title: Artificial intelligence for quantum computing - Review
created: 2025-05-07
source: https://www.nature.com/articles/s41467-025-65836-3
visibility: public
semantic_cluster: quantum-computing
tags:
  [
    "artificial-intelligence",
    "quantum-computing",
    "machine-learning",
    "quantum-error-correction",
    "deep-learning",
    "transformers",
    "reinforcement-learning",
    "nature-communications",
    "review",
  ]
---

# Artificial intelligence for quantum computing

Review article in Nature Communications, volume 16, Article number 10829,
published December 2025.

Authors: Yuri Alexeev, Marwa H. Farag, Taylor L. Patti, Mark E. Wolf, Natalia
Ares, Alán Aspuru-Guzik, Simon C. Benjamin, Zhenyu Cai, Shuxiang Cao,
Christopher Chamberland, Zohim Chandani, Federico Fedele, Ikko Hamamura,
Nicholas Harrigan, Jin-Sung Kim, Elica Kyoseva, Justin G. Lietz, Tom Lubowe,
Alexander McCaskey, Roger G. Melko, Kouhei Nakaji, Alberto Peruzzo, Pooja Rao,
Bruno Schmitt, Timothy Costa, et al.

## Overview

Quantum computing faces scaling challenges across hardware design, calibration,
error correction, and operation. This review surveys how artificial
intelligence techniques are being applied across the full quantum computing
stack to accelerate progress toward fault-tolerant quantum computation.

The article covers AI applications from device design through preprocessing,
control, quantum error correction, and postprocessing. It examines both
near-term NISQ development and long-term fault-tolerant workflows. The review
emphasizes that AI cannot replace quantum computers due to exponential
classical simulation limits, but may become essential infrastructure for
operating them.

## Core Argument

AI for quantum not quantum for AI:
The review focuses solely on AI assisting quantum computing development, not
the longer-term prospect of quantum computers enhancing AI.

Exponential scaling barrier:
Classical AI cannot efficiently simulate generic quantum systems. Quantum
systems grow exponentially in description complexity with each added qubit.
AI serves as complementary tool for interpreting and controlling quantum
processes, not as substitute for quantum hardware.

Full stack integration:
Useful quantum computing requires heterogeneous architecture combining
fault-tolerant quantum hardware with accelerated supercomputers. AI may serve
as the control brain integrating these components.

Workflow organization:
The review follows causal sequence of quantum computer operation: device
design, preprocessing, control and optimization, quantum error correction,
and postprocessing.

## Key Applications

Device design:
AI methods search design spaces for superconducting circuits, photonic systems,
semiconductor qubits, quantum dots, and trapped atoms. Applications include
multi-qubit operation design, physical geometry optimization, and quantum
optical setup generation for entangled states.

Preprocessing:
Circuit synthesis and compilation using generative models to produce shorter,
more efficient quantum circuits. AI adapts circuits to specific hardware
characteristics and transfers optimizations between problems.

Control and optimization:
Automated tuning of qubits, design of control pulses, maintenance of device
stability, and discovery of optimal operating points. Reinforcement learning
for sequential decision-making in dynamic environments.

Quantum error correction:
Neural network decoders for recognizing error patterns and decoding syndrome
measurements. AI assistance in discovering better error-correcting codes.
Critical latency constraints require extremely fast inference.

Postprocessing:
Measurement signal classification, error mitigation from noisy outputs, and
readout error correction. Machine learning for distinguishing qubit states in
noisy measurement data.

## AI Methods Surveyed

Deep neural networks:
Backpropagation-based architectures learning multiple data abstractions.
Includes discriminative and generative model families.

Transformer models:
Parallelizable sequence learning with long-range and bidirectional context.
Popularized by GPT family for language and code applications.

Reinforcement learning:
Sequential decision-making via reward signals. Used for control optimization
and automated calibration in dynamic environments.

Diffusion models:
Random walk-based generative models learning denoising processes. Applied to
circuit synthesis and quantum optical design.

Transfer learning:
Iterative pre-optimization in progressively realistic substrates for handling
simulation-to-hardware gaps.

## Critical Limitations

Training data scarcity:
Real quantum data is expensive and noisy. Simulated data may misrepresent
actual hardware behavior causing distribution shift failures.

Scaling challenges:
Methods demonstrated on small qubit counts may not generalize to large-scale
systems. Context length and computational limits constrain LLM-based
approaches.

Latency constraints:
Quantum error correction requires real-time decoding faster than syndrome
cycle times. Data movement and hardware implementation dominate practical
decoder performance.

Speed and hardware integration:
AI decoders require FPGA GPU ASIC implementation with bounded memory and
temperature constraints. Batching and worst-case latency matter for fault
tolerance.

Trust and verification:
AI predictions lack transparent proof, risky for scientific hardware. Training
on wrong noise models produces misleading results. Overfitting to benchmark
circuits limits generalization.

## Implementation Requirements

High-performance computing:
Training requires accelerated GPU computing and supercomputer resources.
Simulation-based training data generation is computationally expensive.

Cross-disciplinary expertise:
Effective application requires combining quantum physics, machine learning,
software engineering, and hardware architecture knowledge.

Platform standards:
Open ecosystems like CUDA-Q for heterogeneous quantum supercomputing. Shared
infrastructure for compiler optimization and hardware abstraction.

## Academic Review Summary

Core claim:
Modern AI methods are advancing nearly every layer of quantum computing and
may be essential infrastructure for scaling toward useful fault-tolerant
quantum computation.

Methodological gaps:
No systematic review methodology with search protocol or inclusion criteria.
Weak distinction between proof-of-concept and deployable technology.
Taxonomy organized by workflow rather than evidence strength or technical
constraints. No benchmark normalization across methods. Limited treatment
of negative results and failure modes.

Unsupported claims:
AI might be the only tool capable of solving scaling problems overstates
capabilities relative to existing non-AI methods. AI decoders provide
superior accuracy broadly despite massive training data requirements and
latency constraints. Diffusion models are precursors to transformers is
factually incorrect. All popular qubit modalities prevented from
below-threshold operation is imprecise without threshold definitions.

Missing evidence:
Data provenance and reproducibility details across applications.
Generalization testing across devices noise regimes and circuit sizes.
Latency and systems evidence for real-time QEC including data transfer
memory bandwidth and worst-case behavior. Statistical guarantees and
uncertainty quantification for AI-based error mitigation. Energy and compute
cost accounting for training relative to classical baselines.

Conflicts with literature:
Classical AI cannot generally evade quantum simulation hardness per
complexity theory. AI decoder optimism conflicts with known scaling barriers
for latency adaptability and hardware implementation. Generative circuit
synthesis faces compilation hardness limits not overcome by small demonstrations.
Foundation model analogy to language models is unevidenced for quantum computing
due to lack of internet-scale datasets and stable hardware distributions.
AI autonomy conflicts with experimental safety requirements for fragile
quantum devices requiring formal constraints and human oversight.

Verdict:
Valuable broad map of AI for quantum computing as expert narrative review.
Taxonomy and breadth are strengths. Evidence weighting overgeneralized claims
insufficient benchmark comparability and occasional technical overstatement
are weaknesses. Central thesis that AI will be important across QC stack is
plausible. Stronger thesis that AI may be essential or uniquely capable is
not established by evidence presented.

## Related

- [[Quantum Error Correction]] ([Quantum Error Correction](quantum-error-correction.md))
- [[Machine Learning for Physics]] ([Machine Learning for Physics](machine-learning-for-physics.md))
- [[Quantum Computing Hardware]] ([Quantum Computing Hardware](quantum-computing-hardware.md))
- [[Transformer Models]] ([Transformer Models](transformer-models.md))
- [[Reinforcement Learning]] ([Reinforcement Learning](reinforcement-learning.md))
- [[Nature Communications]] ([Nature Communications](nature-communications.md))

## Backlinks
