from setuptools import setup

setup(
    name='utilities',
    version='0.1',
    py_modules=['files'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'rename=files:rename_all_file_extensions', # command=package.module:function
        ],
    },
)