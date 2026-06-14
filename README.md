*AI WAS NOT USED TO MAKE ANYTHING IN THIS CODE, EXCEPT 90% OF THE DICTIONARY, AND TEACHING ME HOW TO FORMAT, EVERYTHING ELSE WAS MADE BY ME*

why the dictionary, you may ask? bc it was something that would consume alot of time

----------------------

CHANGELOG

----------------------

June first update: MORE USELESS FORMATS YAY!!!!

12/06 update: made it wayyyyyyyyyy better

latest update 12/06 put all functions in the same file, and made a separate file for endline stuff that i hate

13/06: removed legacyprintColored and replaced it with generator (legacy function was broken btw)

added new functions (printRGB, printRGBV, generator) guide for generators later

14/06: added customgenerator for rgb uses

----------------------

*1. Guide to using printColored function:*

    printColored("text", *"formats")

text is text

formats are how the text is affected. there can be 1 color only at once but multiple styles like bold and italic at the same time

example:

    printColored("Example use of printColored()", "green","bold","italic")
    

----------------------

*2. Guide to using customColor function:*

    customColor("text", "code")

code is the format code you want to use, for example "02" gives you foggy gray, which wasnt in the format dictionary (it is now)

so i guess if you want a format that isnt in the dictionary, you can use this (btw i believe theres all formats in the dictionary now)

(and to find a format that isnt in the dictionary, use the formatfinder(min,max) function

example:

    customColor("Example use of customColor()", "02", "04")

----------------------

*3. Guide to using legacyprintColored function (ONLY IN OLD VERSION(probably doesnt even work anymore)):*

    legacyprintColored(endl, endlast, *text, **format,)

endl is the last character, make it an empty string for new line

endlast is how the last character acts with 2 modes, make it empty for default, which will display the last character at the end of every string except the last string, which will not have the last character

make it any character for mode 2, which will display the last character on every string, including the last one

text is text, there can be as much text as you want

format is how the string is affected, each text takes 1 format, like this:

printColored(endl, endlast, "Text1", "Text2", format1="red", format2="blue")

it will be like: {"Text1":format1,"Text2":format2}

Text1 will take format1 so it will be red, and text2 will take format2 so it will be blue

no example bc i hate this

----------------------

*4. Guide to using formatfinder function:*

    formatfinder(min, max)

use strings in any case (digit or alphabet, use string)

if both the given values are digits, it will print all available formats between the min and max values provided

example:

    formatfinder("1","107")

else, it will print all available formats in the dictionary

example:

    formatfinder(" "," ")

----------------------

*5. Guide to using printRGB, printRGBV:*

    printRGB(text, r, g, b, view, *format)

r, g, b are the values of the colors that get mixed to output a new color 

view is either foreground (only text is affected) or background, enter bg for background, anything else for foreground

format is some effect like bold or italic, you can add as much as you want

i dont suggest trying normal colors in format. formats are also optional, you can just add ""

example:

    printRGB("Example use of printRGB()", "255","0","255", "fg", "bold")
    printRGB("Example 2 of printRGB()", "0","255","255", "bg", "")
    
for printRGBV,
    
    printRGBV(text, r, g, b, r2, g2, b2, *format)

r,g,b are for the foreground, r2,g2,b2 are for the background, it was made to add both foreground and background at the same time

format is just like printRGB

example:

    printRGBV("Example use of printRGBV()", "0","255","0", "0","0","255", "")
    printRGBV("Example 2 of printRGBV()", "0","0","0", "255", "0", "255", "italic")

----------------------

*6. Guide to using generator, customgenerator*

    generator(*format)

replacement of legacyprintColored()

used to format multiple strings in same line with different formats

theres 2 methods to use it

method 1:

    print(
        f"{generator("red", "bold")}Example use "
        f"{generator("","strikethrough","blue")}of generator()"
        f"{generator("")}"
    )

method 2(WAY easier):

    genformat1 = generator("bright_white","highlight_blue")
    genformat2 = generator("", "yellow", "highlight_green", "underline")
    print(f"{genformat1}Example 2 {genformat2}of generator(){generator("")}")

it works just as legacyprintColored() but easier

now, for customgenerator()

    customgenerator(*code)

just as customColored(), you enter the codes of the formats you want

made to work as legacyprintColored() and output RGB

same 2 methods to use like generator()

method 1:

    print(
        f"{customgenerator("38","2","255","255","0")}Example use "
        f"{customgenerator("0","48","2","0","0","255")}of customgenerator()"
        f"{customgenerator("0")}"
    )

method 2:

    genformat3 = customgenerator("38","2","90","50","100","3")
    genformat4 = customgenerator("0","48","2","60","60","255")
    print(f" {genformat3}Example 2 {genformat4}of customgenerator(){customgenerator("0")}")

----------------------

THANK YOU FOR READING/USING MY CODE!! HOPE IT HELPS!!
