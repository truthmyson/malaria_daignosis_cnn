# this setup.py file will help build and and package our codes as a library (python package)
# so that we can import all the modules(folder's that have _iit__.py files in them) easily
import setuptools

# we will use the readme file as a long description for our package(especially on how to use it)
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0" # package version

REPO_NAME = "MALARIA_DIAGNOSIS"
AUTHOR_USER_NAME = "truthmyson"
SRC_REPO = "cnnclassifier"
AUTHOR_EMAIL = "nageteychristopher@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for a malaria diagnosisCNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={ #add other links useful to the project
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, #tells the setuptools that our packages are in the src directory("" - means root folder)
    packages=setuptools.find_packages(where="src") #we will only create packages from the src directory
)