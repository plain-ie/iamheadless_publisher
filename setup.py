from distutils.core import setup

setup(

    # Application name:
    name="iamheadless_publisher",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Maris Erts",
    author_email="maris@plain.ie",

    # Packages
    packages=["iamheadless_publisher"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    license="LICENSE",
    description="#",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "django==4.0.3",
        "djantic==0.4.1",
        "pydantic==1.9.0",
    ],

)
