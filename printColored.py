"""
 discord: @1skeletoner
 youtube: https://www.youtube.com/@1skeletoner
 github : https://github.com/Mr1Skeletoner/printColored
 thanks for reading :D
"""

import json
with open('custom.json', 'r') as file:
    custom_formats = json.load(file)
import Fonter

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

def _single_code(fformat):
    if fformat.replace(";", "").isdigit():
        return fformat
    elif fformat in formats:
        return formats.get(fformat)
    elif fformat in custom_formats:
        return custom_formats.get(fformat)
    else:
        print(f"{fformat}: Unknown Format!")

def _build_code(*formats_used):
    code_list = []
    for name in formats_used:
        name = _single_code(name)
        if name != None: 
            code_list.append(name)
        
    return ";".join(code_list)

def _rgb_validation(r,g,b):
    if r == "" or g == "" or b == "":
        return ""
    elif not r.isdigit() or not g.isdigit() or not b.isdigit():
        return ""
    elif int(r) > 255 or int(r) < 0 or int(g) > 255 or int(g) < 0 or int(b) > 255 or int(b) < 0:
        return ""
    return ";".join([r,g,b])

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
    "highlight_bright_red"      : "101",
    "highlight_bright_green"    : "102",
    "highlight_bright_yellow"  : "103",
    "highlight_bright_blue"     : "104",
    "highlight_bright_magenta" : "105",
    "highlight_bright_cyan"    : "106",
    "highlight_bright_white"   : "107",

    # Formats (like bold or italic)
    "bold"            : "1",
    "foggygray"       : "2",
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
    def __init__(self, *formats_used):
        self.formats_used = formats_used
    
    def print(self, text):
        text = _font_check(text, *self.formats_used)
        self.format_code = _build_code(*self.formats_used) 
        print(f"\033[{self.format_code}m{text}\033[0m")
    
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
            
    def print(self, text):
        text = _font_check(text, *self.formats_used)
        if self.fg == "":
            if self.bg == "":
                super().print(text)
            else:
                self.format_code = _build_code(*self.formats_used)
                self.rgbcode = "48;2;" + self.bg
                self.finalcode = self.format_code + ";" + self.rgbcode
                print(f"\033[{self.finalcode}m{text}\033[0m")
        else:
            if self.bg == "":
                self.format_code = _build_code(*self.formats_used)
                self.rgbcode = "38;2;" + self.fg
                self.finalcode =  self.format_code + ";" + self.rgbcode
                print(f"\033[{self.finalcode}m{text}\033[0m")
            else:
                self.format_code = _build_code(*self.formats_used)
                self.rgbcode = "38;2;" + self.fg + ";48;2;" + self.bg
                self.finalcode = self.format_code + ";" + self.rgbcode
                print(f"\033[{self.finalcode}m{text}\033[0m")
    
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


def printColored(text, *formats_used):
    text = _font_check(text, *formats_used)
    code = _build_code(*formats_used)
    print(f"\033[{code}m{text}\033[0m")


def colorGen(*formats_used, mode=""):
    code = _build_code(*formats_used)
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
        if code == None:
            print(f"{line}\033[0m" + sepr, end="\n" if i == len(text) - 1 else "")
        else:
            print(f"\033[{code}m{line}\033[0m" + sepr, end="\n" if i == len(text) - 1 else "")
        
# printl is the replacement of colorGen
# its WAY WAYYYY simpler, and takes less space to write
# Dunno if i should keep colorGen, but ill just leave it there because
# it returns the color code itself

def printRGB(text, r,g,b, *formats_used, view=""):
    text = _font_check(text, *formats_used)
    code = _build_code(*formats_used)    
    # if you dont want a format when using the rgb function,
    # you can just enter ""
    rgbvalue = _rgb_validation(r,g,b)
    if rgbvalue != "":
        viewvalue = "48;" if view.lower() == "bg" else "38;"
    else:
        viewvalue = ""

    if code != "":
        code += ";"
    print(f"\033[{viewvalue}2;{rgbvalue}{code}m{text}\033[0m")

def printRGBV(text, r,g,b, r2, g2, b2, *formats_used):
    text = _font_check(text, *formats_used)
    code = _build_code(*formats_used)

    fg = _rgb_validation(r,g,b)
    bg = _rgb_validation(r2,g2,b2)
    if code != "":
        code += ";"

    if fg == "":
        if bg == "":
            print(f"\033[{code}m{text}\033[0m")
        else:
            print(f"\033[{code}48;2;{bg}m{text}\033[0m")
    else:
        if bg == "":
            print(f"\033[{code}38;2;{fg}m{text}\033[0m")
        else:
            print(f"\033[{code}38;2;{fg};48;2;{bg}m{text}\033[0m")
        

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
        for key, value in Fonter.decorators.items():
            print(f"{key}: {value}")
    else:
        for key, value in formats.items():
           print(f"\033[{value}m{key}\033[0m")

