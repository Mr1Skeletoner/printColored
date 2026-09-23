"""
 https://github.com/Mr1Skeletoner/printColored
"""



try:
    from colorama import just_fix_windows_console
    just_fix_windows_console()
except ImportError:
    # if youre on an older Windows version (7/8) and colors don't show up, run: pip install colorama
    import sys
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            STD_OUTPUT_HANDLE = -11
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

            handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
            mode = ctypes.c_uint32()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
        except Exception:
            pass
    

from pathlib import Path
import json
from platformdirs import user_config_dir

CONFIG_DIR = Path(user_config_dir("printColored"))
CUSTOM_FORMATS_PATH = CONFIG_DIR / "custom.json"


def load_custom_formats():
    if CUSTOM_FORMATS_PATH.exists():
        with open(CUSTOM_FORMATS_PATH, "r") as file:
            return json.load(file)
    return {}


def save_custom_formats(formats):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CUSTOM_FORMATS_PATH, "w") as file:
        json.dump(formats, file, indent=4)


def add_custom_format(name, value):
    formats = load_custom_formats()
    formats[name] = value
    save_custom_formats(formats)
    return formats


custom_formats = load_custom_formats()


from . import Fonter
from .formats import ansi_formats, html_colors

_default_source_order = ("ansi_format","rgb_format","custom_format")

def _font_check(text, *inputs):
    changed = False
    font = ""
    decorator = ""
    for request in inputs:
        if request in Fonter.fonts:
            font = request
            changed = True
        elif request in Fonter.decorators:
            decorator = request
            changed = True
    return Fonter.Fonter(text, font, decorator) if changed == True else text 

def _reset(reset):
    if reset:
        return "\033[0m"
    else: 
        return ""

def _single_code(fformat, *, html_view="", source_order=()):
    if fformat.replace(";", "").isdigit():
        return fformat
    for source in source_order:
        if source == "ansi_format":
            if fformat in ansi_formats:
                return ansi_formats.get(fformat)
        elif source == "rgb_format":
            if fformat in html_colors:
                return str("38;2;" if html_view != "bg" else "48;2;") + html_colors.get(fformat)
        elif source == "custom_format":
            if fformat in custom_formats:
                return custom_formats.get(fformat)
        else:
            raise ValueError(f"{source}: Unknown Format Source!")
    raise ValueError(f"{fformat}: Unknown Format!")
    
def _build_code(*formats_used, html_view="", source_order=()):
    code_list = []
    for name in formats_used:
        name = _single_code(name, html_view=html_view, source_order=source_order)
        if name != None: 
            code_list.append(name)
        
    return ";".join(code_list)

def _rgb_validation(r,g,b):
    if r == "" and g == "" and b == "":
        return ""
    elif r == "" or g == "" or b == "":
        raise ValueError("One or more RGB values are missing!")
    elif not r.isdigit() or not g.isdigit() or not b.isdigit():
        raise ValueError("You cant enter a non-digit!")
    elif int(r) > 255 or int(r) < 0 or int(g) > 255 or int(g) < 0 or int(b) > 255 or int(b) < 0:
        raise ValueError("The RGB value must be greater than or equal 0, and lesser than or equal 255!")
    return ";".join([r,g,b])


class Theme:
    def __init__(self, *formats_used):
        self.formats_used = formats_used
    
    def print(self, text, *, reset=True, html_view="", source_order=_default_source_order):
        text = _font_check(text, *self.formats_used)
        self.format_code = _build_code(*self.formats_used, html_view=html_view, source_order=source_order) 
        reset = _reset(reset)
        print(f"\033[{self.format_code}m{text}{reset}")
    
    def overwrite(self, *new):
        self.formats_used = new
    
    def add(self, *new):
        self.formats_used = self.formats_used + new

    def remove(self, *removed):
        self.formats_used = tuple(fformat for fformat in self.formats_used if fformat not in removed)
    
    def showUsed(self):
        print(self.formats_used)

    def __str__(self):
        return str(self.formats_used)


