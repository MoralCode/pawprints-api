from setuptools import setup, find_packages
setup(
    name="pawprints_api",
    version="0.1.0",
    packages=find_packages(),#['pawprints_api'],
    install_requires=['websockets'],
)