from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector
from Enigma import Enigma

print('''==============ENIGMA MACHINE SIMULATION V1 - BUILD BY SAHEER.K================
----------------------------------------------------------------------

LET ME GIVE YOU SOME BRIEFS ABOUT ENIGMA MACHINE!
PLUGBOARD - REPLACES THE LETTER WITH SELECTED LETTER.
ROTOR - THE MAIN PART OF THE MACHINE, THIS WILL ROTATE FOR EVERY LETTER ENCRYPTED
REFLECTOR - IT SENDS THE LETTER CAME OUT OF ROTARS INTO ROTARS AGAIN WITH SOME CHANGE IN LETTER
RING - IT IS USED TO CHANGE THE POSITION OF THE INTERNAL WIRING RELATIVE TO ROTOR.
KEY - A string that will be used as a key

-------------------------------------------------------------------------''')

print('''======================SETTINGS===================
ENTER THE SETTINGS FOR ENIGMA MACHINE''')

#taking inputs from users
print("========================PLUGBOARD==================")
user_input = input("Enter plugboard settings (Format: AN,BF,CU - A will be replaced with N and vice versa)\n> ")
user_input.upper()
user_input_PB = list(map(str, user_input.split(",")))
print("====================++REFLECTOR=====================")
user_input_RE = input("Choose the reflector A or B or C (Default relfector is A) \n>")
print("====================++ROTOR=====================")
user_input = input("choose any 3 rotors from 1, 2, 3, 4, 5\n note:Order of the rotors to be entered accurately (Format: 123)\n>")



#historical engima compnents
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")


#implementing a list of objects to refer rotors
list_of_objects = [I, II, III, IV, V]

#keyboard & plugboard
KB = Keyboard()
PB = Plugboard(user_input_PB)


#evaluvating user inputs
user_input_RE = user_input_RE.upper()
match user_input_RE:
    case "A":
        user_input_RE = A
    case "B":
        user_input_RE = B
    case "C":
        user_input_RE = C
    case "":
        user_input_RE = A

#defining enigma machine
ENIGMA = Enigma(user_input_RE,list_of_objects[int(user_input[0])],list_of_objects[int(user_input[1])],list_of_objects[int(user_input[2])],PB,KB)

#set rings
print("======================RINGS=====================")
print('''Enter the rings settings (Format: 1,2,3)\n note: you can enter any number between 1 to 26 for each ring.''')
x = input('>')
x = [a for a in x.split(",")]
for i in range(len(x)):
    x[i] = int(x[i])
x = tuple(x)
ENIGMA.set_rings(x) #RING SETTINGS TO BE GIVEN OVER SCREEN
#set message key
print("=======================KEY======================")
key = input("Enter the key (Format: CAT)\n>")
ENIGMA.set_key(key) #KEY TO BE ASKED OVER SCREEN

#Testing statements
# ENIGMA.r1.show()
# ENIGMA.r2.show()
# ENIGMA.r3.show()
#encipher letter
# print(ENIGMA.encipher("A"))
#encipher message
print("=======================ENCRYPTION======================")
message = input("Enter the text to encrypt>\n")
# message = "TESTINGTESTINGTESTINGTESTING" #INPUT TO BE TAKEN OVER SCREEN
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)
print("The encrypted text is")
print(">"+cipher_text)
