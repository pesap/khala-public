---
title: Attribute-Preserving Optimal Network Reductions
created: 2026-03-12T12:04:06.207391
source: https://www.energy.gov/sites/prod/files/2015/09/f26/16-RM2015-Tylavsky.pdf
visibility: public
semantic_cluster: concepts
tags:
  [
    "power-systems",
    "network-reduction",
    "optimization",
    "ward-reduction",
    "holomorphic-series-method",
    "power-flow",
    "voltage-stability",
  ]
---

# Attribute-Preserving Optimal Network Reductions

Research presentation by Dan Tylavsky, Yujia Zhu, Shruti Rao (Arizona State
University) with William Schulze, Ray Zimmerman, Dick Shuler, Jubo Yan (Cornell
University), Biao Mao (Rensselaer Polytechnic University), and Dan Shawhan
(Resources for the Future). CERTS R&M Cornell, August 2015.

## Context and Objectives

### Research Goal

Develop reduced network equivalencing procedures that preserve specific
attributes of electric power networks. Traditional network reductions only
preserve certain structures but become inaccurate when operating conditions
change.

### Traditional Network Reduction Methods

#### Ward Reduction

- Preserves nodal voltages and branch flows for base case only under linearity
  assumption

#### Improved Ward (PV-Ward or Extended Ward)

- Better performance on matching reactive support

#### REI (Radial Equivalent Independent)

- Better reactive support modeling
- Hot start method preserving base case power flow solutions
- Inaccurate when operating conditions change

### Targeted Network Reduction Benefits

- More accurate simulations of electric power networks
- Applications: E4ST, dynamic simulations, transmission expansion planning

## Scope of Research

### Developing Attribute-Preserving Network Equivalents

- Topology preservation
- Branch values optimization
- Generator placement
- Load models

### Reduced DC Equivalents Preserving Branch Flow Values

- Finding optimal branch reactances for AC-to-DC model conversion
- Bus aggregation techniques
- Ward-type reduction optimization
- Generalized optimization formulation

## Key Research Areas

### 1. OP-Ward Reduction (Optimization-based Ward Reduction)

Minimize branch flow errors in the retained model portion through unconstrained
optimization.

#### Objective Function

```math
\min \| \Lambda_1 y - b \|_2
```

Where:

- $\Lambda_1$ is constructed from PTDF (Power Transfer Distribution Factor)
  matrices
- $y$ represents reactance variables
- $b$ represents branch susceptance matrix columns

#### Rank Deficiency Problem

The $\Lambda_1$ matrix can be rank deficient in certain network configurations
(e.g., star-mesh conversions). Solution: add pseudo-branches to make $\Lambda_1$
full rank, then remove them from the reduced model.

Test results: all test cases (9-bus, IEEE 118-bus variants) yielded negligible
errors ($< 10^{-12}$%) after applying the pseudo-branch technique.

### 2. Generator Placement Methods

Three methods tested on ERCOT, WECC, and EI (Eastern Interconnection):

#### Shortest Electrical Distance (SED)

- Places external generators at retained generator bus closest in electrical
  distance

#### Optimization-based Generator Placement (OGP)

- Mixed integer linear programming minimizing generation cost
- Retains congestion status

#### Minimum Shift Factor Change (Min-SF)

- Places external generators at bus with most similar shift factor
- Found to be most robust and accurate

Results: Min-SF and SED methods yielded similar results. Systems cannot be
reduced indefinitely without accuracy consequences.

### 3. Network Reduction Toolbox

#### Major Updates

- Rewrote partial LU factorization algorithm for reduced model construction
  during factorization
- Improved symbolic processing of sparsity patterns

#### Performance Improvements

- ERCOT (6000→424 buses): 3.5 min → 25 sec
- WECC (17000→2000 buses): 3 min → 20 sec
- WECC (19000→300 buses): 4.2 hours → 2.4 min
- EI (62000→5222 buses): Out of Memory → 1.3 hours

