import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swaggerhole",
    version="1.0",
    author="Liodeus",
    author_email="thibaultgalbourdin@gmail.com",
    description="Automate the process of retrieving secrets in the public APIs on swaggerHub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Liodeus/swaggerHole",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)