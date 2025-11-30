from setuptools import setup, find_packages


with open('.apiversion', 'r') as vers, open('README.md', 'r') as desc:
    version = vers.read()
    description = desc.read()

setup(
    name='tunaapi',
    version=version,
    packages=find_packages(),
    install_requires=[
        'anyio~=4.9.0',
        'certifi~=2025.4.26',
        'h11~=0.16.0',
        'httpcore~=1.0.9',
        'httpx~=0.28.1',
        'idna~=3.10',
        'sniffio~=1.3.1',
    ],
    long_description=description,
    long_description_content_type='text/markdown',
)
