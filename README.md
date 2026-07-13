# *printColored*

<img width="777" height="98" alt="Untitled" src="https://github.com/user-attachments/assets/94ce30f1-177d-4812-9483-9459a7260b3b" />

Simple library to change how text looks in many colors and formats.

Using ANSI formats in a dictionary to format text, with currently 41 formats

<img width="202" height="600" alt="image" src="https://github.com/user-attachments/assets/fb02dab7-aa38-447d-94dc-e93988607e0c" />

<img width="130" height="138" alt="image" src="https://github.com/user-attachments/assets/5d94efe4-664b-46a9-8162-734e4e354778" />

You can DM me for any problems on my discord: @1skeletoner

List of functions and classes:

- Formats Dictionary: Containing ANSI codes to format text.

- printColored(text, format): Used to simply format text using ANSI codes from the formats dictionary.
  
- customC(text, *code): Lets you enter the ANSI codes on your own, incase a format isnt included in my dictionary.

- Class Theme(*formats): Used for reusing formats many times.

- Class ThemeRGBV(r,g,b, r2,g2,b2, *formats): Same as Class Theme, but for RGB colors.

- generator(*formats): Used for multiple formats on the same line.

- customG(*code): Same as generator, except you enter the codes on your own. Made specifically for RGB.

- printRGB(r,g,b, view, *formats): Mixes the given RGB values, view is where the output color will be displayed, either foreground or background, and can also add formats.

- printRGBV(r,g,b, r2,g2,b2, *formats): Same as printRGB, except that it takes foreground and background at the same time. r,g,b are for foreground, and r2,g2,b2 are for the background.

- formatfinder: Used for finding new formats, but i dont think theres any format that i didnt add. 

# COMPATIBILITY WARNING!!

Be aware that the terminal you use may or may not support the formats, I use VSCode and it works fine.

Terminals that i know do not support ANSI formatting:

- Command prompt

- Running the script directly through python

- Probably most online web editory

- Acode for phone 

----------------------

# *Guide to using printColored function:*

    printColored("text", *"formats")

text is text

formats are how the text is affected. there can be 1 color only at once but multiple styles like bold and italic at the same time

example:

    printColored("Example use of printColored()", "green","bold","italic")

<img width="248" height="49" alt="image" src="https://github.com/user-attachments/assets/4fe5db89-4fb7-436b-9040-750393803d12" />
    

----------------------

# *Guide to using customC function:*

    customC("text", "code")

code is the format code you want to use, for example "02" gives you foggy gray, which wasnt in the format dictionary (it is now)

so i guess if you want a format that isnt in the dictionary, you can use this (btw i believe theres all formats in the dictionary now)

(and to find a format that isnt in the dictionary, use the formatfinder(min,max) function

example:

    customC("Example use of customColor()", "02", "04")

<img width="253" height="48" alt="image" src="https://github.com/user-attachments/assets/e0bb5833-91c5-4139-9390-d800ed043e1c" />

---

# *Guide to using formatfinder function:*

    formatfinder(min, max)

use strings in any case (digit or alphabet, use string)

if both the given values are digits, it will print all available formats between the min and max values provided

example:

    formatfinder("1","107")

else, it will print all available formats in the dictionary

example:

    formatfinder(" "," ")


----------------------

# *Guide to using printRGB, printRGBV:*

    printRGB(text, r, g, b, view, *format)

r, g, b are the values of the colors that get mixed to output a new color 

view is either foreground (only text is affected) or background, enter bg for background, anything else for foreground

format is some effect like bold or italic, you can add as much as you want

i dont suggest trying normal colors in format. formats are also optional, you can just add ""

example:

    printRGB("Example use of printRGB()", "255","0","255", "fg", "bold")
    printRGB("Example 2 of printRGB()", "0","255","255", "bg", "")

<img width="252" height="61" alt="image" src="https://github.com/user-attachments/assets/44e1238f-50d1-47da-8b41-ae02df45942b" />

# printRGBV 
    
    printRGBV(text, r, g, b, r2, g2, b2, *format)

r,g,b are for the foreground, r2,g2,b2 are for the background, it was made to add both foreground and background at the same time

format is just like printRGB

example:

    printRGBV("Example use of printRGBV()", "0","255","0", "0","0","255", "")
    printRGBV("Example 2 of printRGBV()", "0","0","0", "255", "0", "255", "italic")

<img width="252" height="61" alt="image" src="https://github.com/user-attachments/assets/f48a136d-7e23-4c96-89c7-25775dbaf67f" />

----------------------

# *Guide to using generator, customgenerator*

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

<img width="251" height="46" alt="image" src="https://github.com/user-attachments/assets/7811422f-4120-4903-9166-b1220f624fd3" />

method 2(WAY easier):

    genformat1 = generator("bright_white","highlight_blue")
    genformat2 = generator("", "yellow", "highlight_green", "underline")
    print(f"{genformat1}Example 2 {genformat2}of generator(){generator("")}")

<img width="255" height="45" alt="image" src="https://github.com/user-attachments/assets/9bfa88b7-1ac7-4c6b-93cd-ab73e1443ac6" />

it works just as legacyprintColored() but easier

# customG()

    customG(*code)

just as customC(), you enter the codes of the formats you want

made to work as legacyprintColored() and output RGB

same 2 methods to use like generator()

method 1:

    print(
        f"{customG("38","2","255","255","0")}Example use "
        f"{customG("0","48","2","0","0","255")}of customG()"
        f"{customG("0")}"
    )

<img width="249" height="44" alt="image" src="https://github.com/user-attachments/assets/749f97e7-c7ed-4e9d-9ec2-f902b1f1116e" />

method 2:

    genformat3 = customG("38","2","90","50","100","3")
    genformat4 = customG("0","48","2","60","60","255")
    print(f" {genformat3}Example 2 {genformat4}of customG(){customG("0")}")

<img width="255" height="49" alt="image" src="https://github.com/user-attachments/assets/bb2f8b77-03c7-4c29-b6a3-4e65b135dee1" />

----------------------

# *Guide to using Theme, ThemeRGBV*

tomorrow...

# *ThemeRGBV*

tomorrow

---

# CHANGELOG

June first update: MORE USELESS FORMATS YAY!!!!

12/06 update: made it wayyyyyyyyyy better

latest update 12/06 put all functions in the same file, and made a separate file for endline stuff that i hate

13/06: removed legacyprintColored and replaced it with generator (legacy function was broken btw)

added new functions (printRGB, printRGBV, generator)

14/06: added customgenerator for rgb uses

11/07: removed the old file, updated readme, next big update will be on like 13/07 or 14/07

14/07: added Theme and ThemeRGBV classes, better instructions in code. full guide on both and remaking readme tomorrow or something

---

# *THANK YOU FOR READING/USING MY CODE!! HOPE IT HELPS!!*
