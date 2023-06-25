import setuptools

setuptools.setup(
    name="river",
    version="0.1",
    description="Fearnworks AI Agents",
    packages=setuptools.find_packages() + ["modules"],
    python_requires=">=3.10",
)