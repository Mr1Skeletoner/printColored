

from random import *

fonts: dict[str, tuple[str, ...]] = {
    "original": ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","0","1","2","3","4","5","6","7","8","9","!","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~"),
    
    # act like theres stuff here


}

random_decorators: dict[str, tuple[str, str]] = {
    "chess": (""),
}

decorators: dict[str, tuple[str, str]] = {
    "barrier": (""),
    
}



def Fonter(text: str, font: str, decorator: str = "") -> str:
    original = fonts["original"]
    fontedtext = []
    for letter in text:
        fontedtext.append(fonts[font][original.index(letter)] if letter in original else letter)
    result = "".join(fontedtext)
    if decorator == "":
        return result
    return f"{decorators[decorator][0]}{result}{decorators[decorator][1]}"
