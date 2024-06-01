from setuptools import setup
from Cython.Build import cythonize
import numpy
setup(
    name="pointman",
    ext_modules=cythonize("pointman.pyx", annotate=True),
    include_dirs=[numpy.get_include()]
)    
