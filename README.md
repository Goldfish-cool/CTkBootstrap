# CTkBootstrap

A CustomTkinter theme extension that configures Bootstrap-inspired themes into CTk GUI applications. Heavily inspired by ttkbootstrap.

## Features

- **Built-in Themes** - CustomTkinter now includes a Bootstrap-inspired theme system, allowing for seamless integration of various themes into your CTk GUI applications. This feature enables developers to easily switch between different visual styles, enhancing the overall user experience.

- **Simple Integration** - Drop-in replacement for CustomTkinter that adds theme capabilities with minimal code changes.

- **Dynamic Theme Switching** - Change themes at runtime with a simple method call.

- **Comprehensive Widget Support** - All CTk, ttk, and tk widgets are styled consistently according to the selected theme, providing a cohesive look across your entire application.

## Available Themes

CTkBootstrap includes the following themes:

- **Solar** - A dark theme with accent colors inspired by the sun
- **Darkly** - A flat and modern dark theme
- **Cyborg** - A dark theme with a cyberpunk feel
- **Vapor** - A vaporwave aesthetic with purple and blue tones
- **Monodim** - A minimal dark theme using monochromatic colors
- **Normal CTk** - The default CustomTkinter theme
- **Aurium** - A gold and dark theme

## About Light Mode

Light mode is not everyone's preference, and there are several reasons for this. One major reason is that light mode can cause eye strain, especially in low-light environments. Additionally, some users find it harder to focus on the content when the background is bright, leading to decreased productivity. Furthermore, light mode can also make it difficult to distinguish between different UI elements, making the overall user experience less intuitive.

## Project Status

This project is **HEAVILY IN BETA**, indicating that it is still in the early stages of development. As a result, it is expected that bugs and issues will arise. We are committed to addressing these problems as promptly as possible to ensure the project's stability and quality. Your patience and feedback are greatly appreciated during this beta phase.

## Installation

```bash
pip install CTkBootstrap
```

## Simple Usage

```python
import CTkBootstrap as CTk

# Create a window with the 'solar' theme
root = CTk.CTk(style="solar")
root.title("CTkBootstrap Example")

# Create a button (automatically themed)
button = CTk.CTkButton(root, text="Press Me!")
button.pack(padx=20, pady=20)

# Run the application
root.mainloop()
```

## Theme Manager API

CTkBootstrap includes a powerful `ThemeManager` class that provides a simple and intuitive API for working with themes.

### Basic Usage

```python
from CTkBootstrap.theme_manager import ThemeManager

# Create a theme manager with a specific theme
theme_manager = ThemeManager("darkly")

# Access theme colors directly
primary_color = theme_manager.primary  # e.g., "#375A7F"
success_color = theme_manager.success  # e.g., "#00BC8C"

# Create themed widgets
button = theme_manager.create_themed_button(root, text="Themed Button")
entry = theme_manager.create_themed_entry(root, placeholder_text="Enter text...")

# Create semantic colored buttons
primary_btn = theme_manager.create_primary_button(root, text="Primary Action")
secondary_btn = theme_manager.create_secondary_button(root, text="Secondary Action")
success_btn = theme_manager.create_success_button(root, text="Success Action")
danger_btn = theme_manager.create_danger_button(root, text="Danger Action")
warning_btn = theme_manager.create_warning_button(root, text="Warning Action")
info_btn = theme_manager.create_info_button(root, text="Info Action")

# Apply the theme to all widgets in a window
theme_manager.apply_theme_to_all_widgets(root)

# Change the theme at runtime
theme_manager.change_theme("vapor")
```

### Global Theme Management

For simpler usage, you can use the global theme management functions:

```python
from CTkBootstrap.theme_manager import apply_theme, set_theme, get_primary_color

# Set the current theme for the application
set_theme("darkly")

# Apply the theme to all widgets in a window
apply_theme(root)  # Uses the current theme
apply_theme(root, "solar")  # Sets and applies a specific theme

# Get theme colors
primary = get_primary_color()  # Gets the primary color from the current theme
```

See the examples directory for complete demonstrations of the ThemeManager API.

## Changing Themes at Runtime

You can change themes at runtime using the `apply_theme` method:

```python
# Create a window with the default theme
root = CTk.CTk(style="darkly")

# Later, change the theme
root.apply_theme("vapor")
```

## Advanced Usage

Check out the examples directory for more complex examples of using CTkBootstrap, including:

- Basic example with a single window and a few widgets
- Theme showcase demonstrating all available themes with various widgets
- Widget showcase demonstrating how themes are applied to different widget types (CTk, ttk, and tk)

## Supported Widgets

CTkBootstrap supports theming for all of the following widget types:

### CustomTkinter Widgets
- CTkButton
- CTkFrame
- CTkLabel
- CTkEntry
- CTkCheckBox
- CTkRadioButton
- CTkSwitch
- CTkSlider
- CTkProgressBar
- CTkOptionMenu
- CTkComboBox
- CTkTextbox
- CTkScrollbar
- CTkScrollableFrame
- CTkTabview
- CTkSegmentedButton

### Tkinter ttk Widgets
- ttk.Button
- ttk.Checkbutton
- ttk.Combobox
- ttk.Entry
- ttk.Frame
- ttk.Label
- ttk.LabelFrame
- ttk.Menubutton
- ttk.Notebook
- ttk.PanedWindow
- ttk.Progressbar
- ttk.Radiobutton
- ttk.Scale
- ttk.Scrollbar
- ttk.Separator
- ttk.Sizegrip
- ttk.Treeview

### Tkinter Widgets
- tk.Button
- tk.Canvas
- tk.Checkbutton
- tk.Entry
- tk.Frame
- tk.Label
- tk.Listbox
- tk.Menu
- tk.Menubutton
- tk.Message
- tk.Radiobutton
- tk.Scale
- tk.Scrollbar
- tk.Spinbox
- tk.Text
- tk.Toplevel

## Creating Custom Themes

To create a custom theme, you can add your own entry to the `THEMES` dictionary in the `themes.py` file:

```python
# Example custom theme
"my_theme": {
    "appearance_mode": "dark",  # or "light"
    "color_theme": "blue",  # base CTk color theme
    "colors": {
        "primary": "#hex_code",
        "secondary": "#hex_code",
        "success": "#hex_code",
        "danger": "#hex_code",
        "warning": "#hex_code",
        "info": "#hex_code",
        "light": "#hex_code",
        "dark": "#hex_code"
    },
    "window": {
        "fg_color": ("#hex_light", "#hex_dark"),
    },
    "button": {
        "fg_color": ("#hex_light", "#hex_dark"),
        "hover_color": ("#hex_light", "#hex_dark"),
        "text_color": ("#hex_light", "#hex_dark"),
    },
    # Other widget-specific properties for customizing each widget type
    # See the themes.py file for a complete list of supported widget properties
    "ttk": {
        # ttk-specific theming properties
        "background": "#hex_code",
        "foreground": "#hex_code",
        # etc.
    },
    "tk": {
        # tk-specific theming properties
        "background": "#hex_code",
        "foreground": "#hex_code",
        # etc.
    }
}
```

## Contributing

Contributions to CTkBootstrap are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
- Built on top of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
