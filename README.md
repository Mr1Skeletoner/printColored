June first update: MORE USELESS FORMATS YAY!!!!
also added legacy version to this repository
also added a new version including all formats (useless ones)

*Guide to using (NORMAL, LATEST VERSION "printColored.py" OR "FullDictPrintC", skip for legacy version):*

first, import it like any other file if you use in another code (import it all and not only the function)

import printColored

now, to use the function,

printColored.printColored("endline", "text", *"formats")

endline is the last character at the end of the string, leave empty (without spaces) for new line

text is text

formats are how the string is affected. there can be 1 color only at once but multiple styles like bold and italic at the same time

if you wanna check all formats/styles, you can either check the code or copy paste this:

printColored("form dict","","")

trying to write the statement above on your own may fail because what i wrote has a secret character so just copy paste it

UPD: js run the main file and it will print every format

(if you want a format that isnt available in my dictionary, run the test_finder() function within the range you wish, default is 1:108)

(to apply the format to the dictionary, take the number in the "At iteration X", add it to the dictionary with its name ("name":"X"))



*Guide to using legacy version:*

import if u want

printColored(endl, endlast, *text, **format,)

endl is the last character, make it an empty string for new line

endlast is how the last character acts with 2 modes, make it empty for default, which will display the last character at the end of every string except the last string, which will not have the last character

make it any character for mode 2, which will display the last character on every string, including the last one

text is text, there can be as much text as you want

format is how the string is affected, each text takes 1 format, like this:

printColored(endl, endlast, "Text1", "Text2", format1="red", format2="blue")

it will be like: {"Text1":format1,"Text2":format2}

Text1 will take format1 so it will be red, and text2 will take format2 so it will be blue

THANK YOU FOR READING/USING MY CODE!! HOPE IT HELPS!!
