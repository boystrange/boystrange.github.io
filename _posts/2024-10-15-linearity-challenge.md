---
layout: post
title:  "A solution of the linearity challenge"
---

Claudia Raffaelli and I have been working on an Agda solution of the
linearity challenge that was proposed earlier this year in [the
Concurrent Calculi Formalisation
Benchmark](https://concurrentbenchmark.github.io). Our solution
formalizes
[πLIN](http://dx.doi.org/10.4230/LIPIcs.CONCUR.2022.36) -- a linear
π-calculus based on linear logic -- using the *context splitting*
technique. This technique is traditionally considered heavy but we
find that in the setting of πLIN it works very well. The
formalisation is [publicly available on
GitHub](https://github.com/boystrange/LinearityChallenge/tree/main/fin),
with further developments coming soon.