Distribution: available with MATPOWER 5.1 and on E4ST website (http://e4st.com/)

### 4. Transmission Expansion Corridors

Three candidate transmission projects identified:

#### Champlain-Hudson Power Express

- 1000 MW HVDC line
- Quebec (Hertel substation) to New York City

#### Southern California - Arizona (DPV2)

- 500 kV AC transmission line (Devers-Palo Verde No. 2)
- California portion completed; Arizona portion denied by ACC in 2007

#### Manitoba - Minnesota (Great Northern Transmission Line)

- 500 kV AC line
- Certificate of Need issued June 2015
- Delivers hydro power from Manitoba, wind power from Minnesota

### 5. Inverse Function Network Reduction / Holomorphic Series Method (HSM)

Traditional methods linearize nonlinear (PQ) loads at external buses, then
convert back to equivalent nonlinear loads at base case. This does not handle
nonlinear loads accurately.

The solution uses HSM to obtain voltages as functions of current and complex
power injections (inverse function approach).

#### Power Balance Equation Embedding

```math
\frac{\alpha S_i^*}{V_i^*(\alpha)} = \sum_k Y_{ik} V_k(\alpha)
```

Where $\alpha$ scales complex load $S$. Voltage is represented as a Maclaurin
series:

```math
V(\alpha) = V^{[0]} + V^{[1]}\alpha + V^{[2]}\alpha^2 + \cdots + V^{[N_t]}\alpha^{N_t}
```

Padé approximants are used to represent the voltage series as rational
approximants for convergence beyond the series radius. Stahl's theory:
near-diagonal Padé approximants converge for analytic functions with finite
singularities.

The Voltage Collapse Point (VCP) is estimated as the smallest real zero of Padé
approximant numerator/denominator polynomials.

#### Results on 3-bus system

- Unreduced network VCP: $7.63\times$ base load
- Inverse function approach: $7.61\times$ base load
- Ward reduction: $7.17\times$ base load

The inverse function approach significantly outperforms traditional Ward
reduction for voltage stability analysis.

## Technical Details

### Linear Case Mathematics

```math
Ax = b \;\Rightarrow\; (I + D)x = b \;\Rightarrow\; x = -Dx + b
```

Holomorphically embed with parameter $\alpha$:

```math
x(\alpha) = -\alpha D x(\alpha) + b
```

Represent as a power series and equate powers of $\alpha$ to solve recursively.

### Nonlinear AC Systems

For PQ buses:

```math
\sum_k Y_{ik} V_k^{[0]} = 0 \quad \text{(germ at } \alpha = 0\text{)}
```

```math
\sum_k Y_{ik} V_k^{[n]} = S_i^* W_i^{*[n-1]} \quad \text{(recurrence)}
```

For PV buses: similar formulation with voltage magnitude constraints.

## Key Insights

1. Pseudo-branches solve rank deficiency: adding strategic pseudo-branches
   enables full-rank optimization matrices without significantly impacting
   results.

2. Generator placement matters: Min-SF and SED methods perform similarly; both
   are superior to purely cost-based optimization for preserving system
   behavior.

3. Reduction limits exist: aggressive reductions (to ~10% of original size) show
   significant accuracy degradation in LMP and energy cost calculations.

4. Voltage preservation requires nonlinear methods: traditional Ward-type
   reductions fail for voltage stability analysis; HSM-based inverse function
   equivalents preserve voltage behavior accurately.

5. Computational efficiency gains: the optimized toolbox reduces computation
   time by orders of magnitude while enabling previously infeasible large-scale
   reductions.

## Applications

- Power flow analysis for large interconnections (ERCOT, WECC, EI)
- Transmission expansion planning (E4ST tool)
- Voltage stability studies
- Locational Marginal Price (LMP) analysis
- Dynamic simulations

## Related

- [[Ward Reduction]] ([Ward Reduction](ward-reduction.md))
- [[REI Reduction Method]] ([REI Reduction Method](rei-reduction-method.md))
- [[Power Transfer Distribution Factor]]
  ([Power Transfer Distribution Factor](power-transfer-distribution-factor.md))
- [[Padé Approximants]] ([Padé Approximants](pade-approximants.md))
- [[Voltage Collapse Analysis]]
  ([Voltage Collapse Analysis](voltage-collapse-analysis.md))
- [[MATPOWER]] ([MATPOWER](matpower.md))
- [[E4ST Model]] ([E4ST Model](e4st-model.md))

## Backlinks
