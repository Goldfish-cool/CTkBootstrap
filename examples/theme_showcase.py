"""
Theme showcase example for CTkBootstrap.

This example demonstrates all the available themes in CTkBootstrap and
shows various widgets with their themed appearance.
"""

import sys
import os
from typing import Dict, Any

# Add the parent directory to the path so we can import CTkBootstrap
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import CTkBootstrap as CTk
except ImportError:
    print("CTkBootstrap not found. You may need to install it with 'pip install CTkBootstrap'.")
    sys.exit(1)


class ThemeShowcaseApp:
    """An application to showcase all CTkBootstrap themes."""
    
    def __init__(self):
        """Initialize the theme showcase application."""
        # Create the main window with a theme
        self.app = CTk.CTk(style="solar")
        self.app.title("CTkBootstrap Theme Showcase")
        self.app.geometry("800x600")
        
        # Store the current theme
        self.current_theme = "solar"
        
        # Create the main UI
        self.create_ui()
    
    def create_ui(self):
        """Create the user interface."""
        # Create a main frame
        self.main_frame = CTk.CTkFrame(self.app)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create a header frame
        self.header_frame = CTk.CTkFrame(self.main_frame, corner_radius=0)
        self.header_frame.pack(fill="x", padx=0, pady=0)
        
        # Add title and theme selector
        title = CTk.CTkLabel(
            self.header_frame, 
            text="CTkBootstrap Theme Showcase", 
            font=("Helvetica", 24, "bold")
        )
        title.pack(side="left", padx=20, pady=20)
        
        theme_label = CTk.CTkLabel(self.header_frame, text="Select Theme:")
        theme_label.pack(side="left", padx=(40, 5), pady=20)
        
        theme_options = list(CTk.THEMES.keys())
        self.theme_dropdown = CTk.CTkOptionMenu(
            self.header_frame,
            values=theme_options,
            command=self.change_theme
        )
        self.theme_dropdown.set(self.current_theme)
        self.theme_dropdown.pack(side="left", padx=5, pady=20)
        
        # Create content frame with two columns
        self.content_frame = CTk.CTkFrame(self.main_frame)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Left column - Button showcase
        self.left_column = CTk.CTkFrame(self.content_frame)
        self.left_column.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Buttons section
        self.create_button_section(self.left_column)
        
        # Right column - Other widgets
        self.right_column = CTk.CTkFrame(self.content_frame)
        self.right_column.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # Form widgets
        self.create_form_section(self.right_column)
        
        # Footer with theme info
        self.footer_frame = CTk.CTkFrame(self.main_frame, corner_radius=0)
        self.footer_frame.pack(fill="x", padx=0, pady=(10, 0))
        
        self.theme_info_label = CTk.CTkLabel(
            self.footer_frame,
            text=f"Current Theme: {self.current_theme}",
            font=("Helvetica", 12)
        )
        self.theme_info_label.pack(side="left", padx=20, pady=10)
        
        # Credits
        credits = CTk.CTkLabel(
            self.footer_frame,
            text="CTkBootstrap - Inspired by ttkbootstrap",
            font=("Helvetica", 10)
        )
        credits.pack(side="right", padx=20, pady=10)
    
    def create_button_section(self, parent):
        """Create the button showcase section."""
        # Heading
        heading = CTk.CTkLabel(
            parent, 
            text="Button Showcase", 
            font=("Helvetica", 16, "bold")
        )
        heading.pack(padx=10, pady=10)
        
        # Primary button
        primary_btn = CTk.CTkButton(
            parent,
            text="Primary Button",
            font=("Helvetica", 12)
        )
        primary_btn.pack(padx=20, pady=10, fill="x")
        
        # Secondary button with custom color
        secondary_btn = CTk.CTkButton(
            parent,
            text="Secondary Button",
            fg_color="gray",
            font=("Helvetica", 12)
        )
        secondary_btn.pack(padx=20, pady=10, fill="x")
        
        # Button with icon (simulated with text)
        icon_btn = CTk.CTkButton(
            parent,
            text="📁 Open File",
            font=("Helvetica", 12)
        )
        icon_btn.pack(padx=20, pady=10, fill="x")
        
        # Outline button
        outline_btn = CTk.CTkButton(
            parent,
            text="Outline Button",
            fg_color="transparent",
            border_width=1,
            font=("Helvetica", 12)
        )
        outline_btn.pack(padx=20, pady=10, fill="x")
        
        # Small button
        small_btn = CTk.CTkButton(
            parent,
            text="Small Button",
            font=("Helvetica", 10),
            height=28
        )
        small_btn.pack(padx=20, pady=10, fill="x")
        
        # Button row
        btn_row = CTk.CTkFrame(parent)
        btn_row.pack(padx=20, pady=10, fill="x")
        
        for i, text in enumerate(["One", "Two", "Three"]):
            CTk.CTkButton(
                btn_row,
                text=text,
                width=80,
                font=("Helvetica", 10)
            ).pack(side="left", padx=5, pady=5, expand=True)
    
    def create_form_section(self, parent):
        """Create the form widgets showcase section."""
        # Heading
        heading = CTk.CTkLabel(
            parent, 
            text="Form Widgets", 
            font=("Helvetica", 16, "bold")
        )
        heading.pack(padx=10, pady=10)
        
        # Entry with label
        entry_label = CTk.CTkLabel(parent, text="Username:")
        entry_label.pack(padx=20, pady=(10, 0), anchor="w")
        
        username_entry = CTk.CTkEntry(
            parent,
            placeholder_text="Enter your username",
            width=200
        )
        username_entry.pack(padx=20, pady=(0, 10), fill="x")
        
        # Password entry
        pwd_label = CTk.CTkLabel(parent, text="Password:")
        pwd_label.pack(padx=20, pady=(10, 0), anchor="w")
        
        password_entry = CTk.CTkEntry(
            parent,
            placeholder_text="Enter your password",
            show="•",
            width=200
        )
        password_entry.pack(padx=20, pady=(0, 10), fill="x")
        
        # Checkbox group
        checkbox_frame = CTk.CTkFrame(parent)
        checkbox_frame.pack(padx=20, pady=10, fill="x")
        
        checkbox1 = CTk.CTkCheckBox(checkbox_frame, text="Remember me")
        checkbox1.pack(padx=10, pady=5, anchor="w")
        
        checkbox2 = CTk.CTkCheckBox(checkbox_frame, text="Subscribe to newsletter")
        checkbox2.pack(padx=10, pady=5, anchor="w")
        
        # Radio buttons
        radio_label = CTk.CTkLabel(parent, text="Notification preference:")
        radio_label.pack(padx=20, pady=(10, 0), anchor="w")
        
        radio_var = CTk.IntVar(value=1)
        
        radio_frame = CTk.CTkFrame(parent)
        radio_frame.pack(padx=20, pady=(0, 10), fill="x")
        
        radio1 = CTk.CTkRadioButton(
            radio_frame, 
            text="Email", 
            variable=radio_var, 
            value=1
        )
        radio1.pack(padx=10, pady=5, anchor="w")
        
        radio2 = CTk.CTkRadioButton(
            radio_frame, 
            text="SMS", 
            variable=radio_var, 
            value=2
        )
        radio2.pack(padx=10, pady=5, anchor="w")
        
        # Slider
        slider_label = CTk.CTkLabel(parent, text="Volume:")
        slider_label.pack(padx=20, pady=(10, 0), anchor="w")
        
        slider = CTk.CTkSlider(parent, from_=0, to=100)
        slider.pack(padx=20, pady=(0, 10), fill="x")
        slider.set(75)
    
    def change_theme(self, theme_name):
        """Change the application theme."""
        self.current_theme = theme_name
        self.app.apply_theme(theme_name)
        
        # Update theme info
        self.theme_info_label.configure(text=f"Current Theme: {theme_name}")
    
    def run(self):
        """Run the application."""
        self.app.mainloop()


if __name__ == "__main__":
    app = ThemeShowcaseApp()
    app.run() 