# dm me on discord if you want: @1skeletoner
# thanks ^-^

formats = { # i think the dictonary now contains every possible format
    # Colors 
    "gray"   : "30",
    "red"    : "31",
    "green"  : "32",
    "yellow" : "33",
    "blue"   : "34",
    "magenta": "35",
    "cyan"   : "36",

    # slightly bright
    # useless but i will leave it there
    "bright_gray"    : "90", # im sure this is just normal gray but
                             # i will leave it there
    "bright_red"     : "91",
    "bright_green"   : "92",
    "bright_yellow"  : "93",
    "bright_blue"    : "94",
    "bright_magenta" : "95",
    "bright_cyan"    : "96",
    "bright_white"   : "97", # trust me, this is different than bold

    # Highlight
    "highlight_red"    : "41",
    "highlight_green"  : "42",
    "highlight_yellow" : "43",
    "highlight_blue"   : "44",
    "highlight_magenta": "45",
    "highlight_cyan"   : "46",
    "highlight_gray"   : "100",
    "highlight_black"  : "40",
    "highlight_white"  : "47",

    # bright highlight
    # what am i even doing in life anymore
    "highlight_bright_red"     : "101",
    "highlight_bright_green"   : "102",
    "highlight_bright_yellow"  : "103",
    "highlight_bright_blue"    : "104",
    "highlight_bright_magenta" : "105",
    "highlight_bright_cyan"    : "106",
    "highlight_bright_white"   : "107",

    # Formats (like bold or italic)
    "bold"            : "1",
    "foggy_gray"      : "2",
    "italic"          : "3",
    "underline"       : "4",
    "inverted"        : "7", # inverted and highlight white are probably the same lol
    "invisible"       : "8",
    "strikethrough"   : "9",
    "double_underline": "21",

    "reset": "0", # placeholder or smth idk i dont even use it bc u can just type 0 but i will just keep it there
    ""     : "0"
}

class Theme:
    def __init__(self, *_formats):
        self._formats = _formats
    
    def print(self, text):
        self.format_code = ";".join(formats[name] for name in self._formats)
        print(f"\033[{self.format_code}m{text}\033[0m")
    
    def overwrite(self, *new):
        self._formats = new
    
    def add(self, *new):
        self._formats = self._formats + new
    
    def remove(self, *removed):
        self._formats = list(self._formats)
        for fmt in self._formats:
            if fmt in removed:
                self._formats.remove(fmt)
        self._formats = tuple(self._formats)
    
    def showUsed(self):
        print(self._formats)


class ThemeRGBV(Theme):
    def __init__(self, r, g, b, r2, g2, b2, *_formats):
        super().__init__(*_formats)
        
        if r == "" or g == "" or b == "":
            self.fg = ""
        elif not r.isdigit() or not g.isdigit() or not b.isdigit():
            self.fg = ""
        else:
            self.fg = ";".join([r,g,b])
            
        if r2 == "" or g2 == "" or b2 == "":
            self.bg = ""
        elif not r2.isdigit() or not g2.isdigit() or not b2.isdigit():
            self.bg = ""
        else:
            self.bg = ";".join([r2,g2,b2])
            
    def print(self, text):
        if self.fg == "":
            if self.bg == "":
                super().print(text)
            else:
                self.formatcode = ";".join(formats[name] for name in self._formats)
                self.rgbcode = "48;2;" + self.bg
                self.finalcode = self.formatcode + ";" + self.rgbcode
                print(f"\033[{self.finalcode}m{text}\033[0m")
        else:
            if self.bg == "":
                self.formatcode = ";".join(formats[name] for name in self._formats)
                self.rgbcode = "38;2;" + self.fg
                self.finalcode =  self.formatcode + ";" + self.rgbcode
                print(f"\033[{self.finalcode}m{text}\033[0m")
            else:
                self.formatcode = ";".join(formats[name] for name in self._formats)
                self.rgbcode = "38;2;" + self.fg + ";48;2;" + self.bg
                self.finalcode = self.formatcode + ";" + self.rgbcode
                print(f"\033[{self.finalcode}m{text}\033[0m")
    
    def overwrite(self, r,g,b, r2,g2,b2, *new):
        super().overwrite(*new)
        
        if r == "" or g == "" or b == "":
            self.fg = ""
        elif not r.isdigit() or not g.isdigit() or not b.isdigit():
            self.fg = ""
        else:
            self.fg = ";".join([r,g,b])
            
        if r2 == "" or g2 == "" or b2 == "":
            self.bg = ""
        elif not r2.isdigit() or not g2.isdigit() or not b2.isdigit():
            self.bg = ""
        else:
            self.bg = ";".join([r2,g2,b2])
        
    def showUsed(self):
      print(f"Foreground: {self.fg}")
      print(f"Background: {self.bg}")
      print(f"Formats: {self._formats}")


def printColored(text, *_formats):
    format_code = ";".join(formats[name] for name in _formats)
    print(f"\033[{format_code}m{text}\033[0m")

def customC(text, *code): # this removes the need for the version with all useless formats
    code = ";".join(code)
    print(f"\033[{code}m{text}\033[0m")

def generator(*_formats):
    code = ";".join(formats[name] for name in _formats)
    return f"\033[{code}m"

# generator is the replacement of the legacy function
# its WAYYY simpler, but takes alot of space to write
# btw the legacy function was broken sooo
# now generator is also fixed

def customG(*code): # specifically made for rgb
    # also shortened the name for faster writing
    code = ";".join(code)
    return f"\033[{code}m"