class ThemeRGBV(Theme):
    def __init__(self, r="", g="", b="", r2="", g2="", b2="", *formats_used):
        super().__init__(*formats_used)
        
        self.fg = _rgb_validation(r,g,b)
        self.bg = _rgb_validation(r2,g2,b2)
            
    def print(self, text, *, reset=True, html_view="", source_order=_default_source_order):
        text = _font_check(text, *self.formats_used)
        self.format_code = _build_code(*self.formats_used, html_view=html_view, source_order=source_order)
        reset = _reset(reset)

        if self.format_code:
            self.format_code += ";"

        if self.fg == "":
            if self.bg == "":
                super().print(text, reset=reset, html_view=html_view, source_order=source_order)
            else:
                self.rgbcode = "48;2;" + self.bg
                self.finalcode = self.format_code + self.rgbcode
                print(f"\033[{self.finalcode}m{text}{reset}")
        else:
            if self.bg == "":
                self.rgbcode = "38;2;" + self.fg
                self.finalcode = self.format_code + self.rgbcode
                print(f"\033[{self.finalcode}m{text}{reset}")
            else:
                self.rgbcode = "38;2;" + self.fg + ";48;2;" + self.bg
                self.finalcode = self.format_code + self.rgbcode
                print(f"\033[{self.finalcode}m{text}{reset}")
    
    def overwrite(self, r,g,b, r2,g2,b2, *new):
        super().overwrite(*new)
        
        self.fg = _rgb_validation(r,g,b)
        self.bg = _rgb_validation(r2,g2,b2)
        
    def showUsed(self):
      print(f"Foreground: {self.fg}")
      print(f"Background: {self.bg}")
      print(f"Formats: {self.formats_used}")

    def __str__(self):
        return self.fg +";"+ self.bg +" "+ self.formats_used


def printColored(text, *formats_used, reset= True, html_view="", source_order=_default_source_order):
    text = _font_check(text, *formats_used)
    code = _build_code(*formats_used, html_view=html_view, source_order=source_order)        
    reset = _reset(reset)

    print(f"\033[{code}m{text}{reset}")


def colorGen(*formats_used, mode="", html_view="", source_order=_default_source_order):
    code = _build_code(*formats_used, html_view=html_view, source_order=source_order)
    if mode == "b":
        return code
    else:
        return f"\033[{code}m"

# colorGen is the replacement of the legacy function
# its WAYYY simpler, but takes alot of space to write
# btw the legacy function was broken sooo
# now colorGen is also fixed


def printl(text=(), formats_used=(), *, sepr=""):
    
    for i, (line, fformat) in enumerate(zip(text, formats_used)):
        code = []
        line = _font_check(line, fformat)
        if type(fformat) == str:
            fformat = _single_code(fformat)
            if fformat != None:
                code.append(fformat)

        elif type(fformat) == tuple:
            for name in fformat:
                name = _single_code(name)
                if name != None:
                    code.append(name)
        
        code = ";".join(code)
        print(f"\033[{code}m{line}\033[0m" + sepr, end="\n" if i == len(text) - 1 else "")
        
# printl is the replacement of colorGen
# its WAY WAYYYY simpler, and takes less space to write
# Dunno if i should keep colorGen, but ill just leave it there because
# it returns the color code itself

def printRGB(text, r,g,b, *formats_used, view="", html_view="",reset=True, source_order=_default_source_order):
    text = _font_check(text, *formats_used)
    code = _build_code(*formats_used, html_view=html_view, source_order=source_order)
    reset = _reset(reset)    
    # if you dont want a format when using the rgb function,
    # you can just not enter it
    rgbvalue = _rgb_validation(r,g,b)
    if rgbvalue != "":
        viewvalue = "48;" if view.lower() == "bg" else "38;"
    else:
        viewvalue = ""

    if code != "":
        code = ";" + code


    print(f"\033[{viewvalue}2;{rgbvalue}{code}m{text}{reset}")


def printRGBV(text, r,g,b, r2, g2, b2, *formats_used, reset=True, html_view="", source_order=_default_source_order):
    text = _font_check(text, *formats_used)
    code = _build_code(*formats_used, html_view=html_view, source_order=source_order)
    reset = _reset(reset)

    fg = _rgb_validation(r,g,b)
    bg = _rgb_validation(r2,g2,b2)
    if code != "":
        code += ";"
    

    if fg == "":
        if bg == "":
            print(f"\033[{code}m{text}{reset}")
        else:
            print(f"\033[{code}48;2;{bg}m{text}{reset}")
    else:
        if bg == "":
            print(f"\033[{code}38;2;{fg}m{text}{reset}")
        else:
            print(f"\033[{code}38;2;{fg};48;2;{bg}m{text}{reset}")
        

def formatfinder(min, max): # made this to find new formats, theres nothing beyond 107
    # btw use strings ("1","108") and not integers (1,108)
    if min.isdigit() and max.isdigit():
        min = int(min)
        max = int(max)
        for code in range(min, max+1):
            print(f"At iteration {code}: \033[{code}mHello World!\033[0m")
    elif min == "font" or max == "font":
        for key, value in Fonter.fonts.items():
            print(f"{key}: {value}")
    elif min == "decors" or max == "decors":
        for key, value in Fonter.decorators.items():
            print(f"{key}: {value}")
    elif min == "ansi_dict" or max == "ansi_dict":
        for key, value in ansi_formats.items():
           print(f"\033[{value}m{key}\033[0m")
    elif min == "html_dict" or max == "html_dict":
        for key, value in html_colors.items():
           print(f"\033[38;2;{value}m{key}\033[0m")
    elif min == "custom_dict" or max == "custom_dict":
        for key, value in custom_formats.items():
           print(f"\033[{value}m{key}\033[0m")
