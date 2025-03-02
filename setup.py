import setuptools
from customtkinter import *

root = CTk()
long_description = """
A Customtkinter theme extension for CTk that configures all ttkbootstrap themes into CTk GUI. Heavily Inspired by: ttkbootstrap.

Check this out!
## Features

[BUILT-IN-THEMES] 
Customtkinter now includes a built-in theme system, similar to ttkbootstrap, allowing for seamless integration of various themes into your CTk GUI applications. This feature enables developers to easily switch between different visual styles, enhancing the overall user experience.
Not Every theme from ttkbootstrap is in here.

## Includes

** - Solar**

** - Darkly**

** - Cyborg**

** - Vapor**

** - Monodim**

** - Normal CTk**

** - Aurium**

## About Light Mode

Light mode is not everyone's preference, and there are several reasons for this. One major reason is that light mode can cause eye strain, especially in low-light environments. 
Additionally, some users find it harder to focus on the content when the background is bright, leading to decreased productivity. Furthermore, light mode can also make it difficult to distinguish between different UI elements, making the overall user experience less intuitive.

## Heavily Beta

This project is **HEAVILY IN BETA**, indicating that it is still in the early stages of development. 
As a result, it is expected that bugs and issues will arise. 
I am committed to addressing these problems as promptly as possible to ensure the project's stability and quality. 
Your patience and feedback are greatly appreciated during this beta phase.

## Installation
```python
python -m pip install CTkBootstrap
```
## Simple Usage
```python
import CTkBootstrap as CTk

root = CTk(style="solar")

button1 = CTk.Button(root, text="Press Me!")
button1.pack(side=LEFT, padx=5, pady=10)

root.mainloop()

```
## New Themes will come out..

"""


setuptools.setup(
    name="CTkBootstrap",
    version="1.0",
    author="Golden_On60FPS",
    author_email="cahlara11@gmail.com",
    description="A Customtkinter theme extension for CTk that configures all ttkbootstrap themes into CTk GUI. Heavily Inspried by: ttkbootstrap.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT license",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Goldfish-cool/CTkBootstrap",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requries=["customtkinter==5.2.2"],
    python_requries=">=3.13.1"
)