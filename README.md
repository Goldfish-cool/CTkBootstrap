# CTkBootstrap

A CustomTkinter theme extension that configures Bootstrap-inspired themes into CTk GUI applications. Heavily inspired by ttkbootstrap.

## Features

- **Built-in Themes** - CustomTkinter now includes a Bootstrap-inspired theme system, allowing for seamless integration of various themes into your CTk GUI applications. This feature enables developers to easily switch between different visual styles, enhancing the overall user experience.

- **Simple Integration** - Drop-in replacement for CustomTkinter that adds theme capabilities with minimal code changes.

- **Dynamic Theme Switching** - Change themes at runtime with a simple method call.

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
        # etc.
    },
    "window": {
        "fg_color": ("#hex_light", "#hex_dark"),
    },
    "button": {
        "fg_color": ("#hex_light", "#hex_dark"),
        "hover_color": ("#hex_light", "#hex_dark"),
        "text_color": ("#hex_light", "#hex_dark"),
    },
    # Other widget-specific properties
}
```

## Contributing

Contributions to CTkBootstrap are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
- Built on top of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
