def ConvertToMorse():
        message = input("please enter a word: ")
        for character in message.upper(): #for each letter in the word print the morse code version of it 
            print (alphabet[character], end=" ")

def ConvertToEnglish():
        message1 = input("please enter your morse code: ")
        for character in message1: #
            print(alphabet[character], end=" ")

alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
   '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
   '$': '...-..-', '@': '.--.-.', ' ': '/'} # all the letters numbers and symbols comverted into morse

choice = input("please press 1 if you want to convert into morse code, or press 2 if you want to convert from morse code: ") #options menu

if choice == "1":
    ConvertToMorse() 

elif choice =="2":
    ConvertToEnglish()
