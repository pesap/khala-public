---
title: Power System and LMP Fundamentals (Litvinov 2008)
created: 2026-03-12
visibility: public
semantic_cluster: sources
tags:
  [
    electricity-markets,
    lmp,
    locational-marginal-pricing,
    power-systems,
    iso-new-england,
    economic-dispatch,
    contingency-analysis,
  ]
source: https://faculty.sites.iastate.edu/tesfatsi/archive/econ458/tesfatsion/lmp.AdvancedWPM.ELitvinovWEM301.pdf
---

# Power System and LMP Fundamentals (Litvinov 2008)

Technical presentation (186 pages) by Eugene Litvinov, Director of Business
Architecture and Technology Department at ISO New England. Presented as WEM 301
(Wholesale Electricity Markets) at Iowa State University, 2008.

## Overview

This comprehensive presentation covers the technical foundations of Locational
Marginal Pricing (LMP) as implemented by ISO New England, including power system
modeling, contingency analysis, sensitivity calculations, economic dispatch
formulation, and market system architecture.

## Electrical Network Fundamentals

### Network Model Components

Device : Any electrical device (line, transformer, breaker, etc.)

Node : Connection point of two or more devices in one-line model

Bus : Connection point of two or more branches in the network model

Branch : Physical or equivalent line connecting buses

Injection : Power flow into bus (generation), negative value

Withdrawal : Power flow from bus (load), positive value

Interface : Set of branches that, when opened, split network into two separate
islands

External Interface : Interface between two control areas (e.g., NE and NY),
containing only inter-ties

### Power System Physics

Ohm's Law : $I = U / R$ (Current equals Voltage divided by Resistance)

Power : $P = U \times I$ (Power equals Voltage times Current)

Losses : Lines have resistance causing heat loss proportional to current
squared: $Losses = I^2 \times R$

Kirchhoff's Laws : Current law states sum of currents at any node equals zero.
Voltage law states sum of voltage drops around any closed loop equals zero.

### Reference Bus (Slack Bus)

The reference bus is essential for power flow calculations:

- Makes up for system losses that cannot be predicted
- Balances generation and load in the system
- In AC systems, the reference bus injects additional MWs to compensate for
  losses
- PTDFs and shift factors are dependent on reference bus location in AC models
  (but not in DC models)
- By definition, loss factor at reference bus equals zero: $LF_{ref} = 0$
- All shift factors at reference bus equal zero: $S_{ref,k} = 0$

## Contingency Analysis

### Purpose

Determine conditions violating operating limits:

- Branch overloads
- Abnormal voltages
- Interface limits
- Voltage angle differences

### Process

Performed both in real-time (using state estimator) and study mode:

1. Calculate base power flow
2. Check all limiting elements for violations
3. Screen all contingencies using DC model-based quick power flow
4. Check each for potential violations
5. Run suspicious contingencies through full AC power flow
6. Report violations in base case and under contingencies

### Each Contingency

Described by the set of outaged components, simulating equipment failures to
ensure system reliability.

## Sensitivities

### Power Transfer Distribution Factors (PTDF)

Definition : PTDF determines the change in power flow on each line when 1 MW is
transferred from one bus to another.

Key Properties : When 1 MW is transferred between two buses, it affects every
single flow in the network. PTDFs are reference-bus dependent in AC models due
to loss compensation. PTDFs are not reference-bus dependent in DC models (no
losses in DC networks).

Formula : $PTDF = \frac{\Delta P_{mn}}{\Delta \pi_{ij}}$ (change in line flow
divided by change in transfer)

### Shift Factors (SF)

Definition : PTDFs when one point is always the reference bus. SF shows how flow
in a branch changes if injection at a bus changes by 1 MW.

Key Properties : SF values are dependent on reference bus location. The
reference bus always makes up for injection changes to maintain system balance.
This is a fundamental security analysis tool for answering: how will solution
change for variations in inputs, and how must inputs change to control outputs?

