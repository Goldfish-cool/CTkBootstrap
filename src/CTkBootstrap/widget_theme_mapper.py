"""
Widget theme mapper for CTkBootstrap.

This module provides functions to apply theme properties to specific CustomTkinter widgets.
"""

from typing import Dict, Any, Optional, List, Union, Tuple
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk


# Helper function to extract a single color from a tuple
def extract_single_color(color_value: Any) -> str:
    """
    Extract a single color value from a tuple or return the color directly if it's a string.
    CustomTkinter uses color tuples (light, dark), but Tkinter expects single strings.
    
    Args:
        color_value: The color value (either a string or a tuple of strings)
        
    Returns:
        A single color string
    """
    if isinstance(color_value, tuple) and len(color_value) > 0:
        # For standard Tkinter widgets, use the first color in the tuple
        return color_value[0]
    elif isinstance(color_value, list) and len(color_value) > 0:
        # Handle list format as well
        return color_value[0]
    elif isinstance(color_value, str):
        # If the string contains spaces, it might be accidentally concatenated colors
        if ' ' in color_value and color_value.count('#') > 1:
            # Split by space and take the first valid color
            return color_value.split()[0]
        return color_value
    # Return a default if None or other unexpected type
    return color_value


# CustomTkinter Widget Mappers

def apply_theme_to_button(button: ctk.CTkButton, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkButton.
    
    Args:
        button: The button widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "hover_color", "text_color", "border_color"]:
        if prop in theme_props:
            button.configure(**{prop: theme_props[prop]})


def apply_theme_to_frame(frame: ctk.CTkFrame, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkFrame.
    
    Args:
        frame: The frame widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "border_color", "corner_radius"]:
        if prop in theme_props:
            frame.configure(**{prop: theme_props[prop]})


def apply_theme_to_label(label: ctk.CTkLabel, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkLabel.
    
    Args:
        label: The label widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "text_color", "corner_radius"]:
        if prop in theme_props:
            label.configure(**{prop: theme_props[prop]})


