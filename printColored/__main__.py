from .core import *

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

    
    genformat1 = colorGen("bright_white", "highlight_blue")
    genformat2 = colorGen("", "yellow", "highlight_green", "underline")
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
    printRGB("Example use of printRGB()".center(32), "255", "0", "255", "bold"," ")
    printRGB("Example 2 of printRGB()".center(32), "0", "255", "255", "","bg")
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