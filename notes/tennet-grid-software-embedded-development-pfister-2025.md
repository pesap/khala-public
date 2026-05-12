---
title: The Grid Does not Wait for a Requirements Document - TenneT Embedded Development Model
created: 2025-05-07
source: https://lfenergy.org/the-grid-doesnt-wait-for-a-requirements-document/
visibility: public
semantic_cluster: software-engineering
tags:
  [
    "power-systems",
    "embedded-development",
    "sticky-information",
    "powsybl",
    "lf-energy",
    "open-source",
    "tennet",
    "grid-operations",
    "domain-expertise",
  ]
---

# The Grid Does not Wait for a Requirements Document

Blog article by Hugo Pfister, Manager Grid Security Applications at TenneT
Netherlands. Published on LF Energy, May 2025.

## Overview

Traditional power system operators separate grid operations from software
development, treating IT as a support function. TenneT challenges this model
by embedding software developers directly within grid security operations. The
result is a tenfold improvement in analysis performance and faster iteration on
tools that match operational reality.

The article argues that power systems contain sticky information, knowledge so
bound to operational context that it cannot be transferred without loss. When
domain experts and developers are separated by organizational boundaries,
requirements documents fail to capture tacit knowledge. The solution is not
better requirements but dissolving the boundary entirely.

## Core Argument

Sticky information in power systems:
Knowledge that lives in physics intuition, operational constraints learned
through experience, and the ability to distinguish simulation artifacts from
real anomalies. Only those inside operations possess this knowledge reliably.

Organizational latency costs:
When operational insights must pass through requirements documents to distant
software teams, iteration slows and tools calcify around outdated specifications.

Embedded development model:
Developers work as part of the operations team, not for them. Questions and
answers happen in the same conversation. The person who spots an anomaly and
the person who can fix it are often the same.

Central IT as platform:
IT provides infrastructure, security, CI/CD pipelines, and standards. The role
is enabling autonomy through reliable plumbing, not controlling tool choices.

Shared open source foundations:
PowSyBl provides simulation capabilities shared across European TSOs. Building
on shared foundations redirects engineering effort toward differentiating work.

## Key Results

Performance improvement : Tenfold speedup in grid security analysis after
embedding developers and migrating to PowSyBl.

Iteration speed : Operational questions and engineering answers in the same
room, same conversation. Latency between insight and codification eliminated.

Domain fit : Tools evolve with operational needs because builders understand
the problem directly.

Scalability limit : Model cannot scale to large teams. Only limited people
can work within operational reality and build required domain knowledge. This
forces strong prioritization.

Community governance : Being inside the PowSyBl community means helping shape
roadmap responses to regulatory changes and security issues, not waiting for
vendor patches.

## Implementation

PowSyBl framework : Open source power system simulation framework originally
developed by RTE, now hosted at LF Energy. Written in Java for power flow,
contingency analysis, and capacity calculation.

Organizational model : Software development capability embedded within grid
security operations team. Developers share operational context with grid
engineers.

Central IT role : Platform engineering, security compliance, shared tooling
standards, CI/CD pipelines. Infrastructure that makes local innovation viable
without controlling it.

Integration : Business-built software integrates with broader IT landscape
through shared platform capabilities.

## Academic Review Summary

Core claim : Embedding software development within grid operations, built on
shared open source foundations, delivers better tooling than separating
business from IT through requirements documents.

Methodological gaps : No described study design, undefined tenfold metric,
confounded organizational model with technology change, single case without
comparative evidence, no failure analysis or counterfactual.

Unsupported claims : Dissolving boundary is superior to hybrid models, only
insiders can distinguish artifacts, DORA autonomy oversimplified, business
software validates IT without demonstrated security controls.

Missing evidence : Performance benchmarks with statistical variation, DORA
delivery metrics, cost analysis, safety validation, cybersecurity posture,
comparative cases where centralized IT succeeded.

Conflicts with literature : Safety critical systems require independent
assurance; modern DevOps moved beyond requirements handoff years ago; domain
expertise does not guarantee maintainable software; von Hippel supports
co-location not necessarily full boundary dissolution.

Verdict : Plausible case study with intuitive appeal but insufficient
evidence for general organizational prescription. Needs causal separation of
factors, risk analysis, and comparative validation.

## Related

- [[PowSyBl]] ([PowSyBl](powsybl.md))
- [[LF Energy]] ([LF Energy](lf-energy.md))
- [[Sticky Information]] ([Sticky Information](sticky-information.md))
- [[Platform Engineering]] ([Platform Engineering](platform-engineering.md))
- [[Open Source in Power Systems]] ([Open Source in Power Systems](open-source-in-power-systems.md))

## Backlinks