if __name__ == '__main__':
    deco =  Theme("green", "bold")
    deco2 = Theme("bright_blue", "bold")
    deco3 = Theme("bright_yellow")
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
    
    deco.print(border)
    choice = True if input("Do you want to see all Fonter and decorators in the extra file?(Y/N): ").lower() == "y" else False
    if choice:    
        print("All Fonter + decorators available:")
        formatfinder(" ","font")

    deco.print(border)
    
    deco2.print(border)
    print("Guide for using the functions:")
    deco2.print(border)

    # main functions:
    
    # printColored()
    deco.print(border)
    print("Page 1:")
    printColored("Example use of printColored()".center(32), "green","bold","italic")
    print("Main function, enter text, then formats, and the text will come formatted based on the provided formats")
    print("Take a look at the dictionary and enter formats to use")
    deco.print(border)
    input("Press enter to continue...")

    
    # colorGen()
    deco.print(border)
    print("Page 2:")
    print(
        f"{colorGen('red', 'bold')}   Example use "
        f"{colorGen('', 'strikethrough', 'blue')}of colorGen()"
        f"{colorGen('')}"
    )

    
    genformat1 = colorGen("bright_white", "highlightblue")
    genformat2 = colorGen("", "yellow", "highlightgreen", "underline")
    print(f"    {genformat1}Example 2 {genformat2}of colorGen(){colorGen('')}")
    print("This is used to enter many formats in the same line")
    deco.print(border)
    input("Press enter to continue...")


    # printl()
    deco.print(border)
    print("Page 3:")
    printl(("Example", "use", "of", "printl()"),("green", ("36", "italic"), "yellow", "magenta"), sepr=" ")
    print("Printl is used to print many text in same line each with their own formats")
    deco.print(border)
    input("Press enter to continue...")

    # printRGB()
    deco.print(border)
    print("Page 4:")
    printRGB("Example use of printRGB()".center(32), "255", "0", "255", " ", "bold")
    printRGB("Example 2 of printRGB()".center(32), "0", "255", "255", "bg", "")
    print("Notice how it can only display either")
    print("foreground or background at one time")
    print("You can also add formats to it".center(32))
    deco.print(border)
    input("Press enter to continue...")

    
    # printRGBV()
    deco.print(border)
    print("Page 5:")
    printRGBV("Example use of printRGBV()".center(32), "0", "255", "0", "0", "0", "255", "")
    printRGBV("Example 2 of printRGBV()".center(32), "0", "0", "0", "255", "0", "255", "italic")
    print("It can display both foreground and background")
    print("and also add formats".center(32))
    print("Note that sometimes the background")
    print("color blocks the foreground color")
    deco.print(border)
    input("Press enter to continue...")

    
    # Theme
    deco.print(border)
    print("Page 6:")
    deadly = Theme("brightred", "double_underline", "bold")
    deadly.print("Example use of Theme class")
    print("It can be used for formats that you use many times")

    deadly.add("strikethrough")
    deadly.print("Example of add(*formats)")

    deadly.remove("double_underline", "strikethrough")
    deadly.print("Example of remove(*formats)")

    deadly.overwrite("highlight_brightred", "underline")
    deadly.print("Example of overwrite(*formats)")

    deadly.showUsed()
    print("showUsed() displays the current formats")
    deco.print(border)
    input("Press enter to continue...")

    
    # ThemeRGBV
    deco.print(border)
    print("Page 7:")
    classified = ThemeRGBV("255", "255", "255", "0", "0", "0", "")
    classified.print("Example of printRGBV(r,g,b,r2,g2,b2,*formats)")
    print("It can change both foreground and background")
    print("and you can choose to use one or both")

    classified.add("bold", "underline")
    classified.print("Example of add(*formats)")

    classified.remove("underline")
    classified.print("Example of remove(*formats)")
    print("Adding/removing only affects formats")

    classified.overwrite("0", "0", "0", "255", "255", "255", "strikethrough")
    classified.print("Example of overwrite(r,g,b,r2,g2,b2,*new)")
    print("Overwrite rewrites the whole object")

    classified.showUsed()
    print("showUsed() displays the current settings")
    deco.print(border)
    input("Press enter to continue...")


    deco.print(border)
    deco2.print(border)
    print("Thanks for reading!")
    deco2.print(border)

    deco3.print(border)
    print("BONUS: Custom formats using either ANSI or RGB")
    key = "placeholder"
    while key.lower() != "_exit_":
        key = input("Enter new key (_exit_ to leave): ")
        if key.lower() != "_exit_":
            custom_formats[key] = input(f"Enter a value for {key}: ")
            while custom_formats[key].replace(";", "").isdigit() == False:
                print("Invalid code!")
                print("The code must have digits only (; is an exception)")
                custom_formats[key] = input(f"Enter a value for {key}: ")
        else:
            break
    with open("custom.json", "w") as file:
        json.dump(custom_formats, file, indent=4)
    deco3.print(border)