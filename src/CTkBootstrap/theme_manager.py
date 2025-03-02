"""
CTkBootstrap ThemeManager - A simplified theme manager for CTkBootstrap

This module provides an easy-to-use interface for applying and managing themes
with CustomTkinter. It handles the complexities of theme application and provides
a simple API for developers.
"""

import customtkinter as ctk
from typing import Dict, List, Any, Optional, Union, Tuple
from .themes import THEMES
from . import theme_loader


class ThemeManager:
    """
    A simplified theme manager for CTkBootstrap that makes theme application easy.
    
    This class provides direct access to theme colors and a simple API for applying
    themes to widgets and windows.
    """
    
    def __init__(self, theme_name: str = "darkly"):
        """
        Initialize the theme manager with a specified theme.
        
        Args:
            theme_name: The name of the theme to use (default: "darkly")
        """
        self._theme_name = theme_name.lower()
        self._theme = self._get_theme_dict(self._theme_name)
        self._colors = self._theme.get("colors", {})
        self._appearance_mode = self._theme.get("appearance_mode", "dark")
        
        # Set appearance mode globally
        ctk.set_appearance_mode(self._appearance_mode)
    
    @property
    def theme_name(self) -> str:
        """Get the current theme name"""
        return self._theme_name
    
    @property
    def appearance_mode(self) -> str:
        """Get the current appearance mode (light/dark)"""
        return self._appearance_mode
    
    @property
    def available_themes(self) -> List[str]:
        """Get a list of all available themes"""
        return list(THEMES.keys())
    
    @property
    def colors(self) -> Dict[str, str]:
        """Get all colors for the current theme"""
        return self._colors
    
    # Direct access to common theme colors as properties
    @property
    def primary(self) -> str:
        """Get the primary color"""
        return self._colors.get("primary", "#375A7F")
    
    @property
    def secondary(self) -> str:
        """Get the secondary color"""
        return self._colors.get("secondary", "#444444")
    
    @property
    def success(self) -> str:
        """Get the success color"""
        return self._colors.get("success", "#00BC8C")
    
    @property
    def danger(self) -> str:
        """Get the danger color"""
        return self._colors.get("danger", "#E74C3C")
    
    @property
    def warning(self) -> str:
        """Get the warning color"""
        return self._colors.get("warning", "#F39C12")
    
    @property
    def info(self) -> str:
        """Get the info color"""
        return self._colors.get("info", "#3498DB")
    
    @property
    def light(self) -> str:
        """Get the light color"""
        return self._colors.get("light", "#ADB5BD")
    
    @property
    def dark(self) -> str:
        """Get the dark color"""
        return self._colors.get("dark", "#303030")
    
    def get_color(self, color_name: str, fallback: str = None) -> str:
        """
        Get a specific color from the theme.
        
        Args:
            color_name: The name of the color to get
            fallback: A fallback color to use if the requested color is not found
            
        Returns:
            The color value as a hex string
        """
        return self._colors.get(color_name, fallback)
    
    def change_theme(self, theme_name: str) -> None:
        """
        Change the current theme.
        
        Args:
            theme_name: The name of the theme to use
        """
        theme_name = theme_name.lower()
        if theme_name not in THEMES:
            valid_themes = ", ".join(self.available_themes)
            raise ValueError(f"Invalid theme: {theme_name}. Valid themes are: {valid_themes}")
        
        self._theme_name = theme_name
        self._theme = self._get_theme_dict(theme_name)
        self._colors = self._theme.get("colors", {})
        self._appearance_mode = self._theme.get("appearance_mode", "dark")
        
        # Set appearance mode globally
        ctk.set_appearance_mode(self._appearance_mode)
    
    def apply_theme_to_widget(self, widget: ctk.CTkBaseClass) -> None:
        """
        Apply the current theme to a single widget.
        
        This method detects the widget type and applies the appropriate theme settings.
        
        Args:
            widget: The CustomTkinter widget to apply the theme to
        """
        widget_type = type(widget).__name__
        
        # Get appropriate theme properties based on widget type
        if isinstance(widget, ctk.CTkButton):
            self._apply_button_theme(widget)
        elif isinstance(widget, ctk.CTkEntry):
            self._apply_entry_theme(widget)
        elif isinstance(widget, ctk.CTkTextbox):
            self._apply_textbox_theme(widget)
        elif isinstance(widget, ctk.CTkCheckBox):
            self._apply_checkbox_theme(widget)
        elif isinstance(widget, ctk.CTkRadioButton):
            self._apply_radiobutton_theme(widget)
        elif isinstance(widget, ctk.CTkSwitch):
            self._apply_switch_theme(widget)
        elif isinstance(widget, ctk.CTkSlider):
            self._apply_slider_theme(widget)
        elif isinstance(widget, ctk.CTkProgressBar):
            self._apply_progressbar_theme(widget)
        elif isinstance(widget, ctk.CTkOptionMenu):
            self._apply_optionmenu_theme(widget)
        elif isinstance(widget, ctk.CTkComboBox):
            self._apply_combobox_theme(widget)
        elif isinstance(widget, ctk.CTkFrame):
            self._apply_frame_theme(widget)
        elif isinstance(widget, ctk.CTkTabview):
            self._apply_tabview_theme(widget)
        elif isinstance(widget, ctk.CTkSegmentedButton):
            self._apply_segmentedbutton_theme(widget)
        elif isinstance(widget, ctk.CTkScrollableFrame):
            self._apply_scrollableframe_theme(widget)
        elif isinstance(widget, ctk.CTkLabel):
            self._apply_label_theme(widget)
    
    def apply_theme_to_all_widgets(self, root: Union[ctk.CTk, ctk.CTkToplevel, ctk.CTkFrame]) -> None:
        """
        Apply the current theme to all widgets in a window or frame.
        
        This method recursively applies theme settings to all CustomTkinter widgets.
        
        Args:
            root: The root window or frame containing widgets to theme
        """
        # First apply theme to the root itself if it's a CTk widget
        if isinstance(root, ctk.CTkBaseClass):
            self.apply_theme_to_widget(root)
        
        # Then recursively apply to all children
        for child in root.winfo_children():
            if isinstance(child, ctk.CTkBaseClass):
                self.apply_theme_to_widget(child)
            
            # Recursively apply to children of this widget
            if hasattr(child, "winfo_children") and callable(getattr(child, "winfo_children")):
                self.apply_theme_to_all_widgets(child)
    
    def create_themed_button(self, 
                            master: Any, 
                            text: str = "", 
                            command: callable = None, 
                            **kwargs) -> ctk.CTkButton:
        """
        Create a button with the current theme applied.
        
        Args:
            master: The parent widget
            text: The button text
            command: The function to call when the button is clicked
            **kwargs: Additional arguments to pass to CTkButton constructor
            
        Returns:
            A themed CTkButton widget
        """
        button = ctk.CTkButton(master, text=text, command=command, **kwargs)
        self._apply_button_theme(button)
        return button
    
    def create_themed_entry(self, 
                           master: Any, 
                           placeholder_text: str = "", 
                           **kwargs) -> ctk.CTkEntry:
        """
        Create an entry widget with the current theme applied.
        
        Args:
            master: The parent widget
            placeholder_text: The placeholder text
            **kwargs: Additional arguments to pass to CTkEntry constructor
            
        Returns:
            A themed CTkEntry widget
        """
        entry = ctk.CTkEntry(master, placeholder_text=placeholder_text, **kwargs)
        self._apply_entry_theme(entry)
        return entry
    
    def create_themed_textbox(self, 
                             master: Any, 
                             **kwargs) -> ctk.CTkTextbox:
        """
        Create a textbox with the current theme applied.
        
        Args:
            master: The parent widget
            **kwargs: Additional arguments to pass to CTkTextbox constructor
            
        Returns:
            A themed CTkTextbox widget
        """
        textbox = ctk.CTkTextbox(master, **kwargs)
        self._apply_textbox_theme(textbox)
        return textbox
    
    def create_themed_frame(self, 
                           master: Any, 
                           **kwargs) -> ctk.CTkFrame:
        """
        Create a frame with the current theme applied.
        
        Args:
            master: The parent widget
            **kwargs: Additional arguments to pass to CTkFrame constructor
            
        Returns:
            A themed CTkFrame widget
        """
        frame = ctk.CTkFrame(master, **kwargs)
        self._apply_frame_theme(frame)
        return frame
    
    def create_primary_button(self, 
                             master: Any, 
                             text: str = "", 
                             command: callable = None, 
                             **kwargs) -> ctk.CTkButton:
        """
        Create a button with the primary theme color.
        
        Args:
            master: The parent widget
            text: The button text
            command: The function to call when the button is clicked
            **kwargs: Additional arguments to pass to CTkButton constructor
            
        Returns:
            A CTkButton widget with primary color
        """
        button = ctk.CTkButton(master, text=text, command=command, **kwargs)
        button.configure(
            fg_color=[self.primary, self.primary],
            hover_color=[self.info, self.info],
            text_color=["#FFFFFF", "#FFFFFF"]
        )
        return button
    
    def create_secondary_button(self, 
                               master: Any, 
                               text: str = "", 
                               command: callable = None, 
                               **kwargs) -> ctk.CTkButton:
        """
        Create a button with the secondary theme color.
        
        Args:
            master: The parent widget
            text: The button text
            command: The function to call when the button is clicked
            **kwargs: Additional arguments to pass to CTkButton constructor
            
        Returns:
            A CTkButton widget with secondary color
        """
        button = ctk.CTkButton(master, text=text, command=command, **kwargs)
        button.configure(
            fg_color=[self.secondary, self.secondary],
            hover_color=[self.info, self.info],
            text_color=["#FFFFFF", "#FFFFFF"]
        )
        return button
    
    def create_success_button(self, 
                             master: Any, 
                             text: str = "", 
                             command: callable = None, 
                             **kwargs) -> ctk.CTkButton:
        """
        Create a button with the success theme color.
        
        Args:
            master: The parent widget
            text: The button text
            command: The function to call when the button is clicked
            **kwargs: Additional arguments to pass to CTkButton constructor
            
        Returns:
            A CTkButton widget with success color
        """
        button = ctk.CTkButton(master, text=text, command=command, **kwargs)
        text_color = ["#000000", "#000000"] if self.is_dark_color(self.success) else ["#FFFFFF", "#FFFFFF"]
        button.configure(
            fg_color=[self.success, self.success],
            hover_color=[self.info, self.info],
            text_color=text_color
        )
        return button
    
    def create_danger_button(self, 
                            master: Any, 
                            text: str = "", 
                            command: callable = None, 
                            **kwargs) -> ctk.CTkButton:
        """
        Create a button with the danger theme color.
        
        Args:
            master: The parent widget
            text: The button text
            command: The function to call when the button is clicked
            **kwargs: Additional arguments to pass to CTkButton constructor
            
        Returns:
            A CTkButton widget with danger color
        """
        button = ctk.CTkButton(master, text=text, command=command, **kwargs)
        text_color = ["#000000", "#000000"] if self.is_dark_color(self.danger) else ["#FFFFFF", "#FFFFFF"]
        button.configure(
            fg_color=[self.danger, self.danger],
            hover_color=[self.warning, self.warning],
            text_color=text_color
        )
        return button
    
    def create_warning_button(self, 
                             master: Any, 
                             text: str = "", 
                             command: callable = None, 
                             **kwargs) -> ctk.CTkButton:
        """
        Create a button with the warning theme color.
        
        Args:
            master: The parent widget
            text: The button text
            command: The function to call when the button is clicked
            **kwargs: Additional arguments to pass to CTkButton constructor
            
        Returns:
            A CTkButton widget with warning color
        """
        button = ctk.CTkButton(master, text=text, command=command, **kwargs)
        text_color = ["#000000", "#000000"] if self.is_dark_color(self.warning) else ["#FFFFFF", "#FFFFFF"]
        button.configure(
            fg_color=[self.warning, self.warning],
            hover_color=[self.info, self.info],
            text_color=text_color
        )
        return button
    
    def create_info_button(self, 
                          master: Any, 
                          text: str = "", 
                          command: callable = None, 
                          **kwargs) -> ctk.CTkButton:
        """
        Create a button with the info theme color.
        
        Args:
            master: The parent widget
            text: The button text
            command: The function to call when the button is clicked
            **kwargs: Additional arguments to pass to CTkButton constructor
            
        Returns:
            A CTkButton widget with info color
        """
        button = ctk.CTkButton(master, text=text, command=command, **kwargs)
        text_color = ["#000000", "#000000"] if self.is_dark_color(self.info) else ["#FFFFFF", "#FFFFFF"]
        button.configure(
            fg_color=[self.info, self.info],
            hover_color=[self.primary, self.primary],
            text_color=text_color
        )
        return button
    
    def is_dark_color(self, color_hex):
        """
        Determine if a color is light or dark to set text contrast appropriately.
        
        Args:
            color_hex: The color in hex format (e.g., "#FFFFFF")
            
        Returns:
            True if the color is light (bright), False if the color is dark
        """
        # Remove # if present
        color_hex = color_hex.lstrip("#")
        
        # Convert to RGB
        try:
            r, g, b = int(color_hex[0:2], 16), int(color_hex[2:4], 16), int(color_hex[4:6], 16)
            
            # Calculate perceived brightness (ITU-R BT.709)
            brightness = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
            
            # Return True if the color is light (brightness > 0.5)
            return brightness > 0.5
        except (ValueError, IndexError):
            # If the color can't be parsed, assume it's dark
            return False
    
    def _get_theme_dict(self, theme_name: str) -> Dict[str, Any]:
        """Get the theme dictionary for a given theme name"""
        if theme_name not in THEMES:
            valid_themes = ", ".join(list(THEMES.keys()))
            raise ValueError(f"Invalid theme: {theme_name}. Valid themes are: {valid_themes}")
        return THEMES[theme_name]
    
    def _get_widget_theme_props(self, widget_type: str) -> Dict[str, Any]:
        """Get theme properties for a specific widget type"""
        return self._theme.get(widget_type.lower(), {})
    
    def _apply_button_theme(self, button: ctk.CTkButton) -> None:
        """Apply theme to a CTkButton widget"""
        button_props = self._get_widget_theme_props("button")
        
        # Get theme properties or use fallbacks
        fg_color = button_props.get("fg_color", [self.primary, self.primary])
        hover_color = button_props.get("hover_color", [self.info, self.info])
        text_color = button_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme
        button.configure(
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color
        )
    
    def _apply_entry_theme(self, entry: ctk.CTkEntry) -> None:
        """Apply theme to a CTkEntry widget"""
        entry_props = self._get_widget_theme_props("entry")
        
        # Get theme properties or use fallbacks
        fg_color = entry_props.get("fg_color", ["#343638", "#343638"])
        border_color = entry_props.get("border_color", [self.info, self.info])
        text_color = entry_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme
        entry.configure(
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color
        )
    
    def _apply_textbox_theme(self, textbox: ctk.CTkTextbox) -> None:
        """Apply theme to a CTkTextbox widget"""
        textbox_props = self._get_widget_theme_props("textbox")
        # Fall back to entry properties if textbox properties are not defined
        entry_props = self._get_widget_theme_props("entry")
        
        # Get theme properties or use fallbacks
        fg_color = textbox_props.get("fg_color", entry_props.get("fg_color", ["#343638", "#343638"]))
        border_color = textbox_props.get("border_color", entry_props.get("border_color", [self.info, self.info]))
        text_color = textbox_props.get("text_color", entry_props.get("text_color", ["#FFFFFF", "#FFFFFF"]))
        
        # Apply theme
        textbox.configure(
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color
        )
        
        # Apply theme to the internal text widget
        try:
            internal_text = textbox._textbox
            if internal_text:
                internal_text.configure(
                    fg=text_color[1] if self._appearance_mode == "dark" else text_color[0]
                )
        except (AttributeError, IndexError):
            pass
    
    def _apply_checkbox_theme(self, checkbox: ctk.CTkCheckBox) -> None:
        """Apply theme to a CTkCheckBox widget"""
        checkbox_props = self._get_widget_theme_props("checkbox")
        
        # Get theme properties or use fallbacks
        fg_color = checkbox_props.get("fg_color", ["#343638", "#343638"])
        border_color = checkbox_props.get("border_color", [self.info, self.info])
        checkmark_color = checkbox_props.get("checkmark_color", ["#FFFFFF", "#FFFFFF"])
        hover_color = checkbox_props.get("hover_color", [self.primary, self.primary])
        text_color = checkbox_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme
        checkbox.configure(
            fg_color=fg_color,
            border_color=border_color,
            checkmark_color=checkmark_color,
            hover_color=hover_color,
            text_color=text_color
        )
    
    def _apply_radiobutton_theme(self, radiobutton: ctk.CTkRadioButton) -> None:
        """Apply theme to a CTkRadioButton widget"""
        radiobutton_props = self._get_widget_theme_props("radio_button")
        checkbox_props = self._get_widget_theme_props("checkbox")
        
        # Get theme properties or use fallbacks from checkbox properties
        fg_color = radiobutton_props.get("fg_color", checkbox_props.get("fg_color", ["#343638", "#343638"]))
        border_color = radiobutton_props.get("border_color", checkbox_props.get("border_color", [self.info, self.info]))
        hover_color = radiobutton_props.get("hover_color", checkbox_props.get("hover_color", [self.primary, self.primary]))
        text_color = radiobutton_props.get("text_color", checkbox_props.get("text_color", ["#FFFFFF", "#FFFFFF"]))
        
        # Apply theme
        radiobutton.configure(
            fg_color=fg_color,
            border_color=border_color,
            hover_color=hover_color,
            text_color=text_color
        )
    
    def _apply_switch_theme(self, switch: ctk.CTkSwitch) -> None:
        """Apply theme to a CTkSwitch widget"""
        switch_props = self._get_widget_theme_props("switch")
        
        # Get theme properties or use fallbacks
        fg_color = switch_props.get("fg_color", ["#343638", "#343638"])
        progress_color = switch_props.get("progress_color", [self.primary, self.primary])
        button_color = switch_props.get("button_color", ["#FFFFFF", "#FFFFFF"])
        button_hover_color = switch_props.get("button_hover_color", ["#E9ECEF", "#E9ECEF"])
        text_color = switch_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme
        switch.configure(
            fg_color=fg_color,
            progress_color=progress_color,
            button_color=button_color,
            button_hover_color=button_hover_color,
            text_color=text_color
        )
    
    def _apply_slider_theme(self, slider: ctk.CTkSlider) -> None:
        """Apply theme to a CTkSlider widget"""
        slider_props = self._get_widget_theme_props("slider")
        
        # Get theme properties or use fallbacks
        fg_color = slider_props.get("fg_color", ["#343638", "#343638"])
        progress_color = slider_props.get("progress_color", [self.primary, self.primary])
        button_color = slider_props.get("button_color", ["#FFFFFF", "#FFFFFF"])
        button_hover_color = slider_props.get("button_hover_color", ["#E9ECEF", "#E9ECEF"])
        
        # Apply theme
        slider.configure(
            fg_color=fg_color,
            progress_color=progress_color,
            button_color=button_color,
            button_hover_color=button_hover_color
        )
    
    def _apply_progressbar_theme(self, progressbar: ctk.CTkProgressBar) -> None:
        """Apply theme to a CTkProgressBar widget"""
        progressbar_props = self._get_widget_theme_props("progressbar")
        
        # Get theme properties or use fallbacks
        fg_color = progressbar_props.get("fg_color", ["#343638", "#343638"])
        progress_color = progressbar_props.get("progress_color", [self.primary, self.primary])
        
        # Apply theme
        progressbar.configure(
            fg_color=fg_color,
            progress_color=progress_color
        )
    
    def _apply_optionmenu_theme(self, optionmenu: ctk.CTkOptionMenu) -> None:
        """Apply theme to a CTkOptionMenu widget"""
        optionmenu_props = self._get_widget_theme_props("option_menu")
        
        # Get theme properties or use fallbacks
        fg_color = optionmenu_props.get("fg_color", ["#343638", "#343638"])
        button_color = optionmenu_props.get("button_color", [self.primary, self.primary])
        button_hover_color = optionmenu_props.get("button_hover_color", [self.info, self.info])
        text_color = optionmenu_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        dropdown_fg_color = optionmenu_props.get("dropdown_fg_color", [self.dark, self.dark])
        dropdown_hover_color = optionmenu_props.get("dropdown_hover_color", [self.primary, self.primary])
        dropdown_text_color = optionmenu_props.get("dropdown_text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme
        optionmenu.configure(
            fg_color=fg_color,
            button_color=button_color,
            button_hover_color=button_hover_color,
            text_color=text_color,
            dropdown_fg_color=dropdown_fg_color,
            dropdown_hover_color=dropdown_hover_color,
            dropdown_text_color=dropdown_text_color
        )
    
    def _apply_combobox_theme(self, combobox: ctk.CTkComboBox) -> None:
        """Apply theme to a CTkComboBox widget"""
        combobox_props = self._get_widget_theme_props("combobox")
        
        # Get theme properties or use fallbacks
        fg_color = combobox_props.get("fg_color", ["#343638", "#343638"])
        border_color = combobox_props.get("border_color", [self.info, self.info])
        button_color = combobox_props.get("button_color", [self.primary, self.primary])
        button_hover_color = combobox_props.get("button_hover_color", [self.info, self.info])
        text_color = combobox_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        dropdown_fg_color = combobox_props.get("dropdown_fg_color", [self.dark, self.dark])
        dropdown_hover_color = combobox_props.get("dropdown_hover_color", [self.primary, self.primary])
        dropdown_text_color = combobox_props.get("dropdown_text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme
        combobox.configure(
            fg_color=fg_color,
            border_color=border_color,
            button_color=button_color,
            button_hover_color=button_hover_color,
            text_color=text_color,
            dropdown_fg_color=dropdown_fg_color,
            dropdown_hover_color=dropdown_hover_color,
            dropdown_text_color=dropdown_text_color
        )
    
    def _apply_frame_theme(self, frame: ctk.CTkFrame) -> None:
        """Apply theme to a CTkFrame widget"""
        frame_props = self._get_widget_theme_props("frame")
        
        # Get theme properties or use fallbacks
        fg_color = frame_props.get("fg_color", ["#2B2B2B", "#2B2B2B"])
        border_color = frame_props.get("border_color", [self.info, self.info])
        
        # Apply theme
        frame.configure(
            fg_color=fg_color,
            border_color=border_color
        )
    
    def _apply_tabview_theme(self, tabview: ctk.CTkTabview) -> None:
        """Apply theme to a CTkTabview widget"""
        tabview_props = self._get_widget_theme_props("tabview")
        
        # Get theme properties or use fallbacks
        fg_color = tabview_props.get("fg_color", ["#2B2B2B", "#2B2B2B"])
        segmented_button_fg_color = tabview_props.get("segmented_button_fg_color", [self.dark, self.dark])
        segmented_button_selected_color = tabview_props.get("segmented_button_selected_color", [self.primary, self.primary])
        segmented_button_selected_hover_color = tabview_props.get("segmented_button_selected_hover_color", [self.info, self.info])
        segmented_button_unselected_color = tabview_props.get("segmented_button_unselected_color", ["#2B2B2B", "#2B2B2B"])
        segmented_button_unselected_hover_color = tabview_props.get("segmented_button_unselected_hover_color", [self.dark, self.dark])
        text_color = tabview_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme - use only compatible parameters
        try:
            # Try the full configuration first
            tabview.configure(
                fg_color=fg_color,
                segmented_button_fg_color=segmented_button_fg_color,
                segmented_button_selected_color=segmented_button_selected_color,
                segmented_button_selected_hover_color=segmented_button_selected_hover_color,
                segmented_button_unselected_color=segmented_button_unselected_color,
                segmented_button_unselected_hover_color=segmented_button_unselected_hover_color,
                text_color=text_color,
            )
        except ValueError:
            # Fall back to basic configuration if advanced parameters are not supported
            try:
                tabview.configure(
                    fg_color=fg_color,
                    text_color=text_color
                )
            except Exception as e:
                print(f"Warning: Could not fully apply theme to CTkTabview: {e}")
    
    def _apply_segmentedbutton_theme(self, segmentedbutton: ctk.CTkSegmentedButton) -> None:
        """Apply theme to a CTkSegmentedButton widget"""
        segmentedbutton_props = self._get_widget_theme_props("segmented_button")
        
        # Get theme properties or use fallbacks
        fg_color = segmentedbutton_props.get("fg_color", [self.dark, self.dark])
        selected_color = segmentedbutton_props.get("selected_color", [self.primary, self.primary])
        selected_hover_color = segmentedbutton_props.get("selected_hover_color", [self.info, self.info])
        unselected_color = segmentedbutton_props.get("unselected_color", ["#2B2B2B", "#2B2B2B"])
        unselected_hover_color = segmentedbutton_props.get("unselected_hover_color", [self.dark, self.dark])
        text_color = segmentedbutton_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme using only compatible parameters
        try:
            # Try full configuration first
            segmentedbutton.configure(
                fg_color=fg_color,
                selected_color=selected_color,
                selected_hover_color=selected_hover_color,
                unselected_color=unselected_color,
                unselected_hover_color=unselected_hover_color,
                text_color=text_color,
            )
        except ValueError:
            # Fall back to basic configuration
            try:
                segmentedbutton.configure(
                    fg_color=fg_color,
                    selected_color=selected_color,
                    text_color=text_color
                )
            except Exception as e:
                print(f"Warning: Could not fully apply theme to CTkSegmentedButton: {e}")
    
    def _apply_scrollableframe_theme(self, scrollableframe: ctk.CTkScrollableFrame) -> None:
        """Apply theme to a CTkScrollableFrame widget"""
        scrollableframe_props = self._get_widget_theme_props("scrollable_frame")
        
        # Get theme properties or use fallbacks
        fg_color = scrollableframe_props.get("fg_color", ["#2B2B2B", "#2B2B2B"])
        border_color = scrollableframe_props.get("border_color", [self.info, self.info])
        scrollbar_fg_color = scrollableframe_props.get("scrollbar_fg_color", ["#2B2B2B", "#2B2B2B"])
        scrollbar_button_color = scrollableframe_props.get("scrollbar_button_color", [self.primary, self.primary])
        scrollbar_button_hover_color = scrollableframe_props.get("scrollbar_button_hover_color", [self.info, self.info])
        
        # Apply theme
        scrollableframe.configure(
            fg_color=fg_color,
            border_color=border_color,
            scrollbar_fg_color=scrollbar_fg_color,
            scrollbar_button_color=scrollbar_button_color,
            scrollbar_button_hover_color=scrollbar_button_hover_color
        )
    
    def _apply_label_theme(self, label: ctk.CTkLabel) -> None:
        """Apply theme to a CTkLabel widget"""
        # Labels don't have specific theme properties in the theme dict, 
        # so we'll use text_color from various sources
        button_props = self._get_widget_theme_props("button")
        text_color = button_props.get("text_color", ["#FFFFFF", "#FFFFFF"])
        
        # Apply theme
        label.configure(text_color=text_color)

    @classmethod
    def add_theme_search_path(cls, path: str) -> None:
        """
        Add a directory to search for theme files.
        
        This method adds a new directory to the theme search paths list and
        automatically reloads themes from all search directories.
        
        Args:
            path: Directory path to add to the search paths
        """
        theme_loader.add_search_path(path)
        theme_loader.reload_all_themes()
    
    @classmethod
    def get_theme_search_paths(cls) -> List[str]:
        """
        Get the current theme search paths.
        
        Returns:
            A list of directory paths where themes are searched for
        """
        return theme_loader.get_search_paths()
    
    @classmethod
    def reload_themes(cls) -> Dict[str, Dict[str, Any]]:
        """
        Reload all themes from all search paths.
        
        Returns:
            A dictionary with all loaded themes
        """
        return theme_loader.reload_all_themes()
    
    @classmethod
    def load_theme_from_file(cls, file_path: str) -> Optional[str]:
        """
        Load a theme from a JSON file and add it to available themes.
        
        Args:
            file_path: Path to the JSON theme file
            
        Returns:
            The name of the loaded theme, or None if loading failed
        """
        # Extract theme name from filename (without extension)
        import os
        theme_name = os.path.splitext(os.path.basename(file_path))[0].lower()
        
        # Load theme
        theme_data = theme_loader.load_theme_from_file(file_path)
        
        if theme_data:
            # Add theme to THEMES dictionary
            THEMES[theme_name] = theme_data
            return theme_name
        
        return None
    
    @classmethod
    def load_themes_from_directory(cls, directory_path: str) -> Dict[str, Dict[str, Any]]:
        """
        Load all theme files from a directory.
        
        Args:
            directory_path: Path to the directory containing theme files
            
        Returns:
            A dictionary mapping theme names to theme definitions
        """
        return theme_loader.load_themes_from_directory(directory_path)


# Global theme manager instance for simple access
_theme_manager = None

def get_theme_manager(theme_name: str = "darkly") -> ThemeManager:
    """
    Get the global theme manager instance.
    
    Args:
        theme_name: Optional name of the theme to use (only used when creating a new instance)
        
    Returns:
        The global ThemeManager instance
    """
    global _theme_manager
    if _theme_manager is None:
        _theme_manager = ThemeManager(theme_name)
    return _theme_manager

def set_theme(theme_name: str) -> None:
    """
    Set the current theme for the application.
    
    This is a convenience function that creates or uses the global theme manager.
    
    Args:
        theme_name: The name of the theme to use
    """
    manager = get_theme_manager()
    manager.change_theme(theme_name)

def apply_theme(root: Union[ctk.CTk, ctk.CTkToplevel, ctk.CTkFrame], theme_name: str = None) -> None:
    """
    Apply a theme to all widgets in a window or frame.
    
    This is a convenience function that creates or uses the global theme manager.
    
    Args:
        root: The root window or frame containing widgets to theme
        theme_name: Optional name of the theme to use (if not provided, uses the current theme)
    """
    manager = get_theme_manager()
    if theme_name:
        manager.change_theme(theme_name)
    manager.apply_theme_to_all_widgets(root)

def get_theme_color(color_name: str, fallback: str = None) -> str:
    """
    Get a color from the current theme.
    
    This is a convenience function that creates or uses the global theme manager.
    
    Args:
        color_name: The name of the color to get
        fallback: A fallback color to use if the requested color is not found
        
    Returns:
        The color value as a hex string
    """
    manager = get_theme_manager()
    return manager.get_color(color_name, fallback)

# Convenience functions for frequently used theme colors
def get_primary_color() -> str:
    """Get the primary color from the current theme"""
    return get_theme_manager().primary

def get_secondary_color() -> str:
    """Get the secondary color from the current theme"""
    return get_theme_manager().secondary

def get_success_color() -> str:
    """Get the success color from the current theme"""
    return get_theme_manager().success

def get_danger_color() -> str:
    """Get the danger color from the current theme"""
    return get_theme_manager().danger

def get_warning_color() -> str:
    """Get the warning color from the current theme"""
    return get_theme_manager().warning

def get_info_color() -> str:
    """Get the info color from the current theme"""
    return get_theme_manager().info

# Theme loading convenience functions
def add_theme_search_path(path: str) -> None:
    """
    Add a directory to search for theme files.
    
    Args:
        path: Directory path to add to the search paths
    """
    ThemeManager.add_theme_search_path(path)

def get_theme_search_paths() -> List[str]:
    """
    Get the current theme search paths.
    
    Returns:
        A list of directory paths where themes are searched for
    """
    return ThemeManager.get_theme_search_paths()

def reload_themes() -> Dict[str, Dict[str, Any]]:
    """
    Reload all themes from all search paths.
    
    Returns:
        A dictionary with all loaded themes
    """
    return ThemeManager.reload_themes()

def load_theme_from_file(file_path: str) -> Optional[str]:
    """
    Load a theme from a JSON file and add it to available themes.
    
    Args:
        file_path: Path to the JSON theme file
        
    Returns:
        The name of the loaded theme, or None if loading failed
    """
    return ThemeManager.load_theme_from_file(file_path)

def load_themes_from_directory(directory_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Load all theme files from a directory.
    
    Args:
        directory_path: Path to the directory containing theme files
        
    Returns:
        A dictionary mapping theme names to theme definitions
    """
    return ThemeManager.load_themes_from_directory(directory_path) 