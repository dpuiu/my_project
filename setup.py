from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",  
    author="Daniela PUiu",  
    author_email="dpuiu@jhu.edu",  
    description="Python test",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/dpuiu/my_package", 
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
    install_requires=[
        "numpy>=1.21.0",
        "pandas"
    ],
)