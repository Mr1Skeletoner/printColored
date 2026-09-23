from .core import formatfinder

def ansi_range():
    print("All possible formats in range of 1-107:")
    formatfinder("1","107")

def all_ansi_dict_formats():
    print("All available formats:")
    formatfinder("ansi_dict","")

def all_html_formats():
    print("All HTML formats:")
    formatfinder("html_dict","")

def all_custom_formats():
    print("All custom formats:")
    formatfinder("custom_dict","")

def all_fonts():
    print("All fonts available:")
    formatfinder(" ","font")

def all_decors():
    print("All decorators available:")
    formatfinder(" ","decors")

display = {
    "all_ansi_formats": ansi_range,
    "ansi_dict":        all_ansi_dict_formats,
    "html_dict":        all_html_formats,
    "custom_dict":      all_custom_formats,
    "fonts":            all_fonts,
    "decorators":       all_decors
}


def display_formats(selected_source=None):
    if selected_source:
        if selected_source in display:
            display[selected_source]()
        else:
            raise ValueError(f"{selected_source} Not a valid format source!")
    else:
        for source in display:
            display[source]()