#python setup.py build_ext --inplace --language_level=3
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("sp800_22_approximate_entropy_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_binary_matrix_rank_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_cumulative_sums_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_dft_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_frequency_within_block_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_linear_complexity_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_longest_run_ones_in_a_block_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_maurers_universal_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_monobit_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_non_overlapping_template_matching_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_overlapping_template_matching_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_random_excursion_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_random_excursion_variant_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_runs_test.pyx")
)

setup(
    ext_modules = cythonize("sp800_22_serial_test.pyx")
)

