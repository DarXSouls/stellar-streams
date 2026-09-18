# Stellar Stream Dynamics and Perturbations

Computational investigation of Milky Way stellar streams, with a focus on GD-1 and the observable signatures produced by gravitational perturbations.

## Overview

This repository contains the computational work for a stellar-stream dynamics project focused on modeling the morphology and kinematics of Milky Way stellar streams and investigating their response to controlled gravitational perturbations.

The project uses a GD-1-like stream as the primary test system. A dynamically consistent unperturbed stream is first constructed and validated, after which controlled perturbation experiments are performed using different classes of massive perturbers.

The framework is designed to provide a reproducible way to study how gravitational perturbations modify observable stream properties and to construct quantitative perturbation fingerprints as a function of stream position.

## Scientific Goals

The project is organized around the following goals:

1. Construct a dynamically plausible GD-1 baseline model.
2. Generate and validate an unperturbed GD-1-like stellar stream in a Milky Way gravitational potential.
3. Compare simulated stream properties with observational constraints.
4. Introduce controlled gravitational perturbations from different perturber classes.
5. Measure the resulting changes in stream density, morphology, distance, proper motion, and radial velocity.
6. Construct standardized perturbation fingerprints as a function of stream position.
7. Quantify the dependence of perturbation signatures on perturber properties.
8. Develop diagnostics for comparing perturbation signatures with uncertainties in the underlying Galactic model.

## GD-1 Validation

GD-1 is used as the primary validation system because its extended and well-studied structure provides a useful test case for stellar-stream modeling.

The analysis considers observables including:

- Stream morphology
- Stellar density
- Distance
- Proper motion
- Radial velocity

The primary analysis region is

$$
-60^\circ \leq \phi_1 \leq 0^\circ
$$

The present-day stream model is anchored using observational constraints in the GD-1 coordinate system and evolved in the `MilkyWayPotential` implemented in Gala.

## Perturbation Framework

The perturbation experiments follow a common control-matched framework.

An unperturbed stream is generated using a fixed progenitor model, stripping history, Galactic potential, and random seed. This realization provides the control stream against which perturbed streams are compared.

Perturbed streams are then generated under controlled changes to the dynamical model while keeping the remaining simulation configuration fixed as far as possible.

The response is measured through changes in:

- Stellar density
- Stream latitude (`phi2`)
- Distance
- Proper motion in `phi1`
- Proper motion in `phi2`
- Radial velocity

For each observable, the perturbation response is evaluated as a function of
`phi1`. Bootstrap resampling is used to estimate simulation-realization
uncertainties.

For phase-space observables, standardized fingerprints are constructed as

```math
Z_X(\phi_1)
=
\frac{\Delta X(\phi_1)}
{\sigma_{\Delta X}(\phi_1)}.
```

where the resulting quantity describes the perturbation response relative to
simulation-realization uncertainty. It is not an observational detection
significance.

Density perturbations are treated separately using the logarithmic response.

```math
\Delta\ln\rho(\phi_1)
=
\ln\left[
\frac{N_{\rm pert}(\phi_1)}
{N_{\rm control}(\phi_1)}
\right].
```

## Perturber Experiments

The repository contains controlled perturbation engines for several classes of massive perturbers.

### Dark-Matter Perturbations

`notebooks/03_dm_perturbation_engine.ipynb`

Develops the framework for introducing controlled dark-matter perturbations into the stream model and measuring their resulting observable fingerprints.

The resulting derived products are stored under:

`data/derived/dm_fingerprint_192k/`

### Giant Molecular Cloud Perturbations

`notebooks/04_gmc_perturbation_engine.ipynb`

Applies the control-matched perturbation framework to encounters with giant molecular clouds.

The GMC analysis produces stream-response profiles, fingerprint amplitudes, density responses, and multidimensional comparison products.

The resulting derived products are stored under:

`data/derived/gmc_fingerprint_192k/`

### Globular Cluster Perturbations

`notebooks/05_gc_perturbation_engine.ipynb`

Applies the perturbation framework to controlled encounters with massive globular-cluster perturbers.

The GC experiment uses five controlled encounter configurations, G1–G5, with matched encounter impulse scale. Production streams contain 192,064 realized particles per stream.

The resulting streams are transformed into the GD-1 coordinate system and analyzed using:

- 2° `phi1` profiles
- Density responses
- Phase-space response profiles
- Bootstrap uncertainties
- Standardized fingerprints
- Fingerprint amplitudes
- Within-GC response-shape comparisons

Frozen GC products are stored under:

`data/derived/gc_fingerprint_192k/`

## Current Workflow

The computational workflow is organized into the following stages.

### 1. GD-1 Baseline

`notebooks/01_gd1_baseline.ipynb`

Establishes the observational and modeling framework for the GD-1 system, including the observational anchor and baseline data products.

### 2. Unperturbed Stream Model

`notebooks/02_unperturbed_stream_model.ipynb`

Constructs and evaluates the unperturbed GD-1-like stream in the adopted Milky Way potential. The resulting control realization provides the baseline for subsequent perturbation experiments.

