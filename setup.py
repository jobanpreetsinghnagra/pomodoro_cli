from setuptools import setup, find_packages

setup(
    name="pomodoro_cli",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["main", "base"],
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "pomodoro=main:app",
        ],
    },
    author="Your Name",
    description="A simple Pomodoro timer CLI built with Typer.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)