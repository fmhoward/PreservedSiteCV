from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Preserved Site Cross Validation'
LONG_DESCRIPTION = 'Provides optimal stratification while preserving sites for cross validation'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="preservedsite",
    version=VERSION,
    author="Frederick Howard",
    author_email="<fhoward@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pandas", "numpy", "cvxpy", "cplex"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'cross validation'],
    classifiers=[
        "Development Status :: 2 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)