# -*- coding: utf-8 -*-
"""
"""

from __future__ import annotations

from os import path

from setuptools import find_packages, setup


SRC = path.join(path.dirname(__file__), "src")
REQUIRE_FILE = path.join(path.dirname(__file__), "requirements.txt")


def get_requirements():
    with open(REQUIRE_FILE, "r") as fd:
        return [r for r in fd]


def main():
    setup(
        name="cadquery-cpl",
        fullname="CadQuery 2 Common Part Library",
        package_dir={"": "src"},
        packages=find_packages("src"),
        install_requires=get_requirements(),
        data_files=[("", ["requirements.txt"])]
    )


if __name__ == "__main__":
    main()
