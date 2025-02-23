from setuptools import find_packages, setup
from typing import List


# find_packages() - it will find all the packages in the directory
# setup() - it will setup the project


def get_requirements(file_path) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    
    requirementsList = []
    try:
        with open(file_path) as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements != '-e .':
                    requirementsList.append(requirements)

    except FileNotFoundError:
        print("Requirements.txt not found")
        
    return requirementsList


setup(
    name = 'Network Security Project',
    version = '0.0.1',
    author = 'Pranav',
    author_email = 'reach.sharmapranav@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)