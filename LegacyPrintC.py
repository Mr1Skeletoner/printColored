# stupid legacy version
# who would ever use this piece of
# note that this wont be updated anymore after updating the dictionary to the latest version

formats = {
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

    # Format (like bold or italic)
    "bold"            : "01",
    "italic"          : "03",
    "underline"       : "04",
    "inverted"        : "07", # inverted and highlight white are probably the same lol
    "invisible"       : "08",
    "strikethrough"   : "09",
    "double_underline": "21",

    "nothing": "0" # placeholder or smth idk i dont even use it bc u can just type 0 but i will just keep it there
}


def printColored(endl, endlast,*text, **format,):
    if endl == "form dict" or text == "form dict" or format=="form dict":
        for key, value in formats.items():
           print(f"\033[{value}m{key}\033[0m")
    else:
        endlT = endl if endl != "" else None
        format_values = list(format.values())
        x = [1]
        for each_text, format_type, i in zip(text, format_values, x):
            if endlast == "":
                if i != len(text) - 1:
                    format_code = formats.get(format_type)
                    print(f"\033[{format_code}m{each_text}\033[0m", end="")
                else:
                    format_code = formats.get(format_type)
                    print(f"\033[{format_code}m{each_text}\033[0m", end=endlT)
            else:
                format_code = formats.get(format_type)
                print(f"\033[{format_code}m{each_text}\033[0m", end=endlT)
                    
# x and i are placeholders
# if you remove any of them, the code will break
# they specifically work for the endline thing

if __name__ == '__main__':
    print("All available formats:")
    printColored("form dict","","")
