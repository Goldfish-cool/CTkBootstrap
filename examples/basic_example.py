"""
Basic example of using CTkBootstrap.

This example demonstrates how to create a simple GUI application using CTkBootstrap
with different theme options.
"""

import sys
import os

# Add the parent directory to the path so we can import CTkBootstrap
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import CTkBootstrap as CTk
except ImportError:
    print("CTkBootstrap not found. You may need to install it with 'pip install CTkBootstrap'.")
    sys.exit(1)


def create_widgets(app, theme_var):
    """Create the widgets for the application."""
    # Create a frame
    frame = CTk.CTkFrame(app, width=500, height=400)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Add a title
    title = CTk.CTkLabel(frame, text="CTkBootstrap Example", font=("Helvetica", 24))
    title.pack(pady=20)
    
    # Add some buttons
    btn1 = CTk.CTkButton(frame, text="Primary Button")
    btn1.pack(pady=10)
    
    btn2 = CTk.CTkButton(frame, text="Secondary Button", fg_color="gray")
    btn2.pack(pady=10)
    
    # Add text entry
    entry = CTk.CTkEntry(frame, placeholder_text="Type something...")
    entry.pack(pady=10, padx=20, fill="x")
    
    # Add checkbox
    checkbox = CTk.CTkCheckBox(frame, text="Enable feature")
    checkbox.pack(pady=10)
    
    # Add theme selector
    theme_label = CTk.CTkLabel(frame, text="Select Theme:")
    theme_label.pack(pady=(20, 0))
    
    # Create a dropdown for theme selection
    theme_options = list(CTk.THEMES.keys())
    theme_dropdown = CTk.CTkOptionMenu(
        frame, 
        values=theme_options,
        command=lambda t: change_theme(app, t)
    )
    theme_dropdown.set(theme_var)
    theme_dropdown.pack(pady=10)
    
    # Add info text
    info_text = "CTkBootstrap provides Bootstrap-inspired themes for CustomTkinter"
    info = CTk.CTkLabel(frame, text=info_text, wraplength=300)
    info.pack(pady=20)


def change_theme(app, theme_name):
    """Change the application theme."""
    app.apply_theme(theme_name)
    

def main():
    """Main function to run the example."""
    # Available themes: solar, darkly, cyborg, vapor, monodim, normal, aurium
    default_theme = "solar"
    
    # Create the main window with a theme
    app = CTk.CTk(style=default_theme)
    app.title("CTkBootstrap Example")
    app.geometry("600x500")
    
    # Create the widgets
    create_widgets(app, default_theme)
    
    # Start the main event loop
    app.mainloop()


if __name__ == "__main__":
    main() 