from .core import *

_deco = Theme("green", "bold")
_deco2 = Theme("bright_blue", "bold")
_deco3 = Theme("bright_yellow")
_border = "--------------------------------"


def _guide_printColored():
    _deco.print(_border)
    print("printColored()")
    printColored("Example use of printColored()".center(32), "green", "bold", "italic")
    print("Main function, enter text, then formats, and the text will come formatted based on the provided formats")
    print("Take a look at the dictionary and enter formats to use")
    _deco.print(_border)


def _guide_colorGen():
    _deco.print(_border)
    print("colorGen()")
    print(
        f"{colorGen('red', 'bold')}   Example use "
        f"{colorGen('', 'strikethrough', 'blue')}of colorGen()"
        f"{colorGen('')}"
    )

    genformat1 = colorGen("bright_white", "highlight_blue")
    genformat2 = colorGen("", "yellow", "highlight_green", "underline")
    print(f"    {genformat1}Example 2 {genformat2}of colorGen(){colorGen('')}")
    print("This is used to enter many formats in the same line")
    _deco.print(_border)


def _guide_printl():
    _deco.print(_border)
    print("printl()")
    printl(("Example", "use", "of", "printl()"), ("green", ("36", "italic"), "yellow", "magenta"), sepr=" ")
    print("Printl is used to print many text in same line each with their own formats")
    _deco.print(_border)


def _guide_printRGB():
    _deco.print(_border)
    print("printRGB()")
    printRGB("Example use of printRGB()".center(32), "255", "0", "255", "bold", view="")
    printRGB("Example 2 of printRGB()".center(32), "0", "255", "255", view="bg")
    print("Notice how it can only display either")
    print("foreground or background at one time")
    print("You can also add formats to it".center(32))
    _deco.print(_border)


def _guide_printRGBV():
    _deco.print(_border)
    print("printRGBV()")
    printRGBV("Example use of printRGBV()".center(32), "0", "255", "0", "0", "0", "255", "")
    printRGBV("Example 2 of printRGBV()".center(32), "0", "0", "0", "255", "0", "255", "italic")
    print("It can display both foreground and background")
    print("and also add formats".center(32))
    print("Note that sometimes the background")
    print("color blocks the foreground color")
    _deco.print(_border)


def _guide_theme():
    _deco.print(_border)
    print("Theme")
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
    _deco.print(_border)


def _guide_theme_rgbv():
    _deco.print(_border)
    print("ThemeRGBV")
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
    _deco.print(_border)


GUIDE = {
    "printColored": _guide_printColored,
    "colorGen": _guide_colorGen,
    "printl": _guide_printl,
    "printRGB": _guide_printRGB,
    "printRGBV": _guide_printRGBV,
    "Theme": _guide_theme,
    "ThemeRGBV": _guide_theme_rgbv,
}


def func_guide(selected_function=None):
    if selected_function:
        if selected_function in GUIDE:
            GUIDE[selected_function]()
        else:
            raise ValueError(f"{selected_function} Not a valid guide section!")
    else:
        for section in GUIDE:
            GUIDE[section]()
        _deco.print(_border)
        _deco2.print(_border)
        print("Thanks for reading!")
        _deco2.print(_border)