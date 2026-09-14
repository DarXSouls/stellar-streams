import time
import platform
import multiprocessing as mp

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

N_STREAMS_LIST = [16, 20, 24]
N_STEPS = 2000
DT = -1 * u.Myr


# ============================================================
# Worker
# ============================================================

def generate_stream(seed):

    # Give each realization a deterministic but slightly
    # different progenitor position.

    rng = np.random.default_rng(seed)

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

    c = coord.ICRS(
        ra=(229 + rng.normal(0, 0.01)) * u.deg,
        dec=(-0.124 + rng.normal(0, 0.01)) * u.deg,
        distance=(22.9 + rng.normal(0, 0.02)) * u.kpc,
        pm_ra_cosdec=(-2.296 + rng.normal(0, 0.002)) * u.mas / u.yr,
        pm_dec=(-2.257 + rng.normal(0, 0.002)) * u.mas / u.yr,
        radial_velocity=(-58.7 + rng.normal(0, 0.5)) * u.km / u.s,
    )

    c_gc = c.transform_to(
        coord.Galactocentric()
    ).cartesian

    w0 = gd.PhaseSpacePosition(c_gc)

    progenitor_mass = 2.5e4 * u.Msun

    progenitor_pot = gp.PlummerPotential(
        m=progenitor_mass,
        b=4 * u.pc,
        units=galactic,
    )

    df = ms.FardalStreamDF(
        gala_modified=False
    )

    generator = ms.MockStreamGenerator(
        df,
        pot,
        progenitor_potential=progenitor_pot,
    )

    stream, _ = generator.run(
        w0,
        progenitor_mass,
        dt=DT,
        n_steps=N_STEPS,
    )

    return stream.shape[0]


# ============================================================
# Main benchmark
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("Gala Parallel Mock-Stream Benchmark")
    print("=" * 70)

    print(f"Python       : {platform.python_version()}")
    print(f"Gala         : {gala.__version__}")
    print(f"CPU count    : {mp.cpu_count()}")
    print(f"Steps/stream : {N_STEPS}")
    print(f"dt           : {DT}")
    print()

    print("-" * 70)
    print(
        f"{'Processes':>12} "
        f"{'Streams':>12} "
        f"{'Time (s)':>15} "
        f"{'Streams/s':>15} "
        f"{'Speedup':>12}"
    )
    print("-" * 70)

    baseline_time = None

    for n_streams in N_STREAMS_LIST:

        start = time.perf_counter()

        with mp.Pool(
            processes=n_streams
        ) as pool:

            particle_counts = pool.map(
                generate_stream,
                range(n_streams)
            )

        elapsed = time.perf_counter() - start

        streams_per_sec = n_streams / elapsed

        if baseline_time is None:
            baseline_time = elapsed

        speedup = baseline_time / elapsed

        print(
            f"{n_streams:>12} "
            f"{n_streams:>12} "
            f"{elapsed:>15.4f} "
            f"{streams_per_sec:>15.3f} "
            f"{speedup:>12.2f}x"
        )

    print("-" * 70)

    print()
    print("Particle counts from final run:")
    print(particle_counts)

    print()
    print("Benchmark completed successfully.")
