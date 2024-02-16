from  setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long = f.read()

setup(
    name="pyrema",
    version='1.0',
    description='Manage a LaTeX project structure.',
    long_description=long,
    author='lawrej1',
    author_email="thejasonlawrence1@gmail.com",
    packages=find_packages(),
    url="https://github.com/Jason-Lawrence/pyrema/tree/master",
    install_requires=[
        "pylatex"
    ]
)