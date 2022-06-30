from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

setup(
    name="serienabend-shef-telegram",
    version="0.0.1",
    description="",
    long_description=readme,
    author="Dominique Mattern",
    author_email="dominique@mattern.dev",
    # url='',
    packages=find_packages(),
)
