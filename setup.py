from setuptools import setup, find_packages

setup(
    name="CalculadoraMatricesVectores",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "calculadora=src.main:main",
        ],
    },
)