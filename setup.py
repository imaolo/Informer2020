import setuptools
setuptools.setup(
    name='Informer2020', version='0.1',
    packages=setuptools.find_packages(),
    install_requires = ['matplotlib', 'numpy < 2.0', 'pandas', 'scikit_learn', 'torch'],
    extras_require={'testing': ['pytest']},
)