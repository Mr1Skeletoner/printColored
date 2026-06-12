June first update: MORE USELESS FORMATS YAY!!!!

12/06 update: made it wayyyyyyyyyy better

latest update 12/06 put all functions in the same file, and made a separate file for endline stuff that i hate


*Guide to using printColored function:*

first, import it if you use it in another code

from printColored import *

now, to use the function,

printColored("endline", "text", *"formats")

endline is the last character at the end of the string, leave empty (without spaces) for new line

ENDLINE DOESNT EXIST ANYMORE IN THE MAIN FILE!!

text is text

formats are how the string is affected. there can be 1 color only at once but multiple styles like bold and italic at the same time



*Guide to using customColor function:*

customColor("endline", "text", "code")

endline and text are just same as the main function (printColored)

code is the format code you want to use, for example "02" gives you foggy gray, which wasnt in the format dictionary (it is now)

so i guess if you want a format that isnt in the dictionary, you can use this (btw i believe theres all formats in the dictionary now)

(and to find a format that isnt in the dictionary, use the formatfinder(min,max) function



*Guide to using legacyprintColored function:*

legacyprintColored(endl, endlast, *text, **format,)

endl is the last character, make it an empty string for new line

endlast is how the last character acts with 2 modes, make it empty for default, which will display the last character at the end of every string except the last string, which will not have the last character

make it any character for mode 2, which will display the last character on every string, including the last one

text is text, there can be as much text as you want

format is how the string is affected, each text takes 1 format, like this:

printColored(endl, endlast, "Text1", "Text2", format1="red", format2="blue")

it will be like: {"Text1":format1,"Text2":format2}

Text1 will take format1 so it will be red, and text2 will take format2 so it will be blue



*Guide to using formatfinder function:*

formatfinder(min, max)

use strings in any case (digit or alphabet, use string)

if both the given values are digits, it will print all available formats between the min and max values

else, it will print all available formats in the dictionary



THANK YOU FOR READING/USING MY CODE!! HOPE IT HELPS!!
