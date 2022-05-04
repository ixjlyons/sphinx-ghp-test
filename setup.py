from setuptools import setup, find_packages

setup(
    name="pkg",
    version="0.0.1",
    description="Test",
    packages=find_packages(),
    author="Kenneth R. Lyons",
    python_requires=">=3",
    extras_require={"docs": ["sphinx", "sphinx-gallery", "matplotlib"]},
)
