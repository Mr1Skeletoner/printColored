# Removed stuff with the endline to make it simpler
# this will be the main version
# the other wont get updates i give up (except if i feel like it)
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

def printColored(text, *format):
    format_code = ";".join(formats[name] for name in format)
    print(f"\033[{format_code}m{text}\033[0m")

def customColor(text, *code): # this removes the need for the version with all useless formats
    code = ";".join(code)
    print(f"\033[{code}m{text}\033[0m")

def generator(*format):
    code = ";".join(formats[name] for name in format)
    return f"\033[{code}m"

# generator is the replacement of the legacy function
# its WAYYY simpler, but takes alot of space to write
# btw the legacy function was broken sooo
# now generator is also fixed

def customgenerator(*code): # specifically made for rgb
    code = ";".join(code)
    return f"\033[{code}m"

def printRGB(text, r, g, b, view, *format):
    code = ";".join(formats[name] for name in format) 
    # if you dont want a format when using the rgb function,
    # you can just enter ""
    rgbvalue = ";".join([r,g,b])
    viewvalue = "48" if view.lower() == "bg" else "38"
    if code == "0":
        print(f"\033[{viewvalue};2;{rgbvalue}m{text}\033[0m")
    else:
        print(f"\033[{viewvalue};2;{rgbvalue};{code}m{text}\033[0m")

def printRGBV(text, r, g, b, r2, g2, b2, *format):
    code = ";".join(formats[name] for name in format) 

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
    choice = True if input("Do you want to see all available formats?(Y/N): ").lower() == "y" else False
    if choice:
        print("All available formats:")
        formatfinder(" "," ")
    choice = True if input("Do you want to see all existing formats in range 1-107?(Y/N): ").lower() == "y" else False
    if choice:    
        print("All possible formats in range of 1-107:")
        formatfinder("1","107")
    
    # main functions:

    # printColored()
    printColored("Example use of printColored()", "green","bold","italic")
    # customColor()
    customColor("Example use of customColor()", "02", "04")

    # generators (why did i name it generator?):

    # generator()
    print(
        f"{generator("red", "bold")}Example use "
        f"{generator("","strikethrough","blue")}of generator()"
        f"{generator("")}"
    )

    # this method is way better
    genformat1 = generator("bright_white","highlight_blue")
    genformat2 = generator("", "yellow", "highlight_green", "underline")
    print(f"{genformat1}Example 2 {genformat2}of generator(){generator("")}")

    # customgenerator()
    print(
        f"{customgenerator("38","2","255","255","0")}Example use "
        f"{customgenerator("0","48","2","0","0","255")}of customgenerator()"
        f"{customgenerator("0")}"
    )

    genformat3 = customgenerator("38","2","90","50","100","3")
    genformat4 = customgenerator("0","48","2","60","60","255")
    print(f"{genformat3}Example 2 {genformat4}of customgenerator(){customgenerator("0")}")


    # the rgb functions (you can either try your luck to get a good color, or find it online)

    # printRGB() 
    printRGB("Example use of printRGB()", "255","0","255", " ", "bold")
    printRGB("Example 2 of printRGB()", "0","255","255", "bg", "")

    # printRGBV()
    printRGBV("Example use of printRGBV()", "0","255","0", "0","0","255", "")
    printRGBV("Example 2 of printRGBV()", "0","0","0", "255", "0", "255", "italic")
    # Note that sometimes the background color blocks the foreground color
