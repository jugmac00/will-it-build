"""
will-it-build setup.py
"""
import re
from pathlib import Path

from setuptools import find_packages, setup

NAME = "will-it-build"
KEYWORDS = ["build", "twine"]
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: MacOS",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]
INSTALL_REQUIRES = []

# --+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----


if __name__ == "__main__":
    HERE = Path(__file__).resolve().parent
    META_FILE = (HERE / "src" / "willitbuild" / "__init__.py").read_text()
    META = dict(
        re.findall(r"^__(\w+)__ = ['\"]([^'\"]*)['\"]", META_FILE, re.M)
    )
    setup(
        name=NAME,
        description=META["description"],
        license=META["license"],
        url=META["url"],
        version=META["version"],
        author=META["author"],
        author_email=META["email"],
        maintainer=META["author"],
        maintainer_email=META["email"],
        keywords=KEYWORDS,
        long_description=Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        extras_require={"test": []},
        options={},
        include_package_data=True,
    )
