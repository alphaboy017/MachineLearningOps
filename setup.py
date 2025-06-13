import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "MLflow-Project"
AUTHOR_USER_NAME = "alphaboy017"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "vatsalnpatel1@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="alphaboy017", # type: ignore
    author_email="vatsalnpatel1@gmail.com", # type: ignore
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/alphaboy017/MLflow-Project",
    project_urls={
        "Bug Tracker": f"https://github.com/alphaboy017/MLflow-Project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)