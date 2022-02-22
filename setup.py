from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in boltmaster_v2/__init__.py
from boltmaster_v2 import __version__ as version

setup(
	name="boltmaster_v2",
	version=version,
	description="Boltmaster",
	author="usama",
	author_email="usamanaveed9263@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
