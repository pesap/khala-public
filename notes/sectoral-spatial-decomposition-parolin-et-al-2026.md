---
title: Sectoral and spatial decomposition methods for multi-sector capacity expansion models
created: 2026-04-27
source: https://doi.org/10.1016/j.enconman.2026.121356
visibility: public
semantic_cluster: operations-research
tags:
  [
    "benders-decomposition",
    "capacity-expansion",
    "energy-system-modelling",
    "linear-programming",
    "multi-sector",
    "spatial-decomposition",
    "sectoral-decomposition",
    "budget-based-formulation",
    "dolphyn",
  ]
---

# Sectoral and spatial decomposition methods for multi-sector capacity expansion models

Journal article in Energy Conversion and Management, Volume 358, June
2026, 121356.

Authors: Federico Parolin, Yu Weng, Paolo Colbertaldo, Ruaridh Macdonald.
Affiliations: Politecnico di Milano; MIT Energy Initiative. DOI: 10.1016/j.enconman.2026.121356

## Overview

Capacity expansion models (CEMs) for energy planning face computational
intractability when high resolution is required across temporal,
spatial, and sectoral dimensions. Conventional approaches rely on
temporal aggregation and spatial clustering that sacrifice accuracy for
tractability.

This paper introduces budget-based Benders decomposition algorithms that
extend decomposition to the sectoral and spatial domains. The key
innovation replaces hourly-resolved linking vectors with scalar budgets
that aggregate energy exchanges over subperiods. Tested on continental US
case studies with electricity and hydrogen sectors, the methods achieve
15-70% runtime reductions compared to state-of-the-art temporal
decomposition, with minimal accuracy loss after a two-stage correction
for storage capacity estimation.

## Core Contribution

Budget-based formulation for linking subproblems in Benders
decomposition:

Sectoral budget : Scalar aggregate of net energy exports from sector s
to sector s' over subperiod w, defined as sum of hourly exports.

Spatial budget : Scalar aggregate of inter-zonal transport flows for
zone z over subperiod w.

The budget variables are treated as complicating variables in the upper
problem, enabling decomposition into smaller subproblems per subperiod
and sector (or zone) while maintaining convergence properties.

## Key Results

Temporal + sectoral BD : 20-70% runtime reduction vs. temporal BD alone.
Iter count reduced through doubling cuts per iteration.

Temporal + spatial BD : 40-70% runtime reduction, 10x fewer iterations
than temporal BD (20 vs 310 iterations in 16-zone, 12-week case).

Accuracy : Objective function error 2-4% vs. monolithic formulation.
Individual technology capacities vary due to near-optimal solution
multiplicity.

Limitation : Budget-based linking underestimates storage requirements.
Addressed via two-stage algorithm: Stage 1 solves budget-based BD, Stage 2
warm-starts temporal BD with computed cuts and tight capacity bounds
to estimate storage.

## Implementation

Implemented in Dolphyn.jl, an open-source multi-sector capacity
expansion model using Julia 1.9.2 and JuMP 1.20.0. LP problems solved
with Gurobi 10 (barrier method, presolve enabled, crossover disabled).
Tests run on MIT SuperCloud with Intel Xeon Platinum 8260 processors.

Case studies : Continental US with 16 and 64 zones (EPA IPM spatial
configuration), 12-52 representative weeks via k-means clustering.
Sectors: electricity (PV, wind, nuclear, gas) and hydrogen (electrolysis,
SMR with/without CCS, storage).

## Extensions Discussed

Stochastic models : No formulation changes required; coupling across
scenarios is the primary addition.

Multi-period models : Myopic approach uses consecutive models; perfect-
foresight multiplies subproblems by planning periods.

Mixed-integer : Requires third stage to restore integrality constraints
after relaxed LP solution.

## Academic Review Summary

Core claim : Budget-based Benders decomposition achieves significant
runtime improvements for multi-sector CEMs without resolution sacrifice.

Stress test results : Budget-based linking validated for moderate sector
coupling; storage underestimation requires two-stage fix. Spatial
decomposition shows promise but distributed computing challenges remain.

Evidence quality : Strong empirical validation on US cases; weaker on
sector extensibility (only 2 sectors tested).

Verdict : Valid contribution with practical implementation. Future work
should test 3+ sectors and address spatial decomposition scaling.

## Related

- [[Benders Decomposition]] ([Benders Decomposition](benders-decomposition.md))
- [[Capacity Expansion Planning]] ([Capacity Expansion Planning](capacity-expansion-planning.md))
- [[Energy System Optimization]] ([Energy System Optimization](energy-system-optimization.md))
- [[Dolphyn Model]] ([Dolphyn Model](dolphyn-model.md))
- [[Temporal Aggregation]] ([Temporal Aggregation](temporal-optimization.md))

## Backlinks
