from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="games",
    version="0.0.1",
    author="Vinicius Genu",
    author_email="viniciusgenu01@gmail.com",
    description="Few games to chill out",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vincius-Genu/primeiro_modulo_criado",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)