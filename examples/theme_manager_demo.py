import os
import sys
import tkinter as tk
import customtkinter as ctk

# Add the package to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

try:
    # Import the theme manager
    from src.CTkBootstrap.theme_manager import ThemeManager
    from src.CTkBootstrap.themes import THEMES
except ImportError:
    print("CTkBootstrap modules not found. Make sure you're running this script from the correct directory.")
    sys.exit(1)


class ThemeManagerExample:
    """A simple example demonstrating the ThemeManager API"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("ThemeManager Example")
        self.root.geometry("600x500")
        
        # Create a theme manager instance with the 'darkly' theme
        self.theme_manager = ThemeManager("darkly")
        
        # Create a main container
        self.container = self.theme_manager.create_themed_frame(root)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Create header with theme selector
        self.create_header()
        
        # Create content
        self.create_content()
        
        # Apply initial theme to all widgets
        self.theme_manager.apply_theme_to_all_widgets(root)
    
    def create_header(self):
        """Create header with title and theme selector"""
        header = ctk.CTkFrame(self.container)
        header.pack(fill="x", pady=(0, 20))
        
        # Title
        ctk.CTkLabel(
            header,
            text="ThemeManager Demo",
            font=("Helvetica", 20, "bold")
        ).pack(side="left", padx=10, pady=10)
        
        # Theme selector frame
        selector_frame = ctk.CTkFrame(header)
        selector_frame.pack(side="right", padx=10, pady=10)
        
        # Theme label
        ctk.CTkLabel(selector_frame, text="Theme:").pack(side="left", padx=(0, 5))
        
        # Theme dropdown
        self.themes = list(THEMES.keys())
        theme_var = tk.StringVar(value=self.theme_manager.theme_name)
        
        theme_dropdown = ctk.CTkOptionMenu(
            selector_frame,
            values=self.themes,
            variable=theme_var,
            command=self.change_theme,
            width=120
        )
        theme_dropdown.pack(side="left", padx=5)
        
        # Mode indicator
        self.mode_label = ctk.CTkLabel(
            selector_frame, 
            text=f"Mode: {self.theme_manager.appearance_mode.capitalize()}"
        )
        self.mode_label.pack(side="left", padx=(10, 0))
    
    def create_content(self):
        """Create the main content"""
        # Create a frame for the content
        content = ctk.CTkFrame(self.container)
        content.pack(fill="both", expand=True)
        
        # Left panel - Buttons
        left_panel = ctk.CTkFrame(content)
        left_panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Buttons section title
        ctk.CTkLabel(
            left_panel, 
            text="Themed Buttons",
            font=("Helvetica", 16)
        ).pack(anchor="w", padx=10, pady=(0, 10))
        
        # Standard button
        self.theme_manager.create_themed_button(
            left_panel,
            text="Standard Button",
            command=lambda: self.show_message("Standard button clicked")
        ).pack(fill="x", padx=10, pady=5)
        
        # Primary button
        self.theme_manager.create_primary_button(
            left_panel,
            text="Primary Button",
            command=lambda: self.show_message("Primary button clicked")
        ).pack(fill="x", padx=10, pady=5)
        
        # Secondary button
        self.theme_manager.create_secondary_button(
            left_panel,
            text="Secondary Button",
            command=lambda: self.show_message("Secondary button clicked")
        ).pack(fill="x", padx=10, pady=5)
        
        # Success button
        self.theme_manager.create_success_button(
            left_panel,
            text="Success Button",
            command=lambda: self.show_message("Success button clicked")
        ).pack(fill="x", padx=10, pady=5)
        
        # Danger button
        self.theme_manager.create_danger_button(
            left_panel,
            text="Danger Button",
            command=lambda: self.show_message("Danger button clicked")
        ).pack(fill="x", padx=10, pady=5)
        
        # Warning button
        self.theme_manager.create_warning_button(
            left_panel,
            text="Warning Button",
            command=lambda: self.show_message("Warning button clicked")
        ).pack(fill="x", padx=10, pady=5)
        
        # Info button
        self.theme_manager.create_info_button(
            left_panel,
            text="Info Button",
            command=lambda: self.show_message("Info button clicked")
        ).pack(fill="x", padx=10, pady=5)
        
        # Right panel - Inputs and theme info
        right_panel = ctk.CTkFrame(content)
        right_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # Form section title
        ctk.CTkLabel(
            right_panel, 
            text="Themed Input Widgets",
            font=("Helvetica", 16)
        ).pack(anchor="w", padx=10, pady=(0, 10))
        
        # Text entry with label
        ctk.CTkLabel(right_panel, text="Name:").pack(anchor="w", padx=10, pady=(10, 0))
        
        self.theme_manager.create_themed_entry(
            right_panel,
            placeholder_text="Enter your name"
        ).pack(fill="x", padx=10, pady=(0, 10))
        
        # Textbox with label
        ctk.CTkLabel(right_panel, text="Comments:").pack(anchor="w", padx=10, pady=(10, 0))
        
        self.comments_box = self.theme_manager.create_themed_textbox(
            right_panel,
            height=100
        )
        self.comments_box.pack(fill="x", padx=10, pady=(0, 10))
        self.comments_box.insert("1.0", "Enter your comments here...\nText color matches the theme.")
        
        # Theme color information
        ctk.CTkLabel(
            right_panel, 
            text="Theme Colors",
            font=("Helvetica", 16)
        ).pack(anchor="w", padx=10, pady=(20, 10))
        
        # Theme info textbox
        self.info_box = self.theme_manager.create_themed_textbox(right_panel, height=80)
        self.info_box.pack(fill="x", padx=10, pady=(0, 10))
        
        # Update theme info
        self.update_theme_info()
    
    def change_theme(self, theme_name):
        """Change the current theme"""
        # Change theme in the theme manager
        self.theme_manager.change_theme(theme_name)
        
        # Apply to all widgets
        self.theme_manager.apply_theme_to_all_widgets(self.root)
        
        # Update UI
        self.mode_label.configure(text=f"Mode: {self.theme_manager.appearance_mode.capitalize()}")
        self.update_theme_info()
    
    def update_theme_info(self):
        """Update the theme info textbox"""
        # Clear existing content
        self.info_box.delete("1.0", "end")
        
        # Add theme information
        self.info_box.insert("1.0", f"Current Theme: {self.theme_manager.theme_name}\n")
        self.info_box.insert("end", f"Mode: {self.theme_manager.appearance_mode}\n\n")
        
        # Add color information
        self.info_box.insert("end", "Available Colors:\n")
        colors = [
            ("primary", self.theme_manager.primary),
            ("secondary", self.theme_manager.secondary),
            ("success", self.theme_manager.success),
            ("danger", self.theme_manager.danger),
            ("warning", self.theme_manager.warning),
            ("info", self.theme_manager.info),
        ]
        
        for name, value in colors:
            self.info_box.insert("end", f"  {name}: {value}\n")
    
    def show_message(self, message):
        """Show a message when a button is clicked"""
        # Update the comments box
        self.comments_box.delete("1.0", "end")
        self.comments_box.insert("1.0", message)


if __name__ == "__main__":
    # Initialize CustomTkinter
    ctk.set_appearance_mode("dark")  # Default appearance mode
    ctk.set_default_color_theme("blue")  # Default color theme
    
    # Create the window
    root = ctk.CTk()
    app = ThemeManagerExample(root)
    root.mainloop() 