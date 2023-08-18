name ="p!k@q#r$S%t^u&v"
final = "v!u@t#s%q^k&p"

def convertToASCIIValue(name):
    numbers = ""
    for letter in name:
        numbers += f"{ord(letter)} "
    return numbers

def reverseString(Ascii:str):
    list_ = Ascii.strip().split(" ")
    for i in range(len(list_)):
        for x, l in enumerate(list_):
            if int(list_[i]) > int(l):
                list_[x] = list_[i]
                list_[i] = l
    return list_

def makeLetters(list_):
    l = ""
    for letter in list_:
        
        l += f"{int(letter):c} "
    return l

if __name__ == "__main__":
    letters = convertToASCIIValue("p!k@q#r$S%t^u&v")
    revesAscii = reverseString(letters)
    output = makeLetters(revesAscii).replace(" ", "")
    print(output)