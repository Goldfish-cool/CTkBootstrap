import setuptools
import os

# Read the long description from README.md
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CTkBootstrap",
    version="1.0.0",
    author="Golden_On60FPS",
    author_email="cahlara11@gmail.com",
    description="A Customtkinter theme extension for CTk that configures all ttkbootstrap themes into CTk GUI. Heavily Inspired by: ttkbootstrap.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Goldfish-cool/CTkBootstrap",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["customtkinter>=5.2.0"],
    python_requires=">=3.7",
)