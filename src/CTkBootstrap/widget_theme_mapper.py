"""
Widget theme mapper for CTkBootstrap.

This module provides functions to apply theme properties to specific CustomTkinter widgets.
"""

from typing import Dict, Any, Optional
import customtkinter as ctk


def apply_theme_to_button(button: ctk.CTkButton, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkButton.
    
    Args:
        button: The button widget to style
        theme_props: The theme properties to apply
    """
    if "fg_color" in theme_props:
        button.configure(fg_color=theme_props["fg_color"])
    
    if "hover_color" in theme_props:
        button.configure(hover_color=theme_props["hover_color"])
    
    if "text_color" in theme_props:
        button.configure(text_color=theme_props["text_color"])
    
    if "border_color" in theme_props:
        button.configure(border_color=theme_props["border_color"])


def apply_theme_to_frame(frame: ctk.CTkFrame, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkFrame.
    
    Args:
        frame: The frame widget to style
        theme_props: The theme properties to apply
    """
    if "fg_color" in theme_props:
        frame.configure(fg_color=theme_props["fg_color"])
    
    if "border_color" in theme_props:
        frame.configure(border_color=theme_props["border_color"])


def apply_theme_to_label(label: ctk.CTkLabel, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkLabel.
    
    Args:
        label: The label widget to style
        theme_props: The theme properties to apply
    """
    if "fg_color" in theme_props:
        label.configure(fg_color=theme_props["fg_color"])
    
    if "text_color" in theme_props:
        label.configure(text_color=theme_props["text_color"])


def apply_theme_to_entry(entry: ctk.CTkEntry, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkEntry.
    
    Args:
        entry: The entry widget to style
        theme_props: The theme properties to apply
    """
    if "fg_color" in theme_props:
        entry.configure(fg_color=theme_props["fg_color"])
    
    if "border_color" in theme_props:
        entry.configure(border_color=theme_props["border_color"])
    
    if "text_color" in theme_props:
        entry.configure(text_color=theme_props["text_color"])


def apply_theme_to_checkbox(checkbox: ctk.CTkCheckBox, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkCheckBox.
    
    Args:
        checkbox: The checkbox widget to style
        theme_props: The theme properties to apply
    """
    if "fg_color" in theme_props:
        checkbox.configure(fg_color=theme_props["fg_color"])
    
    if "border_color" in theme_props:
        checkbox.configure(border_color=theme_props["border_color"])
    
    if "text_color" in theme_props:
        checkbox.configure(text_color=theme_props["text_color"])
    
    if "hover_color" in theme_props:
        checkbox.configure(hover_color=theme_props["hover_color"])


def apply_theme_to_slider(slider: ctk.CTkSlider, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkSlider.
    
    Args:
        slider: The slider widget to style
        theme_props: The theme properties to apply
    """
    if "fg_color" in theme_props:
        slider.configure(fg_color=theme_props["fg_color"])
    
    if "progress_color" in theme_props:
        slider.configure(progress_color=theme_props["progress_color"])
    
    if "button_color" in theme_props:
        slider.configure(button_color=theme_props["button_color"])
    
    if "button_hover_color" in theme_props:
        slider.configure(button_hover_color=theme_props["button_hover_color"])


# Widget type to theme application function mapping
WIDGET_THEME_MAPPERS = {
    ctk.CTkButton: apply_theme_to_button,
    ctk.CTkFrame: apply_theme_to_frame,
    ctk.CTkLabel: apply_theme_to_label,
    ctk.CTkEntry: apply_theme_to_entry,
    ctk.CTkCheckBox: apply_theme_to_checkbox,
    ctk.CTkSlider: apply_theme_to_slider,
    # Add more widget types as needed
}


def apply_theme_to_widget(widget: Any, theme_name: str, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a widget based on its type.
    
    Args:
        widget: The widget to style
        theme_name: The name of the theme
        theme_props: The theme properties to apply
    """
    widget_type = type(widget)
    
    if widget_type in WIDGET_THEME_MAPPERS:
        mapper_func = WIDGET_THEME_MAPPERS[widget_type]
        mapper_func(widget, theme_props)
    else:
        # For unsupported widget types, try to apply common properties
        for prop in ["fg_color", "bg_color", "text_color", "border_color"]:
            if hasattr(widget, prop) and prop in theme_props:
                widget.configure(**{prop: theme_props[prop]})


def apply_theme_to_all_children(parent: Any, theme_name: str, theme_data: Dict[str, Any]) -> None:
    """
    Recursively apply theme properties to all children widgets.
    
    Args:
        parent: The parent widget
        theme_name: The name of the theme
        theme_data: The theme configuration data
    """
    # Apply theme to the parent widget first
    apply_theme_to_widget(parent, theme_name, theme_data.get(type(parent).__name__.lower(), {}))
    
    # Apply theme to all children widgets recursively
    for child in parent.winfo_children():
        # Get widget-specific properties or use generic ones
        widget_type = type(child).__name__.lower()
        theme_props = theme_data.get(widget_type, {})
        
        # Apply theme to this child
        apply_theme_to_widget(child, theme_name, theme_props)
        
        # Recurse into this child's children
        apply_theme_to_all_children(child, theme_name, theme_data) 