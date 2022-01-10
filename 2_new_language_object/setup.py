
from setuptools import setup
setup(
    name="yor",
    entry_points={
        "spacy_languages": ["yor = yor:Yoruba"],
    }
)
