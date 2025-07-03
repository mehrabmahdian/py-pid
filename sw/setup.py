# sw/setup.py

import setuptools
from pathlib import Path

root = Path(__file__).resolve().parent.parent
readme_path = root / "README.md"

with open(readme_path, "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py-PID",
    version="0.0.1",
    author="Mehrab Mahdian",
    author_email="memahdian@outlook.com",
    description="Py-PID: A simple Python package for PID control.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mehrabmahdian/py-pid",
    package_dir={"": "."},  # packages are inside `sw/py_pid`
    packages=setuptools.find_packages(where="."),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