### Loss Factors (LF)

Definition : Sensitivity of system losses to change in injection at a location.

Delivery Factor : $DF_i = 1 - LF_i$

Key Properties : There are as many loss factors as locations in the network.
Values depend on reference bus location because slack bus balances injection
increments. Loss factor at reference bus is always zero (no change in power flow
if balanced at same bus). Used in linear analysis to estimate effect of
transfers on system losses.

Marginal vs. Average Losses : Marginal losses are about twice as much as average
losses. Marginal describes the effect of increasing transmission loading.
Average describes losses per MW of flow. Both are dependent on system state
(flow in lines).

## Economic Dispatch and LMP Calculation

### Economic Dispatch (ED)

Definition : Least expensive way of supplying load in the system.

ISO-NE Implementation : Runs every 5 minutes to re-optimize generation. Produces
unit output levels (Desired Dispatch Points, DDP) in MW. Produces LMPs at each
generator node (nodal dispatch rates).

Mathematical Formulation

Objective function (minimize total cost): $$\min \sum_{i=1}^{N} C_i \cdot Pg_i$$

Subject to:

- System balance constraint (equality): Total generation equals Total load plus
  Losses
- Transmission constraints (inequalities): Branch/interface flow limits

Linear Programming Approach : General OPF (Optimal Power Flow) is non-linear but
not robust or quick enough for real-time. ISO-NE uses linearized version with
Linear Programming (LP) technique. Constraints must be linear to use LP.

### Shadow Prices (Dual Variables)

System Balance Shadow Price ($\lambda$) : One value for entire system. Never
zero (system balance always binds). Represents the marginal cost of supplying
load.

Transmission Constraint Shadow Prices ($\mu_k$) : Each transmission constraint k
has its own shadow price. Binding constraints have non-zero shadow price.
Non-binding constraints have shadow price equal to zero. Represents change in
total cost if constraint relaxed by 1 unit.

Binding Constraint : Constraint that becomes equality at optimal solution (for
example, a branch at its limit).

### LMP Fundamental Properties

n+1 Rule : For n binding constraints, there are at least n+1 marginal units.
This does not include the equality constraint. With no congestion, only one
marginal unit exists.

Marginal Units : Price at each marginal unit's location always equals its offer
price. Any load increment at any location is delivered from marginal units. LMP
at any location is a linear combination of LMPs (offer prices) at marginal
locations.

Key LMP Behaviors : Without congestion ($\mu_k = 0$) and without losses, the LMP
is same at all locations. LMPs can exceed the highest offer price (due to
congestion and losses). Opening a branch can lower LMPs. LMP can be negative at
some locations.

### LMP Decomposition (Three Components)

Each LMP can be split into three components:

$$\lambda_i = \lambda - LF_i \cdot \lambda + \sum_{k=1}^{K} SF_{ik} \cdot \mu_k$$

Or equivalently:

$$\lambda_i = \lambda(1 - LF_i) + \sum_{k=1}^{K} SF_{ik} \cdot \mu_k$$

Where:

Energy Component ($\lambda$) : System balance shadow price, same for all
locations.

Loss Component ($-LF_i \cdot \lambda$) : Marginal cost of additional losses from
supplying load at location i.

Congestion Component ($\sum SF_{ik} \cdot \mu_k$) : Cost of transmission
constraints, zero when no binding constraints.

Alternative Grouping : Group energy and loss components together as one
component called delivered energy component. This is the marginal price of
delivering an increment of load from the reference bus. In fact, the settlement
process never needs energy and loss components separately.

Key Properties of Components : All three components depend on reference bus
selection. Individual component values do not have independent meaning; only
differences matter. Differences between locations are not dependent on reference
bus selection. LMP itself does not change when moving reference bus (total stays
constant). At reference bus: Loss component equals 0, Congestion component
equals 0, Price equals Energy component.

