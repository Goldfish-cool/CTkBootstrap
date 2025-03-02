"""
CTkBootstrap - A CustomTkinter theme extension implementing Bootstrap-style themes.

This module provides a wrapper around CustomTkinter to easily apply Bootstrap-inspired
themes to your CustomTkinter applications.
"""

import sys
import os
from typing import Optional, Literal, Dict, Any

# Import CustomTkinter components
try:
    import customtkinter as ctk
    from customtkinter import *
except ImportError:
    raise ImportError("CustomTkinter is required. Install it with 'pip install customtkinter'.")

# Import the theme configurations
from .themes import THEMES, get_theme_colors
from .widget_theme_mapper import apply_theme_to_widget, apply_theme_to_all_children

# Version info
__version__ = "1.0.0"


class CTk(ctk.CTk):
    """
    A wrapper around the CTk class that adds theme support.
    """
    
    def __init__(
        self,
        style: Optional[str] = None,
        fg_color: Optional[str | tuple[str, str]] = None,
        **kwargs
    ):
        """
        Initialize a themed CTk window.
        
        Args:
            style: The name of the theme to apply ("solar", "darkly", "cyborg", "vapor", "monodim", "normal", "aurium")
            fg_color: The background color of the window (overrides theme if provided)
            **kwargs: Additional arguments to pass to CTk
        """
        # Store the current theme name
        self._current_theme = None
        
        # Initialize the base CTk window
        super().__init__(fg_color=fg_color, **kwargs)
        
        # Apply the theme if provided
        if style:
            self.apply_theme(style)
    
    def apply_theme(self, theme_name: str) -> None:
        """
        Apply a predefined theme to the CTk window.
        
        Args:
            theme_name: The name of the theme to apply
        """
        theme_name = theme_name.lower()
        if theme_name not in THEMES:
            valid_themes = ", ".join(THEMES.keys())
            raise ValueError(f"Invalid theme: {theme_name}. Valid themes are: {valid_themes}")
        
        # Get the theme configuration
        theme = THEMES[theme_name]
        
        # Store the current theme name
        self._current_theme = theme_name
        
        # Set the appearance mode (light or dark)
        ctk.set_appearance_mode(theme["appearance_mode"])
        
        # Set the default color theme
        ctk.set_default_color_theme(theme.get("color_theme", "blue"))
        
        # Apply custom colors to the window
        if "window" in theme:
            for prop, value in theme["window"].items():
                if hasattr(self, prop):
                    setattr(self, prop, value)
        
        # Apply theme to existing widgets
        self.update_idletasks()  # Make sure all widgets are created
        apply_theme_to_all_children(self, theme_name, theme)
    
    def get_current_theme(self) -> Optional[str]:
        """
        Get the name of the currently applied theme.
        
        Returns:
            The name of the currently applied theme, or None if no theme has been applied
        """
        return self._current_theme
    
    def apply_theme_to_widget(self, widget, widget_props=None):
        """
        Apply the current theme to a specific widget.
        
        Args:
            widget: The widget to apply the theme to
            widget_props: Optional override for widget properties
        """
        if self._current_theme is None:
            return
        
        theme = THEMES[self._current_theme]
        widget_type = type(widget).__name__.lower()
        
        # Get specific properties for this widget type, or use the widget_props if provided
        if widget_props is None:
            widget_props = theme.get(widget_type, {})
        
        apply_theme_to_widget(widget, self._current_theme, widget_props)


# Enhanced versions of CustomTkinter widgets with theme support

class CTkButton(ctk.CTkButton):
    """Themed version of CTkButton."""
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Apply theme if master has a theme applied
        if hasattr(master, "get_current_theme") and master.get_current_theme():
            theme_name = master.get_current_theme()
            if theme_name and theme_name in THEMES:
                theme = THEMES[theme_name]
                if "button" in theme:
                    button_props = theme["button"]
                    for prop, value in button_props.items():
                        if hasattr(self, prop):
                            setattr(self, prop, value)


class CTkFrame(ctk.CTkFrame):
    """Themed version of CTkFrame."""
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Apply theme if master has a theme applied
        if hasattr(master, "get_current_theme") and master.get_current_theme():
            theme_name = master.get_current_theme()
            if theme_name and theme_name in THEMES:
                theme = THEMES[theme_name]
                if "frame" in theme:
                    frame_props = theme["frame"]
                    for prop, value in frame_props.items():
                        if hasattr(self, prop):
                            setattr(self, prop, value)


class CTkLabel(ctk.CTkLabel):
    """Themed version of CTkLabel."""
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Apply theme if master has a theme applied
        if hasattr(master, "get_current_theme") and master.get_current_theme():
            theme_name = master.get_current_theme()
            if theme_name and theme_name in THEMES:
                theme = THEMES[theme_name]
                if "label" in theme:
                    label_props = theme["label"]
                    for prop, value in label_props.items():
                        if hasattr(self, prop):
                            setattr(self, prop, value)


class CTkEntry(ctk.CTkEntry):
    """Themed version of CTkEntry."""
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Apply theme if master has a theme applied
        if hasattr(master, "get_current_theme") and master.get_current_theme():
            theme_name = master.get_current_theme()
            if theme_name and theme_name in THEMES:
                theme = THEMES[theme_name]
                if "entry" in theme:
                    entry_props = theme["entry"]
                    for prop, value in entry_props.items():
                        if hasattr(self, prop):
                            setattr(self, prop, value)


# Add more themed widgets as needed...

# For backward compatibility with customtkinter, re-export other classes
# (but without themed versions yet)
for name, obj in ctk.__dict__.items():
    if isinstance(obj, type) and name.startswith("CTk") and name not in globals():
        globals()[name] = obj 