
def get_nemonic(text):
    nemonics = {"a": "Alpha", "b": "Beta", "c": "Charlie", "d": "Delta", "e": "Echo", "f": "Foxtrot", "g": "Golf", "h": "Hotel", "i": "India", "j": "Juliet", "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o": "Oscar", "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango", "u": "Uniform", "v": "Victor", "w": "Wiskey", "x": "X-ray", "y": "Yankee", "z": "Zulu"}
    for item in text:
        if item.lower() in nemonics :
            print(nemonics[item.lower()], end=" ")
        else:
            print(item, end=" ")

get_nemonic("Aiden12")
