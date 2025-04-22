from setuptools import setup, find_packages

setup(
    name="simple_driving",
    version='0.0.1',
    install_requires=[
        'gym',
        'pybullet',
        'numpy',
        'matplotlib',
        'torch'
    ],
    packages=find_packages(),  
    include_package_data=True,  
    package_data={
        'simple_driving': ['resources/*.urdf']
    }
)
