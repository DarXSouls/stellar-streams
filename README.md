# Stellar Stream Dynamics and Perturbations

Computational investigation of Milky Way stellar streams, with a focus on
GD-1 and the effects of gravitational perturbations.

## Overview

This repository contains the ongoing computational work for a stellar-stream
dynamics project focused on modeling the morphology and kinematics of Milky
Way stellar streams and investigating their response to gravitational
perturbations.

The current development phase focuses on establishing a dynamically plausible
unperturbed GD-1-like stream model and validating its observable properties
against observational data before introducing controlled perturbations.

The project is intended as a reproducible computational framework for
studying how different dynamical assumptions and perturbers can influence
stellar-stream observables.

## Scientific Goals

The project is organized around the following goals:

1. Construct a dynamically plausible GD-1 baseline model.
2. Generate an unperturbed stellar stream in a Milky Way gravitational
   potential.
3. Compare simulated and observed stream properties.
4. Introduce controlled dark-matter perturbations.
5. Investigate how perturbations affect observable stream morphology and
   kinematics.
6. Develop diagnostics for distinguishing perturbation signatures from
   uncertainties in the underlying Galactic model.

## GD-1 Validation

GD-1 is used as the primary validation system because its extended,
well-studied structure provides a useful test case for stream modeling.

The analysis considers observables including:

- Stream morphology
- Stellar density
- Distance
- Proper motion
- Radial velocity

The current validation work emphasizes the region

\[
-60^\circ \leq \phi_1 \leq 0^\circ,
\]

where the observational constraints used by the project are best established.

## Current Workflow

The present computational workflow is divided into three main stages.

### 1. GD-1 Baseline

`notebooks/01_gd1_baseline.ipynb`

Establishes the initial GD-1 observational and modeling framework, including
the data products required for subsequent analysis.

### 2. Unperturbed Stream Model

`notebooks/02_unperturbed_stream_model.ipynb`

Develops and evaluates an unperturbed GD-1-like stellar-stream model in a
Milky Way gravitational potential.

### 3. Dark-Matter Perturbation Engine

`notebooks/03_dm_perturbation_engine.ipynb`

Develops the computational framework for introducing controlled
dark-matter-induced perturbations into the stream model.

This component is currently under development.

## Repository Structure

```text
stellar-streams/
│
├── benchmarks/
│   ├── gala_orbit_benchmark.py
│   ├── mockstream_benchmark.py
│   └── mockstream_parallel_benchmark.py
│
├── data/
│   └── derived/
│       ├── notebook01_handoff/
│       │   ├── baseline_metadata.json
│       │   ├── gd1_anchor.json
│       │   ├── gd1_distance_deboer.csv
│       │   └── gd1_profiles.csv
│       │
│       └── s0/
│           ├── S0_metadata.json
│           └── S0_particles.npz
│
└── notebooks/
    ├── 01_gd1_baseline.ipynb
    ├── 02_unperturbed_stream_model.ipynb
    └── 03_dm_perturbation_engine.ipynb
