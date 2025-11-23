#!/usr/bin/env python3
"""
Setup script for Custom Calculator MCP Server
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="custom-calculator-mcp",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Model Context Protocol server with custom calculation tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/custom-calculator-mcp",
    py_modules=["server", "main"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fastmcp>=2.13.1",
    ],
    entry_points={
        "console_scripts": [
            "custom-calculator-mcp=main:main",
        ],
    },
)