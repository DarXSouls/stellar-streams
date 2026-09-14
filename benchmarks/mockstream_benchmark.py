import time
import platform

import numpy as np
import astropy.coordinates as coord
import astropy.units as u

import gala
import gala.dynamics as gd
import gala.potential as gp
from gala.dynamics import mockstream as ms
from gala.units import galactic


# ============================================================
# Configuration
# ============================================================

N_STEPS_LIST = [500, 1000, 2000, 4000]
DT = -1 * u.Myr


# ============================================================
# System information
# ============================================================

print("=" * 70)
print("Gala Mock-Stream Generation Benchmark")
print("=" * 70)

print(f"Python : {platform.python_version()}")
print(f"Gala   : {gala.__version__}")
print(f"NumPy  : {np.__version__}")
print()


# ============================================================
# Milky Way potential
# ============================================================

pot = gp.CCompositePotential()

pot["disk"] = gp.MiyamotoNagaiPotential(
    m=6e10 * u.Msun,
    a=3.5 * u.kpc,
    b=280 * u.pc,
    units=galactic,
)

pot["halo"] = gp.NFWPotential(
    m=7e11,
    r_s=15 * u.kpc,
    units=galactic,
)


# ============================================================
# Pal 5-like progenitor phase-space position
# ============================================================

c = coord.ICRS(
    ra=229 * u.deg,
    dec=-0.124 * u.deg,
    distance=22.9 * u.kpc,
    pm_ra_cosdec=-2.296 * u.mas / u.yr,
    pm_dec=-2.257 * u.mas / u.yr,
    radial_velocity=-58.7 * u.km / u.s,
)

c_gc = c.transform_to(coord.Galactocentric()).cartesian

w0 = gd.PhaseSpacePosition(c_gc)


# ============================================================
# Progenitor
# ============================================================

progenitor_mass = 2.5e4 * u.Msun

progenitor_pot = gp.PlummerPotential(
    m=progenitor_mass,
    b=4 * u.pc,
    units=galactic,
)


# ============================================================
# Stream distribution function
# ============================================================

df = ms.FardalStreamDF(gala_modified=False)


# ============================================================
# Stream generator
# ============================================================

generator = ms.MockStreamGenerator(
    df,
    pot,
    progenitor_potential=progenitor_pot,
)


# ============================================================
# Benchmark
# ============================================================

print("-" * 70)
print(
    f"{'Steps':>10} "
    f"{'Time (s)':>15} "
    f"{'Particles':>15} "
    f"{'Particles/s':>18}"
)
print("-" * 70)


for n_steps in N_STEPS_LIST:

    start = time.perf_counter()

    stream, _ = generator.run(
        w0,
        progenitor_mass,
        dt=DT,
        n_steps=n_steps,
    )

    elapsed = time.perf_counter() - start

    n_particles = stream.shape[0]

    particle_rate = n_particles / elapsed

    print(
        f"{n_steps:>10,d} "
        f"{elapsed:>15.6f} "
        f"{n_particles:>15,d} "
        f"{particle_rate:>18.2f}"
    )


print("-" * 70)

print()
print("Final stream object:")
print(stream)

print()
print("Final stream shape:")
print(stream.shape)

print()
print("Benchmark completed successfully.")
