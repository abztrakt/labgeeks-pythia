from setuptools import setup

setup(
    name = 'labgeeks-pythia',
    version = '1.0',
    license = 'Apache',
    url = 'http://github.com/abztrakt/labgeeks_pythia',
    description = 'The wiki app in the labgeeks suite of student staff management tools.',
    author = 'Craig Stimmel',
    packages = ['labgeeks_pythia',], 
    install_requires = [
        'setuptools',
        'labgeeks-sybil',
        'South==0.7.3',
        'Markdown==2.2.0',
        'diff-match-patch==20120106',
    ],
)
