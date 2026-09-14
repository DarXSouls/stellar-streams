import time
import platform

import numpy as np
import gala
import gala.dynamics as gd
import gala.potential as gp
import astropy.units as u


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

N_ORBITS_LIST = [1, 10, 100, 1000]
N_STEPS = 2000

DT = 1 * u.Myr


# ------------------------------------------------------------
# System information
# ------------------------------------------------------------

print("=" * 70)
print("Gala Orbit Integration Benchmark")
print("=" * 70)

print(f"Python      : {platform.python_version()}")
print(f"Gala        : {gala.__version__}")
print(f"CPU         : {platform.processor()}")
print(f"NumPy       : {np.__version__}")
print(f"Steps/orbit : {N_STEPS}")
print(f"dt          : {DT}")
print()


# ------------------------------------------------------------
# Galactic potential
# ------------------------------------------------------------

potential = gp.MilkyWayPotential2022(version="v2")


# ------------------------------------------------------------
# Construct representative initial conditions
# ------------------------------------------------------------

# Galactocentric position:
# roughly solar-neighborhood scale, but intentionally generic
#
# Coordinates:
# x, y, z [kpc]
# vx, vy, vz [km/s]

base_position = np.array([8.0, 0.0, 0.1]) * u.kpc
base_velocity = np.array([10.0, 220.0, 5.0]) * (u.km / u.s)


# ------------------------------------------------------------
# Benchmark
# ------------------------------------------------------------

results = []

print("-" * 70)
print(f"{'N orbits':>12} {'Time (s)':>15} {'orbits/sec':>15}")
print("-" * 70)

for n_orbits in N_ORBITS_LIST:

    # Create slightly different initial conditions for each orbit.
    positions = np.repeat(
        base_position[:, np.newaxis],
        n_orbits,
        axis=1
    )

    velocities = np.repeat(
        base_velocity[:, np.newaxis],
        n_orbits,
        axis=1
    )

    # Small deterministic offsets so these are independent trajectories.
    if n_orbits > 1:
        offsets = np.linspace(
            -0.1,
            0.1,
            n_orbits
        ) * u.kpc

        positions[0] += offsets

    w0 = gd.PhaseSpacePosition(
        pos=positions,
        vel=velocities
    )

    # Warm-up integration for the first case.
    if n_orbits == N_ORBITS_LIST[0]:
        potential.integrate_orbit(
            w0,
            dt=DT,
            n_steps=100
        )

    start = time.perf_counter()

    orbit = potential.integrate_orbit(
        w0,
        dt=DT,
        n_steps=N_STEPS
    )

    elapsed = time.perf_counter() - start

    orbits_per_sec = n_orbits / elapsed

    results.append(
        (n_orbits, elapsed, orbits_per_sec)
    )

    print(
        f"{n_orbits:>12,d} "
        f"{elapsed:>15.6f} "
        f"{orbits_per_sec:>15.3f}"
    )


print("-" * 70)
print()
print("Benchmark completed successfully.")
print()

# Basic sanity check
print("Final phase-space array shape:")
print(orbit.shape)
