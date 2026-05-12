---
title: Britto et al. (2026) on building power grid models from OpenStreetMap
created: 2026-05-12
source: https://arxiv.org/abs/2605.04289
visibility: public
semantic_cluster: power-systems
tags:
  [
    "power-grid",
    "openstreetmap",
    "optimal-power-flow",
    "microsoft-research",
    "open-data",
    "transmission-networks",
  ]
---

## Overview

Britto, Spina, Yang, Fowers, Zhang, and White (Microsoft Research and University of Washington) 
present a five-stage pipeline that transforms OpenStreetMap data into solver-ready Optimal 
Power Flow (OPF) models. The paper addresses a critical data accessibility problem: real 
transmission grid data in the US is classified as Critical Energy Infrastructure Information 
(CEII), making it inaccessible to most researchers.

The pipeline extracts power infrastructure from OpenStreetMap, reconstructs bus-branch 
topology through voltage inference and line merging, estimates electrical parameters using 
voltage-class lookup tables, allocates hourly demand using Census population as a spatial 
proxy, and solves DC/AC OPF using PowerModels.jl with progressive relaxation.

The models were validated across all 48 contiguous US states and six multi-state regions 
including the full Western (5,076 buses) and Eastern (21,697 buses) Interconnections. 42 of 
48 state models (88%) converged at strictest relaxation for AC-OPF at peak hour. Median 
dispatch cost was $22/MWh and median system losses 1.0%, consistent with real wholesale 
market outcomes. All 54 models are publicly released at https://github.com/microsoft/GridSFM.

## Core Contribution

Open data pipeline for transmission network modeling : A complete workflow from raw 
geographic data to OPF-solvable models without proprietary utility data.

Progressive relaxation strategy : Automatic constraint loosening that enables convergence 
on imprecise models while quantifying model quality through relaxation level needed.

Scale validation : First open-data pipeline validated at full interconnection scale 
(Western and Eastern Interconnections).

## Key Results

State model convergence : 42 of 48 states (88%) solved AC-OPF at strictest relaxation 
level during peak demand; 44 (92%) off-peak.

Regional model success : Full Western Interconnection (5,076 buses) and Eastern 
Interconnection (21,697 buses) models both converged.

Realistic dispatch costs : Median $22/MWh, consistent with US wholesale market prices.

Realistic losses : Median 1.0% system losses, reasonable for transmission-level models.

All models public : 48 single-state and 6 multi-state models released as 
PowerModels-compatible JSON.

## Implementation

Stage 1 - Data extraction : Downloads power infrastructure from local Overpass API 
instance using OpenStreetMap data.

Stage 2 - Topology reconstruction : Voltage inference, line merging, circuit 
classification, and transformer detection to build clean bus-branch topology.

Stage 3 - Parameter estimation : Uses voltage-class lookup tables calibrated with EIA 
plant-level data to assign impedances, ratings, and generator characteristics.

Stage 4 - Demand allocation : Distributes EIA-930 hourly demand to buses using US Census 
population as spatial proxy.

Stage 5 - OPF solving : PowerModels.jl with progressive relaxation strategy that 
automatically loosens constraints until model converges.

## Academic Review Summary

Core claim : OSM plus public EIA/Census data can produce realistic, OPF-solvable US 
transmission models at state and interconnection scale.

Methodological gaps :

- Ground-truth validation is weak. Convergence and plausible costs do not prove topology 
  or flows match reality. Missing comparison against known aggregate flow patterns, 
  congestion zones, or public planning cases.

- Parameter uncertainty is under-characterized. Line impedances, ratings, and transformer 
  parameters are mostly inferred from lookup tables without sensitivity analysis showing 
  how OPF results change under plausible parameter error.

- Demand allocation is crude. Census population is a weak proxy for transmission-level 
  load, missing industrial loads, data centers, and urban/commercial peaks that can 
  materially distort congestion and dispatch.

Unsupported claims :

- Structurally and electrically plausible. Plausibility asserted from OPF convergence and 
  median metrics, but many wrong networks can converge with plausible system totals.

- Reproduce system-level statistics within realistic ranges. Limited benchmarking against 
  actual regional market outcomes, fuel mix, emissions, or congestion behavior.

Verdict : Revise. Promising and useful open-data pipeline, but needs stronger validation 
and uncertainty analysis before models can be treated as credible research benchmarks 
rather than OPF-feasible synthetic approximations.

## Simplified Explanation

The power grid is like a giant road system for electricity. Power plants are factories, 
lines are roads, substations are intersections. Researchers want to study this system but 
the official maps are locked away as sensitive infrastructure.

This paper asks: can we build a useful practice map using only public information? The 
answer is yes. They download public map data, clean it up, estimate missing electrical 
properties, spread demand across the map using population data, then run optimization to 
find the cheapest way to run generators while meeting demand.

It is like building a playable city traffic simulator from Google Maps, census data, and 
guesses about road speed limits. You may not know every detail, but you can still study 
likely traffic patterns and bottlenecks.

These models are good for broad research and experiments, not for operating the real 
grid. Do not use them to say "this exact line will overload tomorrow." Use them to ask 
"what kinds of grid behavior might happen under these conditions?"

## Related

- [[Power Systems Modeling]] ([Power Systems Modeling](power-systems-modeling.md))
- [[Optimal Power Flow]] ([Optimal Power Flow](optimal-power-flow.md))
- [[OpenStreetMap Data Quality]] ([OpenStreetMap Data Quality](openstreetmap-data-quality.md))
- [[Grid Data Availability]] ([Grid Data Availability](grid-data-availability.md))

## Backlinks

