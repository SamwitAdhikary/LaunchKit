from setuptools import setup, find_packages

setup(
    name="launchkit-cli",
    version="0.1.0",
    description="LaunchKit CLI",
    author="Your Name",
    author_email="you@example.com",
    license="MIT",
    packages=find_packages(include=["launchkit_cli", "launchkit_cli.*"]),
    install_requires=[
        "typer[all]>=0.9",
        "httpx>=0.24",
        "keyring>=23.13",
    ],
    entry_points={
        "console_scripts": [
            "launchkit=launchkit_cli.cli:app",
        ],
    },
)
