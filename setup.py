from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    aythor='Somen',
    author_email='somen030@gmail.com',
    pakages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)