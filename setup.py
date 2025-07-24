from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="FLIPKART_RECOMMENDER",
    author="niraj pandey",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements
)