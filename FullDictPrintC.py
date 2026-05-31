# this is the version which has ALL formats including ones that dont work or ones that are useless

formats = {
    # Reset
    "reset": "0",

    # Text styles
    "bold": "1",
    "dim": "2",
    "italic": "3",
    "underline": "4",
    "slow_blink": "5",
    "rapid_blink": "6",
    "invert": "7",
    "hidden": "8",
    "strikethrough": "9",

    # Style resets
    "double_underline": "21",
    "normal_intensity": "22",
    "italic_off": "23",
    "underline_off": "24",
    "blink_off": "25",
    "invert_off": "27",
    "hidden_off": "28",
    "strikethrough_off": "29",

    # Foreground colors
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    "default_foreground": "39",

    # Background colors
    "bg_black": "40",
    "bg_red": "41",
    "bg_green": "42",
    "bg_yellow": "43",
    "bg_blue": "44",
    "bg_magenta": "45",
    "bg_cyan": "46",
    "bg_white": "47",
    "default_background": "49",

    # Decorations
    "framed": "51",
    "encircled": "52",
    "overlined": "53",
    "frame_encircle_off": "54",
    "overline_off": "55",

    # Bright foreground colors
    "bright_black": "90",
    "bright_red": "91",
    "bright_green": "92",
    "bright_yellow": "93",
    "bright_blue": "94",
    "bright_magenta": "95",
    "bright_cyan": "96",
    "bright_white": "97",

    # Bright background colors
    "bg_bright_black": "100",
    "bg_bright_red": "101",
    "bg_bright_green": "102",
    "bg_bright_yellow": "103",
    "bg_bright_blue": "104",
    "bg_bright_magenta": "105",
    "bg_bright_cyan": "106",
    "bg_bright_white": "107"
}

def printColored(endl, text, *format,):
    if endl == "form dict" or text == "form dict" or format=="form dict":
        for key, value in formats.items():
           print(f"\033[{value}m{key}\033[0m")
    else:
        format_code = ";".join(formats[name] for name in format)
        endlT = endl if endl != "" else None
        print(f"\033[{format_code}m{text}\033[0m", end=endlT)

def test_finder(): # made this to find new formats, theres nothing beyond 107
    for code in range(1, 108):
        print(f"At iteration {code}: \033[{code}mHello World!\033[0m")

if __name__ == '__main__':
    print("All available formats:")
    printColored("form dict","","")
    print("All possible formats in range of 1-107 (reason that some of these arent available is that most of them are useless):")
    test_finder()
