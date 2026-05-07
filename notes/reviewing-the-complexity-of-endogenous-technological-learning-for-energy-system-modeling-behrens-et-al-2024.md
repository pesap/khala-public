---
title:
  Reviewing the Complexity of Endogenous Technological Learning for Energy
  System Modeling (Behrens et al. 2024)
created: 2026-03-16
source: https://www.sciencedirect.com/science/article/pii/S2666792424000301
visibility: public
semantic_cluster: energy-system-modeling
tags:
  [
    "energy-system-modeling",
    "technological-learning",
    "experience-curve",
    "nonconvex-optimization",
    "piecewise-linear",
    "complexity-reduction",
    "renewable-energy",
    "energy-transition",
    "review",
  ]
---

# Reviewing the Complexity of Endogenous Technological Learning for Energy System Modeling (Behrens et al. 2024)

Review article in Advances in Applied Energy, Volume 16, December 2024, 100192.
Open Access (CC-BY 4.0).

Authors: Johannes Behrens, Elisabeth Zeyen, Maximilian Hoffmann, Detlef Stolten,
Jann M. Weinand. Affiliations: Forschungszentrum Jülich (Behrens, Hoffmann,
Stolten, Weinand); RWTH Aachen University (Behrens, Stolten); Technical
University of Denmark (Zeyen). DOI: 10.1016/j.adapen.2024.100192

## Overview

Renewable energy technologies and electrolyzers exhibit declining investment
costs as cumulative production grows, a phenomenon captured by experience curves
(also called learning curves). Energy system models that ignore this dynamic
risk locking in suboptimal technology mixes. This paper systematically reviews
how model-endogenous technological learning (ETL) has been implemented in the
literature and catalogues the methods used to manage the resulting computational
complexity.

The core problem: cost-vs-capacity relationships described by experience curves
are nonlinear and nonconvex, turning otherwise tractable linear or mixed-integer
programs into nonconvex optimization problems. Handling these requires
approximations or exact reformulations that trade accuracy against computational
cost.

## Key Concepts

Experience curve : Empirical relationship between investment cost and cumulative
installed capacity (or production volume). Typically expressed as a power-law:
cost decreases by a fixed percentage for each doubling of cumulative capacity.

Learning rate : The percentage cost reduction for each doubling of cumulative
capacity. A 20% learning rate means costs fall by 20% every time capacity
doubles.

Endogenous technological learning (ETL) : Learning is determined inside the
model as an outcome of capacity deployment decisions, rather than specified
exogenously as an assumed cost trajectory.

Piecewise linear approximation : The nonconvex experience curve is approximated
by a sequence of linear segments, converting the nonconvex problem into a
mixed-integer linear program (MILP). The number of segments controls accuracy
vs. problem size.

## Problem Structure

The nonconvex investment cost function introduces several difficulties:

- Non-convexity means standard LP relaxations are loose, making branch-and-bound
  expensive.
- Experience curves couple decisions across time periods: early deployment
  reduces costs for later periods, creating intertemporal interdependencies.
- Sector integration, fine spatial resolution, and detailed temporal resolution
  all add variables and constraints that compound the difficulty.

Iterative solution methods (e.g., alternating fixed-point approaches) generally
converge to local optima that favor suboptimal technology mixes. Exact global
solutions are computationally demanding but necessary for reliable policy
conclusions.

## Methods for Complexity Reduction

The paper surveys several classes of methods for managing model complexity when
ETL is included:

Temporal aggregation : Reducing the number of representative time periods
(hours, days, seasons) to shrink model size, at the cost of temporal resolution
in investment and dispatch decisions.

Spatial aggregation : Clustering regions or nodes to reduce the size of the
network, trading spatial detail for tractability.

Decomposition methods : Separating the problem into subproblems (e.g.,
investment planning vs. dispatch) solved iteratively, allowing larger systems to
be handled in parts.

Technology clustering : Grouping similar technologies to reduce the number of
distinct experience curves and associated binary variables.

Each method involves accuracy-tractability tradeoffs, and the paper argues these
should be considered jointly rather than applied in isolation.

## Gaps and Recommendations

Current practice tends to omit sector coupling (e.g., power, heat, transport,
hydrogen) or to use coarse spatial and temporal resolutions when ETL is
included, because fine-grained models become intractable. The paper identifies
this as a significant gap: the same model features that make ETL impactful are
those most often dropped to maintain solvability.

The authors propose a more integrated approach to complexity management that
preserves model feasibility while retaining important system structure, and call
for future research into:

- Better exact solution methods for nonconvex ETL problems at scale.
- Systematic benchmarks comparing approximation quality across methods.
- Integration of ETL with sector-coupled, high-resolution energy system models.

## Related

- [[Energy System Modeling]]
  ([Energy System Modeling](energy-system-modeling.md))
- [[Experience Curve]] ([Experience Curve](experience-curve.md))
- [[Piecewise Linear Optimization]]
  ([Piecewise Linear Optimization](piecewise-linear-optimization.md))
- [[Nonconvex Optimization]]
  ([Nonconvex Optimization](nonconvex-optimization.md))

## Backlinks
