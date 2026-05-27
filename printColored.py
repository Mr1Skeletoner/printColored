# Usage guide on github
# thank you for using my code, it means alot to me ^-^
# if you want to talk to me about anything, or a question, dm me on discord, the user is: 1skeletoner
# also if you would like to help you can dm me an additional format or color not in my code
# thanks :)

formats = {
    # Colors
    "gray": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",

    # Highlight
    "highlight_red": "41",
    "highlight_green": "42",
    "highlight_yellow": "43",
    "highlight_blue": "44",
    "highlight_magenta": "45",
    "highlight_cyan": "46",
    "highlight_gray": "47",

    # Format (like bold or italic)
    "bold": "01",
    "italic": "03",
    "underline": "04",
    "inverted": "07",
    "invisible": "08",
    "strikethrough": "09",
    "double_underline": "21",

    "nothing": "0", # placeholder or smth idk i dont even use it bc u can just type 0 but i will just keep it there
}


def printColored(endl, text, *format,):
    if endl == "form dict" or text == "form dict" or format=="form dict":
        for key, value in formats.items():
           print(f"\033[{value}m{key}\033[0m")
    else:
        format_code = ";".join(formats[name] for name in format)
        endlT = endl if endl != "" else None
        print(f"\033[{format_code}m{text}\033[0m", end=endlT)

if __name__ == '__main__':
    print("All available formats:")
    printColored("form dict","","")
