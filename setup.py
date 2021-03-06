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
            'rename_extensions=files:rename_all_file_extensions', # command=package.module:function
            'rename_ableton_freeze=files:rename_ableton_freeze_samples', # command=package.module:function
        ],
    },
)