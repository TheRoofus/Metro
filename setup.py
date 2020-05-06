from setuptools import setup, find_packages

setup(
    name='train_game',
    classifiers=[
        'Topic :: Software Development :: Libraries :: pygame',
        'Topic :: Games/Entertainment :: Arcade',
    ],
    license='LGPL',
    author=' TheRoofus ',
    maintainer=' TheRoofus ',
    description='Just for fun project. Test skills in game development.',
    include_package_data=True,
    package_dir={'src': 'src'},
    packages=find_packages(),
    url='https://github.com/TheRoofus/Metro/t',
    install_requires=['pygame'],
    version='0.1',
    entry_points={
        'console_scripts': [
            'train_game=src.game:main',
        ],
    },
)