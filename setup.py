# coding=utf-8
from setuptools import setup

requirements = [
	line.decode("UTF-8")
	for line
	in open("requirements.txt", "rb")
	if line.strip() and not line.startswith(b"#")
]

setup(
    name='hayes',
    version='0.0.5',
    packages=['hayes', 'hayes.analysis', 'hayes.ext', 'hayes.django_interop', 'hayes.search'],
    license='MIT',
    long_description="n/a",
    maintainer="Anders Innovations",
    maintainer_email="support@anders.fi",
    install_requires=requirements
)
