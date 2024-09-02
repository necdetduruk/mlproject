from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.

    Parameters:
    file_path (str): The path to the requirements file.

    Returns:
    List[str]: A list of package requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters from each line
        requirements = [req.strip() for req in requirements]

        # Remove the editable installation flag if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='necdetduruk',
    author_email='necdetduruk@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
