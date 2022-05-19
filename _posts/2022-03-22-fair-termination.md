---
layout: post
title:  "Fair Termination in Agda"
link:   https://github.com/boystrange/FairTermination
---

{% include links.md %}

**Fair termination** is a termination property weaker than strong
termination but stronger than weak termination in which only the
"fair" executions of a system are considered insofar as termination
is concerned, whereas "unfair" executions are considered to be
unrealistic. For a particular **fairness assumption**, it is
possible to provide a sound and complete characterization of fair
termination that does not mention fair executions. The
[FairTermination] module is an Agda formalization of this notion of
fair termination along with soundness and completeness proofs of its
characterization.