### 3. Dark-Matter Perturbation Engine

`notebooks/03_dm_perturbation_engine.ipynb`

Introduces controlled dark-matter perturbations and develops the perturbation-fingerprint analysis framework.

### 4. GMC Perturbation Engine

`notebooks/04_gmc_perturbation_engine.ipynb`

Extends the perturbation framework to giant molecular cloud encounters and generates reproducible stream-response and fingerprint products.

### 5. GC Perturbation Engine

`notebooks/05_gc_perturbation_engine.ipynb`

Extends the framework to globular-cluster encounters, including encounter construction, self-consistent perturber integration, production stream generation, observable transformation, response profiling, uncertainty estimation, fingerprint construction, and frozen product export.

## Production Analysis

The production perturbation experiments use a common high-resolution stream-generation framework with:

- 192,064 realized stream particles
- 0.5 Myr integration timestep
- 0.5 Myr release cadence
- 1.5 Gyr stripping duration
- Fixed random seed for reproducibility
- `MilkyWayPotential(version="v2")`
- 2° `phi1` analysis bins
- 500 bootstrap resamples
- Robust profile widths based on `1.4826 × MAD`

The production products provide a stable interface between the individual perturbation notebooks and subsequent project-level analysis.

## Derived Products

The `data/derived/` directory contains validated intermediate and frozen products generated by the analysis notebooks.

### Baseline Products

`data/derived/notebook01_handoff/`

Contains the observational and baseline products required by subsequent notebooks.

### Unperturbed Stream

`data/derived/s0/`

Contains the frozen unperturbed stream realization and its metadata.

### Dark-Matter Fingerprint Products

`data/derived/dm_fingerprint_192k/`

Contains the dark-matter perturbation streams, control realization, response products, summary tables, resolution-convergence information, and radial-velocity diagnostics.

### GMC Fingerprint Products

`data/derived/gmc_fingerprint_192k/`

Contains GMC perturbation streams and matched controls together with:

- Phase-space response profiles
- Density responses
- Fingerprint amplitudes
- DM–GMC response comparisons
- Multidimensional response distances
- Density-inclusive information-ablation analysis
- Metadata and resolution-convergence products

### GC Fingerprint Products

`data/derived/gc_fingerprint_192k/`

Contains the five GC perturbation streams, control stream, profiles, response fingerprints, amplitude summaries, shape-comparison products, and metadata.

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
│       │
│       ├── dm_fingerprint_192k/
│       │   ├── dm_fingerprint_summary.csv
│       │   ├── dm_response_192k.csv
│       │   ├── metadata.json
│       │   ├── resolution_convergence.json
│       │   ├── rv_diagnostic.json
│       │   ├── S_control_192k.npz
│       │   └── S_DM_192k.npz
│       │
│       ├── gmc_fingerprint_192k/
│       │   ├── dm_gmc_information_ablation_192k.csv
│       │   ├── dm_gmc_multidimensional_distance_192k.csv
│       │   ├── dm_gmc_response_comparison_192k.csv
│       │   ├── gmc_density_responses_192k.csv
│       │   ├── gmc_fingerprint_amplitudes_192k.csv
│       │   ├── gmc_phase_space_responses_192k.csv
│       │   ├── metadata.json
│       │   ├── resolution_convergence.json
│       │   ├── S_control_G1_192k.npz
│       │   ├── S_control_G2_192k.npz
│       │   ├── S_control_G3_192k.npz
│       │   ├── S_control_G4_192k.npz
│       │   ├── S_control_G5_192k.npz
│       │   ├── S_GMC_G1_192k.npz
│       │   ├── S_GMC_G2_192k.npz
│       │   ├── S_GMC_G3_192k.npz
│       │   ├── S_GMC_G4_192k.npz
│       │   └── S_GMC_G5_192k.npz
│       │
│       ├── notebook01_handoff/
│       │   ├── baseline_metadata.json
│       │   ├── gd1_anchor.json
│       │   ├── gd1_distance_deboer.csv
│       │   └── gd1_profiles.csv
│       │
│       ├── s0/
│       │   ├── S0_metadata.json
│       │   └── S0_particles.npz
│       │
│       └── gc_fingerprint_192k/
│           ├── gc_fingerprint_amplitudes_192k.csv
│           ├── gc_profiles_192k.csv
│           ├── gc_response_shape_comparison_192k.csv
│           ├── gc_responses_192k.csv
│           ├── metadata.json
│           ├── S_control_192k.npz
│           ├── S_GC_G1_192k.npz
│           ├── S_GC_G2_192k.npz
│           ├── S_GC_G3_192k.npz
│           ├── S_GC_G4_192k.npz
│           └── S_GC_G5_192k.npz
│
└── notebooks/
    ├── 01_gd1_baseline.ipynb
    ├── 02_unperturbed_stream_model.ipynb
    ├── 03_dm_perturbation_engine.ipynb
    ├── 04_gmc_perturbation_engine.ipynb
    └── 05_gc_perturbation_engine.ipynb
