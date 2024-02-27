---
layout: post
title:  FairCheck
link:   https://github.com/boystrange/FairCheck
---

{% include links.md %}

The [GitHub repository of
FairCheck](https://github.com/boystrange/FairCheck) is now publicly
available.  FairCheck is a proof-of-concept implementation of a type
checker for a calculus of binary sessions such that well-typed
processes are guaranteed to be fairly terminating. Fair termination
is a generalized form of termination whereby all infinite executions
of a process are deemed unrealistic because they violate some
fairness assumption. The type system on which FairCheck is based is
also the first one using [**fair subtyping**](#Padovani13B), a
liveness-preserving refinement of the subtyping relation for session
types.
