import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class Pytest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = [
            '--cov=pykrait', '--cov-report', 'term-missing', '--fulltrace',
            '-vv', '-s'
        ]

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='pykrait',
    python_requires='>=3.6',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    long_description=open('README.md').read(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'simplejson',
    ],
    tests_require=['pytest-cov', 'pytest', 'mock'],
    cmdclass={'test': Pytest},
    test_suite='tests',
)