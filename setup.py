from setuptools import setup

setup(
    name='hayes',
    version='0.0.1',
    packages=['hayes'],
    license='MIT',
    long_description="n/a",
    maintainer="Aarni Koskela",
    maintainer_email="akx@iki.fi",
    install_requires=[line for line in file("requirements.txt", "rb") if line.strip() and not line.startswith("#")]
)