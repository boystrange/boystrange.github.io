---
layout: page
title: Software
---

Below is a list of some software packages I have developed for fun,
teaching and/or research.

## Agda

* <i class="fa-li fab fa-github"></i>
  [A Characterization of Fair Termination in Agda](https://github.com/boystrange/FairTermination)  
  This Agda module formalizes the fair termination property for an
  arbitrary reduction system and proves a sound and complete
  characterization without using the fairness assumption.
* <i class="fa-li fab fa-github"></i>
  [Inference Systems with Corules for Fair Subtyping and Liveness Properties of Binary Session Types](https://github.com/boystrange/FairSubtypingAgda)  
  An Agda formalization of weak termination, fair compliance and
  fair subtyping for dependent session types using generalized
  inference systems.
* <i class="fa-li far fa-save"></i>
  [DLπ – A Dependently-Typed Linear π-Calculus in Agda](https://gitlab.di.unito.it/luca.padovani/DependentLinearPi)  
  An Agda formalization of the linear π-calculus with dependent
  pairs capable of expressing structured conversations involving
  data-dependent processes and protocols.
{:.fa-ul compact}

## Type Systems

* <i class="fa-li fab fa-github"></i>
  [FairCheck -- A Fair Termination Checker for Binary Sessions](https://github.com/boystrange/FairCheck)  
  FairCheck is a proof-of-concept implementation of a type checker
  for a calculus of binary sessions such that well-typed processes
  are guaranteed to be **fairly terminating**.
* <i class="fa-li far fa-save"></i>
  [EasyJoin -- Concurrent Typestate-Oriented Programming in Java]({% link easyjoin.md %})  
  **Join pattern** compiler and **code generator** enabling
  **concurrent TSOP** in Java with runtime detection of protocol
  violations.
* <i class="fa-li far fa-save"></i>
  [MC² -- the Mailbox Calculus Checker]({% link mcc.md %})  
  Mailbox conformance and deadlock analysis in the **Mailbox
  Calculus**, an extension of the actor model where processes
  communicate through **first-class, unordered** mailboxes.
* <i class="fa-li far fa-save"></i>
  [CobaltBlue]({% link Software/CobaltBlue/index.html %})  
  Protocol and **deadlock** analysis in the Objective Join-Calculus.
* <i class="fa-li far fa-save"></i>
  [Hypha]({% link Software/hypha/index.html %})  
  Session type inference, deadlock- and lock-freedom analysis in the
  linear π-calculus.
{:.fa-ul compact}

## Libraries

* <i class="fa-li fab fa-github"></i>
  [FuSe](https://github.com/boystrange/FuSe)  
  OCaml library of **binary sessions** featuring equi-recursive,
  polymorphic, context-free session types, delegation, subtyping,
  session type inference.
{:.fa-ul compact}

## Miscellaneous

* <i class="fa-li fab fa-github"></i>
  [EmacsFiraCode](https://github.com/boystrange/EmacsFiraCode)  
  Small Haskell program that automatically generates the Emacs
  composition table for the [Fira
  Code](https://github.com/tonsky/FiraCode) font.
{:.fa-ul compact}