def printRGB(text, r, g, b, view, *_formats):
    code = ";".join(formats[name] for name in _formats) 
    # if you dont want a format when using the rgb function,
    # you can just enter ""
    rgbvalue = ";".join([r,g,b])
    viewvalue = "48" if view.lower() == "bg" else "38"
    if code == "0":
        print(f"\033[{viewvalue};2;{rgbvalue}m{text}\033[0m")
    else:
        print(f"\033[{viewvalue};2;{rgbvalue};{code}m{text}\033[0m")

def printRGBV(text, r, g, b, r2, g2, b2, *_formats):
    code = ";".join(formats[name] for name in _formats) 

    fg = ";".join([r,g,b])
    bg = ";".join([r2,g2,b2])
    if code == "0":
        print(f"\033[38;2;{fg};48;2;{bg}m{text}\033[0m")
    else:
        print(f"\033[38;2;{fg};48;2;{bg};{code}m{text}\033[0m")

def formatfinder(min, max): # made this to find new formats, theres nothing beyond 107
    # btw use strings ("1","108") and not integers (1,108)
    if min.isdigit() and max.isdigit():
        min = int(min)
        max = int(max)
        for code in range(min, max+1):
            print(f"At iteration {code}: \033[{code}mHello World!\033[0m")
    else:
        for key, value in formats.items():
           print(f"\033[{value}m{key}\033[0m")

if __name__ == '__main__':
    deco = Theme("green", "bold")
    border = "--------------------------------"
    deco.print(border)
    
    choice = True if input("Do you want to see all available formats?(Y/N): ").lower() == "y" else False
    if choice:
        print("All available formats:")
        formatfinder(" "," ")
    deco.print(border)
    choice = True if input("Do you want to see all existing formats in range 1-107?(Y/N): ").lower() == "y" else False
    if choice:    
        print("All possible formats in range of 1-107:")
        formatfinder("1","107")
    
    # main functions:
    
    # printColored()
    deco.print(border)
    printColored("Example use of printColored()".center(32), "green","bold","italic")
    print("Take a look at the dictionary and enter formats to use")
    deco.print(border)
    
    
    # customC()
    customC("Example use of customC()".center(32), "02", "04")
    print("This is used to enter specific formats not in the dictionary")
    deco.print(border)

    # generators (why did i name it generator?):

    # generator()
    print(
        f"{generator("red", "bold")}   Example use "
        f"{generator("","strikethrough","blue")}of generator()"
        f"{generator("")}")
    deco.print(border)

    # this method is way better
    genformat1 = generator("bright_white","highlight_blue")
    genformat2 = generator("", "yellow", "highlight_green", "underline")
    print(f"    {genformat1}Example 2 {genformat2}of generator(){generator("")}")
    print("This is used for multiple formats in the same line")
    deco.print(border)

    # customG()
    print(
        f"{customG("38","2","255","255","0")}Example use "
        f"{customG("0","48","2","0","0","255")}of customG()"
        f"{customG("0")}"
    )
    deco.print(border)

    genformat3 = customG("38;2","90","50","100","3")
    genformat4 = customG("0","48;2","60","60","255")
    print(f" {genformat3}Example 2 {genformat4}of customG(){customG("0")}")
    print("Same as generator, but for RGB. Also hard to use and read bc its only format codes")
    deco.print(border)


    # the rgb functions (you can either try your luck to get a good color, or find it online)

    # printRGB() 
    printRGB("Example use of printRGB()".center(32), "255","0","255", " ", "bold")
    deco.print(border)
    printRGB("Example 2 of printRGB()".center(32), "0","255","255", "bg", "")
    print("Notice how it can only display either \nforeground or background at one time")
    print("You can also add formats to it".center(32))
    deco.print(border)

    # printRGBV()
    printRGBV("Example use of printRGBV()".center(32), "0","255","0", "0","0","255", "")
    deco.print(border)
    printRGBV("Example 2 of printRGBV()".center(32), "0","0","0", "255", "0", "255", "italic")
    print("It can both display foreground and background, and also add formats".center(32))
    # Note that sometimes the background color blocks the foreground color
    
    deco.print(border)
    
    # Theme and ThemeRGBV classes
    deadly = Theme("bright_red", "double_underline", "bold")
    deadly.print("Example use of Theme class")
    print("It can be used for formats that you use many times")
    deadly.add("strikethrough")
    deadly.print("Example of adding a format(s) using 'add(*formats)'")
    deadly.remove("double_underline", "strikethrough")
    deadly.print("Example of removing a format(s) using 'remove(*formats)'")
    deadly.overwrite("highlight_bright_red", "underline")
    deadly.print("Example of overwriting the object using 'overwrite(*formats)'")
    deadly.showUsed()
    print("You can check the currently used formats using 'showUsed()'")

    deco.print(border)

    classified = ThemeRGBV("255", "255", "255", "0","0","0", "")
    classified.print("Example of 'printRGBV(r,g,b, r2,g2,b2, *formats)'")
    print("It can change both foreground and background, \nand you can choose to use 1 only or both")

    classified.add("bold","underline")
    classified.print("Example of 'add(*formats)'")
    classified.remove("underline")
    classified.print("Example of 'remove(*formats)'")
    print("Adding/removing only affects formats and not the RGB values")
    classified.overwrite("0","0","0","255","255","255", "strikethrough")
    classified.print("Example of 'overwrite(r,g,b, r2,g2,b2, *new)'")
    print("Overwrite rewrites the whole thing")

    deco.print(border)
    deco.overwrite("bright_blue", "bold")
    deco.print(border)
    print("Scroll up for instructions!")
    deco.print(border)
