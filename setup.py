from setuptools import setup, find_packages
from pathlib import Path

with open("requirements.txt") as requirements_txt:
    requirements = requirements_txt.read().splitlines()

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="porn-cli",
    version="1.0.0",
    author="pain@poseidon444",
    author_email="painedposeidon444@gmail.com",
    maintainer="ananas@r3tr0ananas",
    maintainer_email="r3tr0ananas@hotmail.com",
    description="A module to download and stream your favorite pornos.",
    packages=find_packages(),
    url="https://github.com/mov-cli/porn-cli",
    keywords=[
        "stream",
        "porn",
        "porns",
        "pornhub",
        "xxxmax",
        "hentaimama",
        "javct"
    ],
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        porn-cli=porn_cli.__main__:porncli
    """,
    long_description_content_type="text/markdown",
    long_description=long_description,
)