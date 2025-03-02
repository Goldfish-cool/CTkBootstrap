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
        },
        "checkbox": {
            "fg_color": ("#073642", "#073642"),
            "border_color": ("#2AA198", "#2AA198"),
            "checkmark_color": ("#FDF6E3", "#FDF6E3"),
            "hover_color": ("#B58900", "#B58900"),
            "text_color": ("#FDF6E3", "#FDF6E3")
        },
        "radio_button": {
            "fg_color": ("#073642", "#073642"),
            "border_color": ("#2AA198", "#2AA198"),
            "hover_color": ("#B58900", "#B58900"),
            "text_color": ("#FDF6E3", "#FDF6E3")
        },
        "switch": {
            "fg_color": ("#073642", "#073642"),
            "progress_color": ("#B58900", "#B58900"),
            "button_color": ("#FDF6E3", "#FDF6E3"),
            "button_hover_color": ("#EEE8D5", "#EEE8D5"),
            "text_color": ("#FDF6E3", "#FDF6E3")
        },
        "slider": {
            "fg_color": ("#073642", "#073642"),
            "progress_color": ("#B58900", "#B58900"),
            "button_color": ("#FDF6E3", "#FDF6E3"),
            "button_hover_color": ("#EEE8D5", "#EEE8D5")
        },
        "progressbar": {
            "fg_color": ("#073642", "#073642"),
            "progress_color": ("#B58900", "#B58900")
        },
        "option_menu": {
            "fg_color": ("#073642", "#073642"),
            "button_color": ("#B58900", "#B58900"),
            "button_hover_color": ("#CB4B16", "#CB4B16"),
            "text_color": ("#FDF6E3", "#FDF6E3"),
            "dropdown_fg_color": ("#002B36", "#002B36"),
            "dropdown_hover_color": ("#B58900", "#B58900"),
            "dropdown_text_color": ("#FDF6E3", "#FDF6E3")
        },
        "combobox": {
            "fg_color": ("#073642", "#073642"),
            "border_color": ("#2AA198", "#2AA198"),
            "button_color": ("#B58900", "#B58900"),
            "button_hover_color": ("#CB4B16", "#CB4B16"),
            "text_color": ("#FDF6E3", "#FDF6E3"),
            "dropdown_fg_color": ("#002B36", "#002B36"),
            "dropdown_hover_color": ("#B58900", "#B58900"),
            "dropdown_text_color": ("#FDF6E3", "#FDF6E3")
        },
        "textbox": {
            "fg_color": ("#073642", "#073642"),
            "border_color": ("#2AA198", "#2AA198"),
            "text_color": ("#FDF6E3", "#FDF6E3")
        },
        "scrollbar": {
            "fg_color": ("#073642", "#073642"),
            "button_color": ("#B58900", "#B58900"),
            "button_hover_color": ("#CB4B16", "#CB4B16")
        },
        "scrollable_frame": {
            "fg_color": ("#073642", "#073642"),
            "border_color": ("#2AA198", "#2AA198"),
            "scrollbar_fg_color": ("#073642", "#073642"),
            "scrollbar_button_color": ("#B58900", "#B58900"),
            "scrollbar_button_hover_color": ("#CB4B16", "#CB4B16")
        },
        "tabview": {
            "fg_color": ("#073642", "#073642"),
            "segmented_button_fg_color": ("#002B36", "#002B36"),
            "segmented_button_selected_color": ("#B58900", "#B58900"),
            "segmented_button_selected_hover_color": ("#CB4B16", "#CB4B16"),
            "segmented_button_unselected_color": ("#073642", "#073642"),
            "segmented_button_unselected_hover_color": ("#002B36", "#002B36"),
            "text_color": ("#FDF6E3", "#FDF6E3"),
            "selected_text_color": ("#FDF6E3", "#FDF6E3"),
            "unselected_text_color": ("#93A1A1", "#93A1A1")
        },
        "segmented_button": {
            "fg_color": ("#002B36", "#002B36"),
            "selected_color": ("#B58900", "#B58900"),
            "selected_hover_color": ("#CB4B16", "#CB4B16"),
            "unselected_color": ("#073642", "#073642"),
            "unselected_hover_color": ("#002B36", "#002B36"),
            "text_color": ("#FDF6E3", "#FDF6E3"),
            "selected_text_color": ("#FDF6E3", "#FDF6E3"),
            "unselected_text_color": ("#93A1A1", "#93A1A1")
        },
        "ttk": {
            "background": "#002B36",
            "foreground": "#FDF6E3",
            "fieldbackground": "#073642",
            "selectbackground": "#B58900",
            "selectforeground": "#FDF6E3",
            "activebackground": "#CB4B16",
            "activeforeground": "#FDF6E3",
            "disabledforeground": "#586E75",
            "bordercolor": "#2AA198",
            "insertcolor": "#FDF6E3"
        },
        "tk": {
            "background": "#002B36",
            "foreground": "#FDF6E3",
            "activebackground": "#B58900",
            "activeforeground": "#FDF6E3",
            "disabledforeground": "#586E75",
            "highlightbackground": "#073642",
            "highlightcolor": "#2AA198",
            "insertbackground": "#FDF6E3",
            "selectbackground": "#B58900",
            "selectforeground": "#FDF6E3",
            "troughcolor": "#073642"
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
            "fg_color": ("#444444", "#444444"),
            "border_color": ("#3498DB", "#3498DB")
        },
        "entry": {
            "fg_color": ("#444444", "#444444"),
            "border_color": ("#3498DB", "#3498DB"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "checkbox": {
            "fg_color": ("#444444", "#444444"),
            "border_color": ("#3498DB", "#3498DB"),
            "checkmark_color": ("#FFFFFF", "#FFFFFF"),
            "hover_color": ("#375A7F", "#375A7F"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "radio_button": {
            "fg_color": ("#444444", "#444444"),
            "border_color": ("#3498DB", "#3498DB"),
            "hover_color": ("#375A7F", "#375A7F"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "switch": {
            "fg_color": ("#444444", "#444444"),
            "progress_color": ("#375A7F", "#375A7F"),
            "button_color": ("#FFFFFF", "#FFFFFF"),
            "button_hover_color": ("#E9ECEF", "#E9ECEF"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "slider": {
            "fg_color": ("#444444", "#444444"),
            "progress_color": ("#375A7F", "#375A7F"),
            "button_color": ("#FFFFFF", "#FFFFFF"),
            "button_hover_color": ("#E9ECEF", "#E9ECEF")
        },
        "progressbar": {
            "fg_color": ("#444444", "#444444"),
            "progress_color": ("#375A7F", "#375A7F")
        },
        "option_menu": {
            "fg_color": ("#444444", "#444444"),
            "button_color": ("#375A7F", "#375A7F"),
            "button_hover_color": ("#3498DB", "#3498DB"),
            "text_color": ("#FFFFFF", "#FFFFFF"),
            "dropdown_fg_color": ("#303030", "#303030"),
            "dropdown_hover_color": ("#375A7F", "#375A7F"),
            "dropdown_text_color": ("#FFFFFF", "#FFFFFF")
        },
        "combobox": {
            "fg_color": ("#444444", "#444444"),
            "border_color": ("#3498DB", "#3498DB"),
            "button_color": ("#375A7F", "#375A7F"),
            "button_hover_color": ("#3498DB", "#3498DB"),
            "text_color": ("#FFFFFF", "#FFFFFF"),
            "dropdown_fg_color": ("#303030", "#303030"),
            "dropdown_hover_color": ("#375A7F", "#375A7F"),
            "dropdown_text_color": ("#FFFFFF", "#FFFFFF")
        },
        "textbox": {
            "fg_color": ("#444444", "#444444"),
            "border_color": ("#3498DB", "#3498DB"),
            "text_color": ("#FFFFFF", "#FFFFFF")
        },
        "scrollbar": {
            "fg_color": ("#444444", "#444444"),
            "button_color": ("#375A7F", "#375A7F"),
            "button_hover_color": ("#3498DB", "#3498DB")
        },
        "scrollable_frame": {
            "fg_color": ("#444444", "#444444"),
            "border_color": ("#3498DB", "#3498DB"),
            "scrollbar_fg_color": ("#444444", "#444444"),
            "scrollbar_button_color": ("#375A7F", "#375A7F"),
            "scrollbar_button_hover_color": ("#3498DB", "#3498DB")
        },
        "tabview": {
            "fg_color": ("#444444", "#444444"),
            "segmented_button_fg_color": ("#303030", "#303030"),
            "segmented_button_selected_color": ("#375A7F", "#375A7F"),
            "segmented_button_selected_hover_color": ("#3498DB", "#3498DB"),
            "segmented_button_unselected_color": ("#444444", "#444444"),
            "segmented_button_unselected_hover_color": ("#303030", "#303030"),
            "text_color": ("#FFFFFF", "#FFFFFF"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#ADB5BD", "#ADB5BD")
        },
        "segmented_button": {
            "fg_color": ("#303030", "#303030"),
            "selected_color": ("#375A7F", "#375A7F"),
            "selected_hover_color": ("#3498DB", "#3498DB"),
            "unselected_color": ("#444444", "#444444"),
            "unselected_hover_color": ("#303030", "#303030"),
            "text_color": ("#FFFFFF", "#FFFFFF"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#ADB5BD", "#ADB5BD")
        },
        "ttk": {
            "background": "#303030",
            "foreground": "#FFFFFF",
            "fieldbackground": "#444444",
            "selectbackground": "#375A7F",
            "selectforeground": "#FFFFFF",
            "activebackground": "#3498DB",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#6C757D",
            "bordercolor": "#3498DB",
            "insertcolor": "#FFFFFF"
        },
        "tk": {
            "background": "#303030",
            "foreground": "#FFFFFF",
            "activebackground": "#375A7F",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#6C757D",
            "highlightbackground": "#444444",
            "highlightcolor": "#3498DB",
            "insertbackground": "#FFFFFF",
            "selectbackground": "#375A7F",
            "selectforeground": "#FFFFFF",
            "troughcolor": "#444444"
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
        },
        "entry": {
            "fg_color": ("#121212", "#121212"),
            "border_color": ("#2A9FD6", "#2A9FD6"),
            "text_color": ("#ADAFAE", "#ADAFAE")
        },
        "checkbox": {
            "fg_color": ("#121212", "#121212"),
            "border_color": ("#2A9FD6", "#2A9FD6"),
            "checkmark_color": ("#FFFFFF", "#FFFFFF"),
            "hover_color": ("#2A9FD6", "#2A9FD6"),
            "text_color": ("#ADAFAE", "#ADAFAE")
        },
        "radio_button": {
            "fg_color": ("#121212", "#121212"),
            "border_color": ("#2A9FD6", "#2A9FD6"),
            "hover_color": ("#2A9FD6", "#2A9FD6"),
            "text_color": ("#ADAFAE", "#ADAFAE")
        },
        "switch": {
            "fg_color": ("#121212", "#121212"),
            "progress_color": ("#2A9FD6", "#2A9FD6"),
            "button_color": ("#FFFFFF", "#FFFFFF"),
            "button_hover_color": ("#ADAFAE", "#ADAFAE"),
            "text_color": ("#ADAFAE", "#ADAFAE")
        },
        "slider": {
            "fg_color": ("#121212", "#121212"),
            "progress_color": ("#2A9FD6", "#2A9FD6"),
            "button_color": ("#FFFFFF", "#FFFFFF"),
            "button_hover_color": ("#ADAFAE", "#ADAFAE")
        },
        "progressbar": {
            "fg_color": ("#121212", "#121212"),
            "progress_color": ("#2A9FD6", "#2A9FD6")
        },
        "option_menu": {
            "fg_color": ("#121212", "#121212"),
            "button_color": ("#2A9FD6", "#2A9FD6"),
            "button_hover_color": ("#9933CC", "#9933CC"),
            "text_color": ("#ADAFAE", "#ADAFAE"),
            "dropdown_fg_color": ("#060606", "#060606"),
            "dropdown_hover_color": ("#2A9FD6", "#2A9FD6"),
            "dropdown_text_color": ("#ADAFAE", "#ADAFAE")
        },
        "combobox": {
            "fg_color": ("#121212", "#121212"),
            "border_color": ("#2A9FD6", "#2A9FD6"),
            "button_color": ("#2A9FD6", "#2A9FD6"),
            "button_hover_color": ("#9933CC", "#9933CC"),
            "text_color": ("#ADAFAE", "#ADAFAE"),
            "dropdown_fg_color": ("#060606", "#060606"),
            "dropdown_hover_color": ("#2A9FD6", "#2A9FD6"),
            "dropdown_text_color": ("#ADAFAE", "#ADAFAE")
        },
        "textbox": {
            "fg_color": ("#121212", "#121212"),
            "border_color": ("#2A9FD6", "#2A9FD6"),
            "text_color": ("#ADAFAE", "#ADAFAE")
        },
        "scrollbar": {
            "fg_color": ("#121212", "#121212"),
            "button_color": ("#2A9FD6", "#2A9FD6"),
            "button_hover_color": ("#9933CC", "#9933CC")
        },
        "scrollable_frame": {
            "fg_color": ("#121212", "#121212"),
            "border_color": ("#2A9FD6", "#2A9FD6"),
            "scrollbar_fg_color": ("#121212", "#121212"),
            "scrollbar_button_color": ("#2A9FD6", "#2A9FD6"),
            "scrollbar_button_hover_color": ("#9933CC", "#9933CC")
        },
        "tabview": {
            "fg_color": ("#121212", "#121212"),
            "segmented_button_fg_color": ("#060606", "#060606"),
            "segmented_button_selected_color": ("#2A9FD6", "#2A9FD6"),
            "segmented_button_selected_hover_color": ("#9933CC", "#9933CC"),
            "segmented_button_unselected_color": ("#121212", "#121212"),
            "segmented_button_unselected_hover_color": ("#060606", "#060606"),
            "text_color": ("#ADAFAE", "#ADAFAE"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#555555", "#555555")
        },
        "segmented_button": {
            "fg_color": ("#060606", "#060606"),
            "selected_color": ("#2A9FD6", "#2A9FD6"),
            "selected_hover_color": ("#9933CC", "#9933CC"),
            "unselected_color": ("#121212", "#121212"),
            "unselected_hover_color": ("#060606", "#060606"),
            "text_color": ("#ADAFAE", "#ADAFAE"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#555555", "#555555")
        },
        "ttk": {
            "background": "#060606",
            "foreground": "#ADAFAE",
            "fieldbackground": "#121212",
            "selectbackground": "#2A9FD6",
            "selectforeground": "#FFFFFF",
            "activebackground": "#9933CC",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#555555",
            "bordercolor": "#2A9FD6",
            "insertcolor": "#ADAFAE"
        },
        "tk": {
            "background": "#060606",
            "foreground": "#ADAFAE",
            "activebackground": "#2A9FD6",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#555555",
            "highlightbackground": "#121212",
            "highlightcolor": "#2A9FD6",
            "insertbackground": "#ADAFAE",
            "selectbackground": "#2A9FD6",
            "selectforeground": "#FFFFFF",
            "troughcolor": "#121212"
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
        },
        "entry": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "border_color": ("#8BAAFF", "#8BAAFF"),
            "text_color": ("#FBFBFB", "#FBFBFB")
        },
        "checkbox": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "border_color": ("#8BAAFF", "#8BAAFF"),
            "checkmark_color": ("#FFFFFF", "#FFFFFF"),
            "hover_color": ("#A177FF", "#A177FF"),
            "text_color": ("#FBFBFB", "#FBFBFB")
        },
        "radio_button": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "border_color": ("#8BAAFF", "#8BAAFF"),
            "hover_color": ("#A177FF", "#A177FF"),
            "text_color": ("#FBFBFB", "#FBFBFB")
        },
        "switch": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "progress_color": ("#A177FF", "#A177FF"),
            "button_color": ("#FFFFFF", "#FFFFFF"),
            "button_hover_color": ("#F5D1C5", "#F5D1C5"),
            "text_color": ("#FBFBFB", "#FBFBFB")
        },
        "slider": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "progress_color": ("#A177FF", "#A177FF"),
            "button_color": ("#FFFFFF", "#FFFFFF"),
            "button_hover_color": ("#F5D1C5", "#F5D1C5")
        },
        "progressbar": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "progress_color": ("#A177FF", "#A177FF")
        },
        "option_menu": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "button_color": ("#A177FF", "#A177FF"),
            "button_hover_color": ("#85E3FF", "#85E3FF"),
            "text_color": ("#FBFBFB", "#FBFBFB"),
            "dropdown_fg_color": ("#25023F", "#25023F"),
            "dropdown_hover_color": ("#A177FF", "#A177FF"),
            "dropdown_text_color": ("#FBFBFB", "#FBFBFB")
        },
        "combobox": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "border_color": ("#8BAAFF", "#8BAAFF"),
            "button_color": ("#A177FF", "#A177FF"),
            "button_hover_color": ("#85E3FF", "#85E3FF"),
            "text_color": ("#FBFBFB", "#FBFBFB"),
            "dropdown_fg_color": ("#25023F", "#25023F"),
            "dropdown_hover_color": ("#A177FF", "#A177FF"),
            "dropdown_text_color": ("#FBFBFB", "#FBFBFB")
        },
        "textbox": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "border_color": ("#8BAAFF", "#8BAAFF"),
            "text_color": ("#FBFBFB", "#FBFBFB")
        },
        "scrollbar": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "button_color": ("#A177FF", "#A177FF"),
            "button_hover_color": ("#85E3FF", "#85E3FF")
        },
        "scrollable_frame": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "border_color": ("#8BAAFF", "#8BAAFF"),
            "scrollbar_fg_color": ("#3A1F5D", "#3A1F5D"),
            "scrollbar_button_color": ("#A177FF", "#A177FF"),
            "scrollbar_button_hover_color": ("#85E3FF", "#85E3FF")
        },
        "tabview": {
            "fg_color": ("#3A1F5D", "#3A1F5D"),
            "segmented_button_fg_color": ("#25023F", "#25023F"),
            "segmented_button_selected_color": ("#A177FF", "#A177FF"),
            "segmented_button_selected_hover_color": ("#85E3FF", "#85E3FF"),
            "segmented_button_unselected_color": ("#3A1F5D", "#3A1F5D"),
            "segmented_button_unselected_hover_color": ("#25023F", "#25023F"),
            "text_color": ("#FBFBFB", "#FBFBFB"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#8BAAFF", "#8BAAFF")
        },
        "segmented_button": {
            "fg_color": ("#25023F", "#25023F"),
            "selected_color": ("#A177FF", "#A177FF"),
            "selected_hover_color": ("#85E3FF", "#85E3FF"),
            "unselected_color": ("#3A1F5D", "#3A1F5D"),
            "unselected_hover_color": ("#25023F", "#25023F"),
            "text_color": ("#FBFBFB", "#FBFBFB"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#8BAAFF", "#8BAAFF")
        },
        "ttk": {
            "background": "#25023F",
            "foreground": "#FBFBFB",
            "fieldbackground": "#3A1F5D",
            "selectbackground": "#A177FF",
            "selectforeground": "#FFFFFF",
            "activebackground": "#85E3FF",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#8BAAFF",
            "bordercolor": "#8BAAFF",
            "insertcolor": "#FBFBFB"
        },
        "tk": {
            "background": "#25023F",
            "foreground": "#FBFBFB",
            "activebackground": "#A177FF",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#8BAAFF",
            "highlightbackground": "#3A1F5D",
            "highlightcolor": "#8BAAFF",
            "insertbackground": "#FBFBFB",
            "selectbackground": "#A177FF",
            "selectforeground": "#FFFFFF",
            "troughcolor": "#3A1F5D"
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
        },
        "entry": {
            "fg_color": ("#333333", "#333333"),
            "border_color": ("#4F4F4F", "#4F4F4F"),
            "text_color": ("#E5E5E5", "#E5E5E5")
        },
        "checkbox": {
            "fg_color": ("#333333", "#333333"),
            "border_color": ("#4F4F4F", "#4F4F4F"),
            "checkmark_color": ("#E5E5E5", "#E5E5E5"),
            "hover_color": ("#6F6F6F", "#6F6F6F"),
            "text_color": ("#E5E5E5", "#E5E5E5")
        },
        "radio_button": {
            "fg_color": ("#333333", "#333333"),
            "border_color": ("#4F4F4F", "#4F4F4F"),
            "hover_color": ("#6F6F6F", "#6F6F6F"),
            "text_color": ("#E5E5E5", "#E5E5E5")
        },
        "switch": {
            "fg_color": ("#333333", "#333333"),
            "progress_color": ("#6F6F6F", "#6F6F6F"),
            "button_color": ("#E5E5E5", "#E5E5E5"),
            "button_hover_color": ("#CFCF9D", "#CFCF9D"),
            "text_color": ("#E5E5E5", "#E5E5E5")
        },
        "slider": {
            "fg_color": ("#333333", "#333333"),
            "progress_color": ("#6F6F6F", "#6F6F6F"),
            "button_color": ("#E5E5E5", "#E5E5E5"),
            "button_hover_color": ("#CFCF9D", "#CFCF9D")
        },
        "progressbar": {
            "fg_color": ("#333333", "#333333"),
            "progress_color": ("#6F6F6F", "#6F6F6F")
        },
        "option_menu": {
            "fg_color": ("#333333", "#333333"),
            "button_color": ("#6F6F6F", "#6F6F6F"),
            "button_hover_color": ("#8F8F8F", "#8F8F8F"),
            "text_color": ("#E5E5E5", "#E5E5E5"),
            "dropdown_fg_color": ("#1F1F1F", "#1F1F1F"),
            "dropdown_hover_color": ("#6F6F6F", "#6F6F6F"),
            "dropdown_text_color": ("#E5E5E5", "#E5E5E5")
        },
        "combobox": {
            "fg_color": ("#333333", "#333333"),
            "border_color": ("#4F4F4F", "#4F4F4F"),
            "button_color": ("#6F6F6F", "#6F6F6F"),
            "button_hover_color": ("#8F8F8F", "#8F8F8F"),
            "text_color": ("#E5E5E5", "#E5E5E5"),
            "dropdown_fg_color": ("#1F1F1F", "#1F1F1F"),
            "dropdown_hover_color": ("#6F6F6F", "#6F6F6F"),
            "dropdown_text_color": ("#E5E5E5", "#E5E5E5")
        },
        "textbox": {
            "fg_color": ("#333333", "#333333"),
            "border_color": ("#4F4F4F", "#4F4F4F"),
            "text_color": ("#E5E5E5", "#E5E5E5")
        },
        "scrollbar": {
            "fg_color": ("#333333", "#333333"),
            "button_color": ("#6F6F6F", "#6F6F6F"),
            "button_hover_color": ("#8F8F8F", "#8F8F8F")
        },
        "scrollable_frame": {
            "fg_color": ("#333333", "#333333"),
            "border_color": ("#4F4F4F", "#4F4F4F"),
            "scrollbar_fg_color": ("#333333", "#333333"),
            "scrollbar_button_color": ("#6F6F6F", "#6F6F6F"),
            "scrollbar_button_hover_color": ("#8F8F8F", "#8F8F8F")
        },
        "tabview": {
            "fg_color": ("#333333", "#333333"),
            "segmented_button_fg_color": ("#1F1F1F", "#1F1F1F"),
            "segmented_button_selected_color": ("#6F6F6F", "#6F6F6F"),
            "segmented_button_selected_hover_color": ("#8F8F8F", "#8F8F8F"),
            "segmented_button_unselected_color": ("#333333", "#333333"),
            "segmented_button_unselected_hover_color": ("#1F1F1F", "#1F1F1F"),
            "text_color": ("#E5E5E5", "#E5E5E5"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#AAAAAA", "#AAAAAA")
        },
        "segmented_button": {
            "fg_color": ("#1F1F1F", "#1F1F1F"),
            "selected_color": ("#6F6F6F", "#6F6F6F"),
            "selected_hover_color": ("#8F8F8F", "#8F8F8F"),
            "unselected_color": ("#333333", "#333333"),
            "unselected_hover_color": ("#1F1F1F", "#1F1F1F"),
            "text_color": ("#E5E5E5", "#E5E5E5"),
            "selected_text_color": ("#FFFFFF", "#FFFFFF"),
            "unselected_text_color": ("#AAAAAA", "#AAAAAA")
        },
        "ttk": {
            "background": "#1F1F1F",
            "foreground": "#E5E5E5",
            "fieldbackground": "#333333",
            "selectbackground": "#6F6F6F",
            "selectforeground": "#FFFFFF",
            "activebackground": "#8F8F8F",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#4F4F4F",
            "bordercolor": "#4F4F4F",
            "insertcolor": "#E5E5E5"
        },
        "tk": {
            "background": "#1F1F1F",
            "foreground": "#E5E5E5",
            "activebackground": "#6F6F6F",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#4F4F4F",
            "highlightbackground": "#333333",
            "highlightcolor": "#4F4F4F",
            "insertbackground": "#E5E5E5",
            "selectbackground": "#6F6F6F",
            "selectforeground": "#FFFFFF",
            "troughcolor": "#333333"
        }
    },
    
    # Normal CTk - The default CustomTkinter theme
    "normal": {
        "appearance_mode": "dark",
        "color_theme": "blue",
        # Uses the default CustomTkinter colors
        "colors": {
            "primary": "#1F6AA5",
            "secondary": "#4A4D50",
            "success": "#2CC985",
            "danger": "#E6513F",
            "warning": "#FFA500",
            "info": "#3B8ED0",
            "light": "#DBDBDB",
            "dark": "#242424"
        },
        "ttk": {
            "background": "#242424",
            "foreground": "#DBDBDB",
            "fieldbackground": "#343638",
            "selectbackground": "#1F6AA5",
            "selectforeground": "#FFFFFF",
            "activebackground": "#3B8ED0",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#6C6C6C",
            "bordercolor": "#3B8ED0",
            "insertcolor": "#DBDBDB"
        },
        "tk": {
            "background": "#242424",
            "foreground": "#DBDBDB",
            "activebackground": "#1F6AA5",
            "activeforeground": "#FFFFFF",
            "disabledforeground": "#6C6C6C",
            "highlightbackground": "#343638",
            "highlightcolor": "#3B8ED0",
            "insertbackground": "#DBDBDB",
            "selectbackground": "#1F6AA5",
            "selectforeground": "#FFFFFF",
            "troughcolor": "#343638"
        }
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
        },
        "entry": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "border_color": ("#D4AF37", "#D4AF37"),
            "text_color": ("#FAD7A0", "#FAD7A0")
        },
        "checkbox": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "border_color": ("#D4AF37", "#D4AF37"),
            "checkmark_color": ("#212121", "#212121"),
            "hover_color": ("#D4AF37", "#D4AF37"),
            "text_color": ("#FAD7A0", "#FAD7A0")
        },
        "radio_button": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "border_color": ("#D4AF37", "#D4AF37"),
            "hover_color": ("#D4AF37", "#D4AF37"),
            "text_color": ("#FAD7A0", "#FAD7A0")
        },
        "switch": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "progress_color": ("#D4AF37", "#D4AF37"),
            "button_color": ("#FAD7A0", "#FAD7A0"),
            "button_hover_color": ("#F5B041", "#F5B041"),
            "text_color": ("#FAD7A0", "#FAD7A0")
        },
        "slider": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "progress_color": ("#D4AF37", "#D4AF37"),
            "button_color": ("#FAD7A0", "#FAD7A0"),
            "button_hover_color": ("#F5B041", "#F5B041")
        },
        "progressbar": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "progress_color": ("#D4AF37", "#D4AF37")
        },
        "option_menu": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "button_color": ("#D4AF37", "#D4AF37"),
            "button_hover_color": ("#F5B041", "#F5B041"),
            "text_color": ("#FAD7A0", "#FAD7A0"),
            "dropdown_fg_color": ("#212121", "#212121"),
            "dropdown_hover_color": ("#D4AF37", "#D4AF37"),
            "dropdown_text_color": ("#FAD7A0", "#FAD7A0")
        },
        "combobox": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "border_color": ("#D4AF37", "#D4AF37"),
            "button_color": ("#D4AF37", "#D4AF37"),
            "button_hover_color": ("#F5B041", "#F5B041"),
            "text_color": ("#FAD7A0", "#FAD7A0"),
            "dropdown_fg_color": ("#212121", "#212121"),
            "dropdown_hover_color": ("#D4AF37", "#D4AF37"),
            "dropdown_text_color": ("#FAD7A0", "#FAD7A0")
        },
        "textbox": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "border_color": ("#D4AF37", "#D4AF37"),
            "text_color": ("#FAD7A0", "#FAD7A0")
        },
        "scrollbar": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "button_color": ("#D4AF37", "#D4AF37"),
            "button_hover_color": ("#F5B041", "#F5B041")
        },
        "scrollable_frame": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "border_color": ("#D4AF37", "#D4AF37"),
            "scrollbar_fg_color": ("#2C2C2C", "#2C2C2C"),
            "scrollbar_button_color": ("#D4AF37", "#D4AF37"),
            "scrollbar_button_hover_color": ("#F5B041", "#F5B041")
        },
        "tabview": {
            "fg_color": ("#2C2C2C", "#2C2C2C"),
            "segmented_button_fg_color": ("#212121", "#212121"),
            "segmented_button_selected_color": ("#D4AF37", "#D4AF37"),
            "segmented_button_selected_hover_color": ("#F5B041", "#F5B041"),
            "segmented_button_unselected_color": ("#2C2C2C", "#2C2C2C"),
            "segmented_button_unselected_hover_color": ("#212121", "#212121"),
            "text_color": ("#FAD7A0", "#FAD7A0"),
            "selected_text_color": ("#212121", "#212121"),
            "unselected_text_color": ("#AA8C2C", "#AA8C2C")
        },
        "segmented_button": {
            "fg_color": ("#212121", "#212121"),
            "selected_color": ("#D4AF37", "#D4AF37"),
            "selected_hover_color": ("#F5B041", "#F5B041"),
            "unselected_color": ("#2C2C2C", "#2C2C2C"),
            "unselected_hover_color": ("#212121", "#212121"),
            "text_color": ("#FAD7A0", "#FAD7A0"),
            "selected_text_color": ("#212121", "#212121"),
            "unselected_text_color": ("#AA8C2C", "#AA8C2C")
        },
        "ttk": {
            "background": "#212121",
            "foreground": "#FAD7A0",
            "fieldbackground": "#2C2C2C",
            "selectbackground": "#D4AF37",
            "selectforeground": "#212121",
            "activebackground": "#F5B041",
            "activeforeground": "#212121",
            "disabledforeground": "#AA8C2C",
            "bordercolor": "#D4AF37",
            "insertcolor": "#FAD7A0"
        },
        "tk": {
            "background": "#212121",
            "foreground": "#FAD7A0",
            "activebackground": "#D4AF37",
            "activeforeground": "#212121",
            "disabledforeground": "#AA8C2C",
            "highlightbackground": "#2C2C2C",
            "highlightcolor": "#D4AF37",
            "insertbackground": "#FAD7A0",
            "selectbackground": "#D4AF37",
            "selectforeground": "#212121",
            "troughcolor": "#2C2C2C"
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

# Check the first few themes to see what entries exist for ctktext
sample_themes = list(THEMES.keys())[:3]
for theme_name in sample_themes:
    theme = THEMES[theme_name]
    print(f"Theme '{theme_name}' structure:")
    if "ctktext" in theme:
        print(f"  ctktext exists with properties: {theme['ctktext']}")
    elif "ctktextbox" in theme:
        print(f"  ctktextbox exists with properties: {theme['ctktextbox']}")
    else:
        print("  No ctktext or ctktextbox entry found!")
        
# Now add or ensure that text_color is defined for each theme's text widgets
for theme_name in THEMES:
    theme = THEMES[theme_name]
    
    # Check if we need to add ctktext entry
    if "ctktext" not in theme and "ctktextbox" not in theme:
        # If we have text_color in ctkentry, use that
        if "ctkentry" in theme and "text_color" in theme["ctkentry"]:
            theme["ctktext"] = {"text_color": theme["ctkentry"]["text_color"]}
        else:
            # Default to a contrasting color based on background
            bg_color = theme.get("frame", {}).get("fg_color", ["#FFFFFF", "#333333"])
            # Use light color for dark backgrounds, dark for light backgrounds
            text_color = ["#000000", "#FFFFFF"]  # Default black for light mode, white for dark
            theme["ctktext"] = {"text_color": text_color}
    
    # Ensure theme uses the correct key 'ctktext' not 'ctktextbox'
    if "ctktextbox" in theme and "ctktext" not in theme:
        theme["ctktext"] = theme["ctktextbox"] 