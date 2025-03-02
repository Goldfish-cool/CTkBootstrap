"""
Theme definitions for CTkBootstrap.

This module contains predefined theme configurations for the CTkBootstrap package.
Each theme defines colors, appearance modes, and other UI properties.
"""

# Theme definitions for CTkBootstrap
THEMES = {
    # Solar theme - A dark theme with accent colors inspired by the sun
    "solar": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        "colors": {
            "primary": "#B58900",
            "secondary": "#268BD2",
            "success": "#859900",
            "danger": "#DC322F",
            "warning": "#CB4B16",
            "info": "#2AA198",
            "light": "#FDF6E3",
            "dark": "#002B36"
        },
        "window": {
            "fg_color": ("#002B36", "#002B36")
        },
        "button": {
            "fg_color": ("#B58900", "#B58900"),
            "hover_color": ("#CB4B16", "#CB4B16"),
            "text_color": ("#FDF6E3", "#FDF6E3")
        },
        "frame": {
            "fg_color": ("#073642", "#073642"),
            "border_color": ("#2AA198", "#2AA198")
        },
        "entry": {
            "fg_color": ("#073642", "#073642"),
            "border_color": ("#2AA198", "#2AA198"),
            "text_color": ("#FDF6E3", "#FDF6E3")
        }
    },
    
    # Darkly theme - A flat and modern dark theme
    "darkly": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        "colors": {
            "primary": "#375A7F",
            "secondary": "#444444",
            "success": "#00BC8C",
            "danger": "#E74C3C",
            "warning": "#F39C12",
            "info": "#3498DB",
            "light": "#ADB5BD",
            "dark": "#303030"
        },
        "window": {
            "fg_color": ("#303030", "#303030")
        },
        "button": {
            "fg_color": ("#375A7F", "#375A7F"),
            "hover_color": ("#3498DB", "#3498DB"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "frame": {
            "fg_color": ("#222222", "#222222"),
            "border_color": ("#444444", "#444444")
        }
    },
    
    # Cyborg theme - A dark theme with a cyberpunk feel
    "cyborg": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        "colors": {
            "primary": "#2A9FD6",
            "secondary": "#555555",
            "success": "#77B300",
            "danger": "#CC0000",
            "warning": "#FF8800",
            "info": "#9933CC",
            "light": "#ADAFAE",
            "dark": "#060606"
        },
        "window": {
            "fg_color": ("#060606", "#060606")
        },
        "button": {
            "fg_color": ("#2A9FD6", "#2A9FD6"),
            "hover_color": ("#9933CC", "#9933CC"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "frame": {
            "fg_color": ("#121212", "#121212"),
            "border_color": ("#2A9FD6", "#2A9FD6")
        }
    },
    
    # Vapor theme - A vaporwave aesthetic with purple and blue tones
    "vapor": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        "colors": {
            "primary": "#A177FF",
            "secondary": "#8BAAFF",
            "success": "#75D5FD",
            "danger": "#FF88DC",
            "warning": "#F5D1C5",
            "info": "#85E3FF",
            "light": "#FBFBFB",
            "dark": "#25023F"
        },
        "window": {
            "fg_color": ("#25023F", "#25023F")
        },
        "button": {
            "fg_color": ("#A177FF", "#A177FF"),
            "hover_color": ("#85E3FF", "#85E3FF"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "frame": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "border_color": ("#8BAAFF", "#8BAAFF")
        }
    },
    
    # Monodim - A minimal dark theme using monochromatic colors
    "monodim": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        "colors": {
            "primary": "#6F6F6F",
            "secondary": "#4F4F4F",
            "success": "#8F8F8F",
            "danger": "#D45B5B",
            "warning": "#CFCF9D",
            "info": "#8F9DBF",
            "light": "#E5E5E5",
            "dark": "#1F1F1F"
        },
        "window": {
            "fg_color": ("#1F1F1F", "#1F1F1F")
        },
        "button": {
            "fg_color": ("#6F6F6F", "#6F6F6F"),
            "hover_color": ("#8F8F8F", "#8F8F8F"),
            "text_color": ("#E5E5E5", "#E5E5E5")
        },
        "frame": {
            "fg_color": ("#333333", "#333333"),
            "border_color": ("#4F4F4F", "#4F4F4F")
        }
    },
    
    # Normal CTk - The default CustomTkinter theme
    "normal": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        # Uses the default CustomTkinter colors
    },
    
    # Aurium - A gold and dark theme
    "aurium": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        "colors": {
            "primary": "#D4AF37",  # Gold
            "secondary": "#AA8C2C",
            "success": "#9C7A3C",
            "danger": "#BA4A00",
            "warning": "#F5B041",
            "info": "#D68910",
            "light": "#FAD7A0",
            "dark": "#212121"
        },
        "window": {
            "fg_color": ("#212121", "#212121")
        },
        "button": {
            "fg_color": ("#D4AF37", "#D4AF37"),
            "hover_color": ("#F5B041", "#F5B041"),
            "text_color": ("#212121", "#212121")
        },
        "frame": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "border_color": ("#D4AF37", "#D4AF37")
        }
    }
}

def get_theme_colors(theme_name: str) -> dict:
    """
    Get the colors for a specific theme.
    
    Args:
        theme_name: The name of the theme
        
    Returns:
        A dictionary of color definitions
    """
    theme_name = theme_name.lower()
    if theme_name not in THEMES:
        raise ValueError(f"Theme {theme_name} not found")
    
    return THEMES[theme_name].get("colors", {}) 