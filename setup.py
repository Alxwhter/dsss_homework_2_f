from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Alex",
    author_email="alxwhte.weiss@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)
