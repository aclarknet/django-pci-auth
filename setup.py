from setuptools import find_packages
from setuptools import setup


VERSION='0.0.1'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description='PCI-compliant authentication application for Django 1.4+. '
        'Uses "best of" existing libraries then fills in the gaps.',
    include_package_data=True,
    install_requires=[
        'docutils',
        'django-axes',
        'django-passwords',
        'py-bcrypt',
        'Django>=1.4',
    ],
    long_description=open("README.rst").read(),
    name='django-pci-auth',
    version=VERSION,
)