Why Components Matter : Needed for Financial Transmission Rights (FTRs).
Required to split congestion cost from energy for settlements. Settlement
process never needs energy and loss components separately (only delivered energy
component matters).

### Marginal Loss Pricing (MLP)

Purpose : Account for marginal cost of losses in LMP calculation.

Penalty Factors : Used to modify generator offers by their bus penalty factor:
$C'_i = PF_i \times C_i$

Where penalty factor $PF_i = \frac{1}{1 - LF_i}$

Example : Generator 1 offer is $20/MWh with penalty factor 1.2, giving effective
offer of $24/MWh. Generator 2 offer is $30/MWh with penalty factor 1.0. The
optimal solution delivers all load from Generator 1 (lower effective cost),
setting the Energy Component Price (ECP) to $24/MWh at all locations.

## ISO New England Market Systems

### System Architecture Components

Day-Ahead Market : Used to produce LMPs for next-day scheduling. Units submit
offers specifying incremental cost of producing energy.

Real-Time Market : SCED (Security Constrained Economic Dispatch) runs every 5
minutes. State Estimator provides real-time network conditions. Contingency
Analysis ensures reliability. Produces real-time LMPs and dispatch points.

Data Flows : Real-time data from operations. Day-ahead data for scheduling.
Supply offers and demand bids. Dispatch data and supply offers. Invoice and
billing data.

Market Information : Internal and external web servers. FTP servers for data
exchange. General Ledger and Market User Interface (MUI).

### Consistency Checks

During finalization process:

- Verify all marginal resources have LMP equal to their offer price
- If LMP outside tolerance, errors are reported and corrections applied
- Ensures dispatch selected by operators is close to optimal
- Prevents inconsistent prices

### Multi-Regional Coordination

Challenge : Different markets may not account for neighboring market
constraints, producing inconsistent prices across borders.

## Key Insights

1. Reference bus arbitrariness. While LMPs do not depend on reference bus
   location, the decomposition into components does. Only location-to-location
   differences have physical meaning.

2. Marginal units drive prices. All load increments are served by marginal
   units, making their offer prices the foundation of all LMPs.

3. Linearization trade-offs. ISO-NE uses linearized DC models for real-time
   speed, accepting some accuracy trade-offs for computational feasibility.

4. Components vs. totals. Settlement uses total LMPs, but FTR markets require
   understanding congestion components.

5. Contingency screening. DC model screening identifies suspicious contingencies
   for full AC analysis, balancing speed and accuracy.

6. Real-time optimization. 5-minute dispatch re-optimization keeps system at
   minimum cost while respecting reliability constraints.

## Context

This material was presented as part of WEM 301 (Wholesale Electricity Markets)
at Iowa State University. It reflects ISO New England's implementation circa
2008, providing practical insight into how LMP markets operate technically,
including the trade-offs between model accuracy and computational speed required
for real-time operations.

## Related

- [[Locational Marginal Pricing]]
  ([Locational Marginal Pricing](locational-marginal-pricing.md))
- [[Economic Dispatch]] ([Economic Dispatch](economic-dispatch.md))
- [[Power Transfer Distribution Factor]]
  ([Power Transfer Distribution Factor](power-transfer-distribution-factor.md))
- [[Shift Factors]] ([Shift Factors](shift-factors.md))
- [[Contingency Analysis]] ([Contingency Analysis](contingency-analysis.md))
- [[Marginal Loss Pricing]] ([Marginal Loss Pricing](marginal-loss-pricing.md))
- [[ISO New England]] ([ISO New England](iso-new-england.md))
- [[Financial Transmission Rights]]
  ([Financial Transmission Rights](financial-transmission-rights.md))
- [[Attribute-Preserving Optimal Network Reductions]]
  ([Attribute-Preserving Optimal Network Reductions](attribute-preserving-optimal-network-reductions.md))

## Backlinks
