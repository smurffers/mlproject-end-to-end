from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this funtion will retiurn the list in requirements.txt
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements



setup(
name='mlproject-end-to-end',
version='0.0.1',
author='vivek',
author_email='vvkz.1818@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)