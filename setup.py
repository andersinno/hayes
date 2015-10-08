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
    version='0.0.4',
    packages=['hayes', 'hayes.analysis', 'hayes.ext', 'hayes.django_interop', 'hayes.search'],
    license='MIT',
    long_description="n/a",
    maintainer="Aarni Koskela",
    maintainer_email="akx@iki.fi",
    install_requires=requirements
)
