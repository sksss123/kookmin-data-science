hdList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

def dToHd(number):

    if number>=16:
        dToHd(number/16)
        number %= 16

    print hdList[number],

a = input("Insert decimal number : ")

print "0x",
dToHd(a)