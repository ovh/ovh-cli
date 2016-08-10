from setuptools import setup

import ovhcli


entry_points = {
    'console_scripts': [
        'ovh=ovhcli.cli:cli',
    ]
}

requirements = open('requirements.txt').read()

readme = open('README.rst').read()

setup(
    name="ovhcli",
    version=ovhcli.__version__,
    url='http://github.com/ovh/ovhcli',
    author='Nicolas Crocfer',
    author_email='nicolas.crocfer@corp.ovh.com',
    description="OVH Command Line Interface",
    long_description=readme,
    packages=['ovhcli'],
    include_package_data=True,
    install_requires=requirements,
    entry_points=entry_points,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
