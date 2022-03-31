from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="git-repos",
    version="1.1.0",
    author="Gabriele Sorci",
    author_email="gabrielesorci.25@gmail.com",
    description="Managment multiple git repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/gab-25/git-repos",
    project_urls={
        "Bug Tracker": "https://github.com/gab-25/git-repos/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=["git_repos"]),
    install_requires=["colorama==0.4.4"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["git-repos=git_repos.__main__:main"],
    },
)
