#python setup.py build_ext --inplace 
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("otp.pyx")
)

setup(
    ext_modules = cythonize("dec.pyx")
)

setup(
    ext_modules = cythonize("enc.pyx")
)
