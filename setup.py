import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="contas-bckgrd",
    version="0.0.1",
    author="Giovanna Fritsche e Gian Fritsche",
    author_email="ggarciabas@gmail.com",
    description="Serviços para gerenciamento de contas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ggarciabas/contas-bckgrd/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU  v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)