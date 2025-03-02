# CTkBootstrap Source Code

This directory contains the source code for the CTkBootstrap package.

## Structure

- `CTkBootstrap/` - The main package directory
  - `__init__.py` - Main package entry point with the CTk wrapper class
  - `themes.py` - Definitions for all the theme configurations
  - `widget_theme_mapper.py` - Functions to apply theme properties to CustomTkinter widgets

## How Themes Work

Each theme in CTkBootstrap is defined as a dictionary in `themes.py` with the following structure:

```python
"theme_name": {
    "appearance_mode": "dark",  # or "light"
    "color_theme": "blue",  # base CTk color theme
    "colors": {
        # Bootstrap-style color definitions
        "primary": "#hex_code",
        "secondary": "#hex_code",
        # etc.
    },
    "window": {
        # CTk window properties
        "fg_color": ("#hex_light", "#hex_dark"),
        # etc.
    },
    "button": {
        # CTkButton properties
        "fg_color": ("#hex_light", "#hex_dark"),
        "hover_color": ("#hex_light", "#hex_dark"),
        # etc.
    },
    # Other widget-specific properties
}
```

When a theme is applied to a CTk window, the properties are set on the window and then recursively applied to all child widgets.

## Adding New Themes

To add a new theme, simply add a new entry to the `THEMES` dictionary in `themes.py` following the structure above.

## Adding Support for New Widgets

To add theme support for a new CustomTkinter widget:

1. Create a new function in `widget_theme_mapper.py` to apply theme properties to the new widget type
2. Add the new widget type and function to the `WIDGET_THEME_MAPPERS` dictionary
3. Create a themed wrapper class in `__init__.py` for the new widget 