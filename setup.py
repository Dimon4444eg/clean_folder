from setuptools import setup

setup(
    name='clean_folder',
    version='1.0',
    description='Very useful code',
    url=[],
    author='Kylishov Dmitriy',
    author_email='home_work@go_it.net',
    license='MIT',
    packages=['clean_folder'],
    install_requires=['transliterate'],
    long_description="Some long desctiption",
    long_description_content_type="text/x-rst",
    entry_points={
        'console_scripts': [
            'clean-folder = clean.functions:main'
        ]
    },
    include_package_data=True
)