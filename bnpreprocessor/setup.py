import setuptools
 
with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="bnpreprocessor",
    version= "1.0.6",
    author="Abu Kaisar Mohammad Masum",
 
    author_email="abukaisar24@gmail.com",
 
    description="bengali automatic text preprocessor",
 
    long_description=long_description,
    url="https://github.com/kaisarmasum/bnpreprocessor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
