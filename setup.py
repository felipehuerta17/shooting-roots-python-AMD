from setuptools import setup, find_packages

setup(
    name='shooting_roots',
    version='0.1.0',
    description='Shooting method for Richards\' equation with root water uptake',
    author='F.V. Difonzo et al.',
    url='https://github.com/fdifonzo/shooting-roots-python-code',
    packages=find_packages(exclude=['Examples']),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
