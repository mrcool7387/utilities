from setuptools import setup, find_packages

setup(
    name='utilitys',  # The name of your package
    version='1.0.0',  # Initial version
    description='A versatile collection of useful functions for file management, console output, screen control, and more.',
    long_description=open('README.md').read(),  # Load long description from README file
    long_description_content_type='text/markdown',  # Content type for the long description
    author='Alexander Schwarz',  # Replace with your name
    author_email='alexander.schwarz148@gmail.com',  # Replace with your email
    url='https://github.com/mrcool7387/utilities/',  # Replace with the URL to your project repository
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        'colorama',  # List of dependencies
        'datetime',
        're',
        'shutil',
        'logging',
        'zipfile',
        'uuid',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Replace with your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version
)
