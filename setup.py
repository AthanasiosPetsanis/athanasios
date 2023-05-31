from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


# setuptools.setup(
#      name='athanasios',  
#      version='0.1',
#      scripts=['athanasios'] ,
#      author="Athanasios Petsanis",
#      author_email="athpets8@gmail.com",
#      description="Some General functions I use that are currently useful. Beta version.",
#      long_description=long_description,
#      long_description_content_type="text/markdown",
#      url="https://github.com/AthanasiosPetsanis/athanasios",
#      packages=setuptools.find_packages(),
#      classifiers=[
#          "Programming Language :: Python :: 3",
#          "License :: None",
#          "Operating System :: OS Independent",
#      ],
#     #  package_data={'': ['*.py']},
#      py_modules=['General_Functions'],
#      install_requires=[
#         'time',
#         'csv',
#         'numpy',
#         'matplotlib',
#         'os',
#         'statistics',
#         'datetime',
#      ],
#     #  include_package_data=True,
#  )

setup(
    name='athanasios',
    version='0.1',
    author="Athanasios Petsanis",
    author_email="athpets8@gmail.com",
    description="Some General functions I use that are currently useful. Beta version.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AthanasiosPetsanis/athanasios",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'matplotlib',
        'statistics',
        'datetime',
    ],
)