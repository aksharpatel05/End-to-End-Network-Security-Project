'''
The setup.py file is used in Python projects to define metadata and configuration
for packaging and distributing the project as a Python package.

It typically includes information such as the package name, version, author,
description, dependencies, and entry points.
'''

from setuptools import setup, find_packages 
from typing import List

def get_requriements() -> List[str]:
    """
    This function returns a list of requirements
    """
    requirements_lst: List[str] = [] # Initialize an empty list to store requirements
    try:
        with open('requirements.txt', 'r') as file:
            # Read the file and return a list of lines
            lines = file.readlines()
            #process each line
            for line in lines:
                # Remove any leading or trailing whitespace
                requirements = line.strip()
                # ignore empty lines and -e .
                if requirements and requirements != '-e .':
                    return requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found. No requirements will be installed.")

    return requirements_lst

setup(
    name='Network_Security',
    version='0.0.1',
    author='Akshar Patel',
    packages = find_packages(), # Automatically find and include all packages in the project
    install_requires=get_requriements() # List of dependencies to be installed
)     
        