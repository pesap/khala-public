---
title: Multi-sector demand response for cost optimal energy transitions
created: 2026-05-11
source: https://doi.org/10.1371/journal.pclm.0000918
visibility: public
semantic_cluster: energy-systems
tags:
  ["demand-response",
   "energy-planning",
   "pypsa",
   "capacity-expansion",
   "multi-sector",
   "thermal-dr",
   "electricity",
  ]
---

## Overview

PLOS Climate, May 2026. Barnes, Tehranchi, Reinholz, Metcalfe, Niet.

This study investigates demand response (DR) across multiple energy sectors
(electricity and thermal) in capacity expansion planning. Using PyPSA-USA, the
authors model California and New England 2030 scenarios to compare electrical
versus thermal DR contributions to system cost optimization.

The core insight is that shifting heating and cooling loads (thermal DR) can
provide greater cost savings than shifting electricity use alone, particularly
in capacity-constrained cold climate systems. The authors test two pricing
strategies: carrier-average (same price for all energy types) and carrier-specific
(different prices for electricity vs. heat).

What they tested : Two pricing strategies for demand response in multi-sector
energy systems, applied to California and New England 2030 scenarios with varying
DR adoption levels and natural gas prices.

What they found : Both electrical and thermal DR reduce costs in capacity
constrained systems. Thermal DR significantly reduces heat pump capacity needs
(up to 90% in New England). Pricing energy carriers separately outperforms
uniform pricing. Low DR adoption (<20%) unlocks substantial savings.

The surprising thing : Electrical DR provided no cost savings in unconstrained
California scenarios, contradicting established literature. Only when imports and
existing gas capacity were artificially removed did electrical DR show value.
In New England, thermal DR alone captured maximum savings with electrical DR
adding minimal incremental benefit.

Why it matters : As heating electrifies and cold-climate regions face winter
peaking challenges, thermal DR offers a low-participation pathway to significant
infrastructure cost reduction. The finding challenges assumptions that
electrical load shifting is the primary DR value stream.

The analogy : Think of highway congestion. Instead of building more lanes
(expensive new capacity), demand response spreads traffic across the day. The
paper finds that shifting commercial delivery trucks (thermal loads) is often
more valuable than shifting passenger cars (electrical loads), and you only
need 20% of drivers to change behavior to eliminate the worst jams.

## Core Contribution

Technical contribution : A computationally tractable price-based demand response
implementation for multi-sector energy planning at hourly resolution, using
marginal cost shadow prices from the energy balance constraints rather than
inter-temporal connectivity constraints.

The authors implement DR as a virtual storage resource with carrier-specific
pricing derived from annual average marginal costs. This avoids state-of-the-art
incentive-based DR formulations that introduce inter-temporal constraints and
computational complexity.

Two novel contributions include: (1) direct end-use load shifting rather than
technology-level dispatch, enabling fuel-switching during demand response
events, and (2) net-load characteristic metrics (peakiness, routine ramping,
extreme ramping) applied to capacity expansion studies.

## Key Results

System costs : Up to 40% cost reduction in some New England scenarios with low
DR participation. Carrier-specific pricing consistently outperforms
carrier-average pricing. Cost savings diminish as natural gas prices increase.

California versus New England : Electrical DR provided no benefit in standard
California (existing flexibility from imports and OCGT capacity out-competed
it). In capacity-constrained California (imports removed, OCGT removed),
electrical DR reduced costs up to 14%. New England naturally constrained systems
showed thermal DR as the primary cost reducer with electrical DR adding
minimal value.

Thermal capacity : New England heat pump capacity reduced 90%+ in some scenarios
due to thermal DR enabling adaptation to variable air-source heat pump COP
rather than overbuilding ground-source heat pumps constrained by urban land use.

Emissions : Inconclusive. California showed mild emission reductions (<4%).
New England showed emission increases up to 10% in some scenarios due to
increased fossil furnace operation displacing heat pump electricity use.

Sensitivity : Significant cost savings achievable with only 20% DR load
contribution. Marginal benefits decrease as participation increases beyond this
level.

Battery substitution : DR can substitute for physical battery capacity, with
electrical DR reaching saturation points where batteries are fully displaced.
Thermal DR never reaches full substitution due to inability to shift
non-thermal electrical loads like EV charging.

## Implementation

Model : PyPSA-USA v0.8.0, hourly resolution capacity expansion and economic
dispatch for 2030 planning year.

Regions : California (4 load zones, 80 renewable zones) and New England (6 load
zones, 120 renewable zones).

DR formulation : Price-based program modeling DR as a store with hourly deferral
costs ($/MWh/hr) representing willingness-to-pay. Annual average marginal costs
from no-DR baseline runs set the DR pricing levels.

Constraints : Transmission and gas pipeline capacity frozen at current levels.
Annual import/export volumes capped at current levels. Supply investments
allowed for solar, wind (onshore/offshore), OCGT, CCGT with EIA AEO 2030 build
rate limits. No oil furnace expansion allowed.

Scenarios : 39 scenario names per pricing strategy (carrier-average and
carrier-specific) across DR sector dimension (none, electrical only, thermal
only, both), DR cost dimension (very low, low, medium, high), and natural gas
cost dimension (low, medium, high). Total 156 runs (78 per region).

Data sources : NREL ResStock/ComStock for residential/commercial loads, EIA MECS
and EPRI load shapes for industrial, NREL Electrification Futures Study for
transportation.

## Academic Review Summary

Core claim : Multi-sector demand response with carrier-specific pricing provides
cost-optimal energy transition pathways, with thermal DR offering particularly
high value in capacity-constrained cold climate systems.

Methodological gaps : The implementation lacks load recovery constraints,
conflating load shedding with true demand response. Perfect foresight
eliminates operational flexibility needs. Missing unit commitment constraints
prevent capture of operational value streams.

Unsupported claims : The <20% DR adoption claim is only demonstrated under
unrealistically low DR cost scenarios. The 90%+ heat pump capacity reduction is
driven by artificial GSHP land-use constraints rather than pure DR benefits.

Missing evidence : No empirical validation against historical DR program data.
No thermal comfort impact analysis despite aggressive pre/post heating claims.
No formal uncertainty quantification for technology costs or load forecasts.

Literature conflicts : The finding that electrical DR offers no cost savings in
unconstrained systems contradicts extensive established literature attributing
cost benefits to electrical load shifting. This is resolved only by noting
the artificial constraints imposed in the study design.

Verdict : Revise and resubmit. The paper offers useful methodological
contributions but key claims require tempering to reflect modeling limitations.
The load recovery constraint omission is particularly concerning as it
fundamentally mischaracterizes the physical behavior being modeled.

## Related

- [[LMP Fundamentals]] ([LMP Fundamentals](litvinov-power-system-lmp-fundamentals-2008.md))
- [[Endogenous Technological Learning]] ([Endogenous Technological Learning](reviewing-the-complexity-of-endogenous-technological-learning-for-energy-system-modeling-behrens-et-al-2024.md))

## Backlinks