def apply_theme_to_entry(entry: ctk.CTkEntry, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkEntry.
    
    Args:
        entry: The entry widget to style
        theme_props: The theme properties to apply
    """
    # First apply properties to the CTkEntry container
    for prop in ["fg_color", "border_color", "text_color", "placeholder_text_color"]:
        if prop in theme_props:
            entry.configure(**{prop: theme_props[prop]})
    
    # Then directly apply text_color to the internal tk.Entry widget if it exists
    # Similar to CTkTextbox, CTkEntry contains an internal standard tk.Entry widget
    # that needs to be styled directly for text color to be applied properly
    if "text_color" in theme_props and hasattr(entry, "_entry"):
        internal_entry = entry._entry
        if isinstance(internal_entry, tk.Entry):
            text_color = extract_single_color(theme_props["text_color"])
            internal_entry.configure(fg=text_color)
            
            # Also update the cursor color to match text color if applicable
            if "cursor_color" in theme_props:
                cursor_color = extract_single_color(theme_props["cursor_color"])
            else:
                cursor_color = text_color
            internal_entry.configure(insertbackground=cursor_color)


def apply_theme_to_checkbox(checkbox: ctk.CTkCheckBox, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkCheckBox.
    
    Args:
        checkbox: The checkbox widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "border_color", "text_color", "hover_color", "checkmark_color"]:
        if prop in theme_props:
            checkbox.configure(**{prop: theme_props[prop]})


def apply_theme_to_radio_button(radio: ctk.CTkRadioButton, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkRadioButton.
    
    Args:
        radio: The radio button widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "border_color", "text_color", "hover_color"]:
        if prop in theme_props:
            radio.configure(**{prop: theme_props[prop]})


def apply_theme_to_switch(switch: ctk.CTkSwitch, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkSwitch.
    
    Args:
        switch: The switch widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "progress_color", "button_color", "button_hover_color", "text_color"]:
        if prop in theme_props:
            switch.configure(**{prop: theme_props[prop]})


def apply_theme_to_slider(slider: ctk.CTkSlider, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkSlider.
    
    Args:
        slider: The slider widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "progress_color", "button_color", "button_hover_color"]:
        if prop in theme_props:
            slider.configure(**{prop: theme_props[prop]})


def apply_theme_to_progressbar(progressbar: ctk.CTkProgressBar, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkProgressBar.
    
    Args:
        progressbar: The progress bar widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "progress_color", "border_color"]:
        if prop in theme_props:
            progressbar.configure(**{prop: theme_props[prop]})


def apply_theme_to_option_menu(option_menu: ctk.CTkOptionMenu, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkOptionMenu.
    
    Args:
        option_menu: The option menu widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "button_color", "button_hover_color", "dropdown_fg_color", 
                "dropdown_hover_color", "dropdown_text_color", "text_color"]:
        if prop in theme_props:
            option_menu.configure(**{prop: theme_props[prop]})


def apply_theme_to_combobox(combobox: ctk.CTkComboBox, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkComboBox.
    
    Args:
        combobox: The combobox widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "border_color", "button_color", "button_hover_color", 
                "dropdown_fg_color", "dropdown_hover_color", "dropdown_text_color", "text_color"]:
        if prop in theme_props:
            combobox.configure(**{prop: theme_props[prop]})


def apply_theme_to_textbox(textbox: ctk.CTkTextbox, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkTextbox.
    
    Args:
        textbox: The textbox widget to style
        theme_props: The theme properties to apply
    """
    # First apply properties to the CTkTextbox container
    for prop in ["fg_color", "border_color", "text_color", "scrollbar_button_color", 
                "scrollbar_button_hover_color"]:
        if prop in theme_props:
            textbox.configure(**{prop: theme_props[prop]})
    
    # Directly access and style the internal tk.Text widget
    if hasattr(textbox, "_textbox"):
        internal_text = textbox._textbox
        if isinstance(internal_text, tk.Text):
            # Use text_color from different possible sources, with priority:
            text_color = None
            
            # 1. Check theme_props (usually 'ctktext' in the theme)
            if "text_color" in theme_props:
                text_color = theme_props["text_color"]
            
            # 2. If no text_color in theme_props but textbox has text_color attribute
            if text_color is None and hasattr(textbox, "cget"):
                try:
                    text_color = textbox.cget("text_color")
                except:
                    pass
            
            # 3. Fallback to a default contrasting color
            if text_color is None:
                # Use a default that contrasts with the background
                bg_prop = textbox.cget("fg_color") if hasattr(textbox, "cget") else None
                if bg_prop:
                    # If bg is dark, use light text; if bg is light, use dark text
                    if isinstance(bg_prop, (list, tuple)) and len(bg_prop) > 0:
                        bg = bg_prop[1]  # Use dark mode color
                    else:
                        bg = bg_prop
                    
                    # Very simple contrast check - improve this if needed
                    if bg.startswith('#'):
                        # Convert hex to RGB and check brightness
                        try:
                            r = int(bg[1:3], 16)
                            g = int(bg[3:5], 16)
                            b = int(bg[5:7], 16)
                            brightness = (r * 299 + g * 587 + b * 114) / 1000
                            text_color = "#FFFFFF" if brightness < 128 else "#000000"
                        except:
                            text_color = "#FFFFFF"  # Default to white text
                    else:
                        text_color = "#FFFFFF"  # Default to white text
                else:
                    text_color = "#FFFFFF"  # Default to white text
            
            # Finally apply the text color
            if text_color:
                if isinstance(text_color, (list, tuple)) and len(text_color) > 0:
                    text_color = text_color[1]  # Use dark mode color
                internal_text.configure(fg=text_color)
                
                # Also update cursor color
                internal_text.configure(insertbackground=text_color)


def apply_theme_to_scrollbar(scrollbar: ctk.CTkScrollbar, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkScrollbar.
    
    Args:
        scrollbar: The scrollbar widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "button_color", "button_hover_color"]:
        if prop in theme_props:
            scrollbar.configure(**{prop: theme_props[prop]})


def apply_theme_to_scrollable_frame(scrollable_frame: ctk.CTkScrollableFrame, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkScrollableFrame.
    
    Args:
        scrollable_frame: The scrollable frame widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "border_color", "scrollbar_fg_color", "scrollbar_button_color", 
                "scrollbar_button_hover_color", "corner_radius"]:
        if prop in theme_props:
            scrollable_frame.configure(**{prop: theme_props[prop]})


def apply_theme_to_tabview(tabview: ctk.CTkTabview, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkTabview.
    
    Args:
        tabview: The tabview widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "segmented_button_fg_color", "segmented_button_selected_color",
                "segmented_button_selected_hover_color", "segmented_button_unselected_color",
                "segmented_button_unselected_hover_color", "text_color"]:
        if prop in theme_props:
            tabview.configure(**{prop: theme_props[prop]})


def apply_theme_to_segmented_button(segmented_button: ctk.CTkSegmentedButton, theme_props: Dict[str, Any]) -> None:
    """
    Apply theme properties to a CTkSegmentedButton.
    
    Args:
        segmented_button: The segmented button widget to style
        theme_props: The theme properties to apply
    """
    for prop in ["fg_color", "selected_color", "selected_hover_color", 
                "unselected_color", "unselected_hover_color", "text_color",
                "text_color_disabled"]:
        if prop in theme_props:
            segmented_button.configure(**{prop: theme_props[prop]})


# ttk Widget Mappers

def apply_theme_to_ttk_button(button: ttk.Button, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Button."""
    if "ttk_style" in theme_props:
        button.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_checkbutton(checkbutton: ttk.Checkbutton, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Checkbutton."""
    if "ttk_style" in theme_props:
        checkbutton.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_combobox(combobox: ttk.Combobox, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Combobox."""
    if "ttk_style" in theme_props:
        combobox.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_entry(entry: ttk.Entry, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Entry."""
    if "ttk_style" in theme_props:
        entry.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_frame(frame: ttk.Frame, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Frame."""
    if "ttk_style" in theme_props:
        frame.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_label(label: ttk.Label, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Label."""
    if "ttk_style" in theme_props:
        label.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_labelframe(labelframe: ttk.LabelFrame, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.LabelFrame."""
    if "ttk_style" in theme_props:
        labelframe.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_menubutton(menubutton: ttk.Menubutton, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Menubutton."""
    if "ttk_style" in theme_props:
        menubutton.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_notebook(notebook: ttk.Notebook, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Notebook."""
    if "ttk_style" in theme_props:
        notebook.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_panedwindow(panedwindow: ttk.PanedWindow, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.PanedWindow."""
    if "ttk_style" in theme_props:
        panedwindow.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_progressbar(progressbar: ttk.Progressbar, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Progressbar."""
    if "ttk_style" in theme_props:
        progressbar.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_radiobutton(radiobutton: ttk.Radiobutton, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Radiobutton."""
    if "ttk_style" in theme_props:
        radiobutton.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_scale(scale: ttk.Scale, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Scale."""
    if "ttk_style" in theme_props:
        scale.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_scrollbar(scrollbar: ttk.Scrollbar, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Scrollbar."""
    if "ttk_style" in theme_props:
        scrollbar.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_separator(separator: ttk.Separator, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Separator."""
    if "ttk_style" in theme_props:
        separator.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_sizegrip(sizegrip: ttk.Sizegrip, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Sizegrip."""
    if "ttk_style" in theme_props:
        sizegrip.configure(style=theme_props["ttk_style"])


def apply_theme_to_ttk_treeview(treeview: ttk.Treeview, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a ttk.Treeview."""
    if "ttk_style" in theme_props:
        treeview.configure(style=theme_props["ttk_style"])


# Standard Tkinter Widget Mappers

def apply_theme_to_tk_button(button: tk.Button, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Button."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("activebackground", "active_bg_color"),
        ("activeforeground", "active_text_color")
    ]:
        if theme_prop in theme_props:
            button.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_canvas(canvas: tk.Canvas, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Canvas."""
    if "bg_color" in theme_props:
        canvas.configure(bg=extract_single_color(theme_props["bg_color"]))


def apply_theme_to_tk_checkbutton(checkbutton: tk.Checkbutton, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Checkbutton."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("activebackground", "active_bg_color"),
        ("activeforeground", "active_text_color"),
        ("selectcolor", "select_color")
    ]:
        if theme_prop in theme_props:
            checkbutton.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_entry(entry: tk.Entry, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Entry."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("insertbackground", "cursor_color")
    ]:
        if theme_prop in theme_props:
            entry.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_frame(frame: tk.Frame, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Frame."""
    if "bg_color" in theme_props:
        frame.configure(bg=extract_single_color(theme_props["bg_color"]))


def apply_theme_to_tk_label(label: tk.Label, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Label."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color")
    ]:
        if theme_prop in theme_props:
            label.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_listbox(listbox: tk.Listbox, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Listbox."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("selectbackground", "select_bg_color"),
        ("selectforeground", "select_text_color")
    ]:
        if theme_prop in theme_props:
            listbox.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_menu(menu: tk.Menu, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Menu."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("activebackground", "active_bg_color"),
        ("activeforeground", "active_text_color")
    ]:
        if theme_prop in theme_props:
            menu.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_menubutton(menubutton: tk.Menubutton, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Menubutton."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("activebackground", "active_bg_color"),
        ("activeforeground", "active_text_color")
    ]:
        if theme_prop in theme_props:
            menubutton.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_message(message: tk.Message, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Message."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color")
    ]:
        if theme_prop in theme_props:
            message.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_radiobutton(radiobutton: tk.Radiobutton, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Radiobutton."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("activebackground", "active_bg_color"),
        ("activeforeground", "active_text_color"),
        ("selectcolor", "select_color")
    ]:
        if theme_prop in theme_props:
            radiobutton.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_scale(scale: tk.Scale, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Scale."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("activebackground", "active_bg_color"),
        ("troughcolor", "trough_color")
    ]:
        if theme_prop in theme_props:
            scale.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_scrollbar(scrollbar: tk.Scrollbar, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Scrollbar."""
    for prop, theme_prop in [
        ("bg", "bg_color"),
        ("activebackground", "active_bg_color"),
        ("troughcolor", "trough_color")
    ]:
        if theme_prop in theme_props:
            scrollbar.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_spinbox(spinbox: tk.Spinbox, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Spinbox."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("buttonbackground", "button_bg_color"),
        ("selectbackground", "select_bg_color"),
        ("selectforeground", "select_text_color")
    ]:
        if theme_prop in theme_props:
            spinbox.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_text(text: tk.Text, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Text."""
    for prop, theme_prop in [
        ("bg", "bg_color"), 
        ("fg", "text_color"),
        ("insertbackground", "cursor_color"),
        ("selectbackground", "select_bg_color"),
        ("selectforeground", "select_text_color")
    ]:
        if theme_prop in theme_props:
            text.configure(**{prop: extract_single_color(theme_props[theme_prop])})


def apply_theme_to_tk_toplevel(toplevel: tk.Toplevel, theme_props: Dict[str, Any]) -> None:
    """Apply theme properties to a tk.Toplevel."""
    if "bg_color" in theme_props:
        toplevel.configure(bg=extract_single_color(theme_props["bg_color"]))


# Widget type to theme application function mapping
WIDGET_THEME_MAPPERS = {
    # CustomTkinter Widgets
    ctk.CTkButton: apply_theme_to_button,
    ctk.CTkFrame: apply_theme_to_frame,
    ctk.CTkLabel: apply_theme_to_label,
    ctk.CTkEntry: apply_theme_to_entry,
    ctk.CTkCheckBox: apply_theme_to_checkbox,
    ctk.CTkRadioButton: apply_theme_to_radio_button,
    ctk.CTkSwitch: apply_theme_to_switch,
    ctk.CTkSlider: apply_theme_to_slider,
    ctk.CTkProgressBar: apply_theme_to_progressbar,
    ctk.CTkOptionMenu: apply_theme_to_option_menu,
    ctk.CTkComboBox: apply_theme_to_combobox,
    ctk.CTkTextbox: apply_theme_to_textbox,
    ctk.CTkScrollbar: apply_theme_to_scrollbar,
    ctk.CTkScrollableFrame: apply_theme_to_scrollable_frame,
    ctk.CTkTabview: apply_theme_to_tabview,
    ctk.CTkSegmentedButton: apply_theme_to_segmented_button,
    
    # ttk Widgets
    ttk.Button: apply_theme_to_ttk_button,
    ttk.Checkbutton: apply_theme_to_ttk_checkbutton,
    ttk.Combobox: apply_theme_to_ttk_combobox,
    ttk.Entry: apply_theme_to_ttk_entry,
    ttk.Frame: apply_theme_to_ttk_frame,
    ttk.Label: apply_theme_to_ttk_label,
    ttk.LabelFrame: apply_theme_to_ttk_labelframe,
    ttk.Menubutton: apply_theme_to_ttk_menubutton,
    ttk.Notebook: apply_theme_to_ttk_notebook,
    ttk.PanedWindow: apply_theme_to_ttk_panedwindow,
    ttk.Progressbar: apply_theme_to_ttk_progressbar,
    ttk.Radiobutton: apply_theme_to_ttk_radiobutton,
    ttk.Scale: apply_theme_to_ttk_scale,
    ttk.Scrollbar: apply_theme_to_ttk_scrollbar,
    ttk.Separator: apply_theme_to_ttk_separator,
    ttk.Sizegrip: apply_theme_to_ttk_sizegrip,
    ttk.Treeview: apply_theme_to_ttk_treeview,
    
    # Standard Tkinter Widgets
    tk.Button: apply_theme_to_tk_button,
    tk.Canvas: apply_theme_to_tk_canvas,
    tk.Checkbutton: apply_theme_to_tk_checkbutton,
    tk.Entry: apply_theme_to_tk_entry,
    tk.Frame: apply_theme_to_tk_frame,
    tk.Label: apply_theme_to_tk_label,
    tk.Listbox: apply_theme_to_tk_listbox,
    tk.Menu: apply_theme_to_tk_menu,
    tk.Menubutton: apply_theme_to_tk_menubutton,
    tk.Message: apply_theme_to_tk_message,
    tk.Radiobutton: apply_theme_to_tk_radiobutton,
    tk.Scale: apply_theme_to_tk_scale,
    tk.Scrollbar: apply_theme_to_tk_scrollbar,
    tk.Spinbox: apply_theme_to_tk_spinbox,
    tk.Text: apply_theme_to_tk_text,
    tk.Toplevel: apply_theme_to_tk_toplevel,
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
        try:
            # For CTk widgets
            for prop in ["fg_color", "text_color", "border_color", "button_color"]:
                if hasattr(widget, prop) and prop in theme_props:
                    widget.configure(**{prop: theme_props[prop]})
            
            # For ttk widgets
            if "ttk_style" in theme_props and hasattr(widget, "configure"):
                widget.configure(style=theme_props["ttk_style"])
            
            # For tk widgets
            if "bg_color" in theme_props and hasattr(widget, "configure"):
                if hasattr(widget, "configure"):
                    widget.configure(bg=extract_single_color(theme_props["bg_color"]))
                
            if "text_color" in theme_props and hasattr(widget, "configure"):
                if hasattr(widget, "configure"):
                    widget.configure(fg=extract_single_color(theme_props["text_color"]))
        except Exception:
            # Ignore configuration errors for unsupported widgets
            pass


def directly_update_text_widgets_colors(parent, theme_name):
    """
    A solution to force update text colors for all CTkTextbox and CTkEntry widgets.
    This function recursively finds all text widgets and applies the appropriate text color
    based on the current theme and appearance mode.
    
    Args:
        parent: The parent widget to recursively search for text widgets
        theme_name: The current theme name
    """
    if not hasattr(parent, "winfo_children"):
        return
    
    try:
        from CTkBootstrap.themes import THEMES
    except ImportError:
        # Fallback if we can't import the themes
        # Get the current appearance mode
        mode = ctk.get_appearance_mode()
        
        # Set appropriate colors based on appearance mode
        if mode == "Dark":
            text_color = "#DCE4EE"  # Light color for dark mode
        else:
            text_color = "#1E1E1E"  # Dark color for light mode
            
        # Process all children with the fallback color
        _update_text_widgets_with_color(parent, text_color)
        return
    
    # If we have themes imported, try to get colors from theme
    if theme_name in THEMES:
        theme_data = THEMES[theme_name]
        text_color = None
        
        # Try to get text color from different possible theme properties
        for widget_key in ["ctktext", "ctktextbox", "ctkentry"]:
            if widget_key in theme_data and "text_color" in theme_data[widget_key]:
                theme_text_color = theme_data[widget_key]["text_color"]
                if theme_text_color:
                    text_color = theme_text_color
                    break
        
        # If no specific text color found in the theme
        if text_color is None:
            # Try to get from general colors
            colors = theme_data.get("colors", {})
            if "text" in colors:
                text_color = colors["text"]
            elif "primary-text" in colors:
                text_color = colors["primary-text"]
            elif "content" in colors:
                text_color = colors["content"]
            
        # If we found a text color in the theme, use it
        if text_color:
            # Extract single color if it's a tuple/list
            text_color = extract_single_color(text_color)
            _update_text_widgets_with_color(parent, text_color)
            return
    
    # Fallback - use appearance mode-based colors
    mode = ctk.get_appearance_mode()
    if mode == "Dark":
        text_color = "#DCE4EE"  # Light color for dark mode
    else:
        text_color = "#1E1E1E"  # Dark color for light mode
    
    _update_text_widgets_with_color(parent, text_color)


def _update_text_widgets_with_color(parent, text_color):
    """
    Helper function to update text widgets with a specific color.
    
    Args:
        parent: The parent widget to recursively search for text widgets
        text_color: The color to apply to text widgets
    """
    if not hasattr(parent, "winfo_children"):
        return
        
    for child in parent.winfo_children():
        # Handle CTkTextbox widgets
        if isinstance(child, ctk.CTkTextbox) and hasattr(child, "_textbox"):
            internal_text = child._textbox
            if isinstance(internal_text, tk.Text):
                # Apply text color directly to internal text widget
                internal_text.configure(fg=text_color)
                internal_text.configure(insertbackground=text_color)
        
        # Handle CTkEntry widgets
        elif isinstance(child, ctk.CTkEntry) and hasattr(child, "_entry"):
            internal_entry = child._entry
            if isinstance(internal_entry, tk.Entry):
                # Apply text color directly to internal entry widget
                internal_entry.configure(fg=text_color)
                internal_entry.configure(insertbackground=text_color)
        
        # Recursively process this child's children
        _update_text_widgets_with_color(child, text_color)


def apply_theme_to_all_children(parent, theme_name, theme_data):
    """
    Apply theme properties to a parent widget and all its children recursively.
    
    Args:
        parent: The parent widget to apply theme to and all its children
        theme_name: The name of the theme to apply
        theme_data: The theme data containing widget properties
    """
    # First apply theme to the parent widget
    apply_theme_to_widget(parent, theme_name, theme_data)
    
    # Then apply theme to all children recursively
    if hasattr(parent, "winfo_children"):
        for child in parent.winfo_children():
            # Get the widget type
            widget_type = type(child).__name__.lower()
            
            # Convert CustomTkinter widget type to theme key format
            if widget_type.startswith("ctk"):
                theme_key = widget_type
            else:
                theme_key = widget_type
            
            # Get specific properties for this widget type
            widget_props = theme_data.get(theme_key, {})
            
            # Apply theme to this child
            apply_theme_to_widget(child, theme_name, widget_props)
            
            # Recursively apply theme to this child's children
            apply_theme_to_all_children(child, theme_name, theme_data)
    
    # After all the standard theme application, directly update text widgets
    # to ensure colors are applied correctly to internal tk widgets
    directly_update_text_widgets_colors(parent, theme_name)


def configure_ttk_styles(root: Union[tk.Tk, tk.Toplevel, ctk.CTk], theme_name: str, theme_data: Dict[str, Any]) -> None:
    """
    Configure ttk styles for the current theme.
    
    Args:
        root: The root window
        theme_name: The name of the theme
        theme_data: The theme configuration data
    """
    if "ttk" not in theme_data:
        return
    
    style = ttk.Style(root)
    
    # Configure the ttk theme if specified
    if "ttk_theme" in theme_data:
        try:
            style.theme_use(theme_data["ttk_theme"])
        except tk.TclError:
            # If the theme doesn't exist, use the default theme
            pass
    
    # Apply ttk theme properties
    ttk_props = theme_data.get("ttk", {})
    processed_props = {}
    
    # Process ttk properties to extract single colors from tuples
    for prop, value in ttk_props.items():
        processed_props[prop] = extract_single_color(value)
    
    # Configure the ttk theme
    style.configure(".", **processed_props)
    
    # Apply custom styles if available
    if "ttk_styles" in theme_data:
        for style_name, style_props in theme_data["ttk_styles"].items():
            # Process style properties to extract single colors
            processed_style_props = {}
            for prop, value in style_props.items():
                processed_style_props[prop] = extract_single_color(value)
            
            style.configure(style_name, **processed_style_props) 