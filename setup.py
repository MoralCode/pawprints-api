from setuptools import setup, find_packages
setup(
    name="pawprints_api",
    version="0.1.0",
    packages=find_packages(),
    package_dir={'': '.'},
    package_data={'pawprints_api': '*'},
    include_package_data=True,
    install_requires=['websockets'],
)