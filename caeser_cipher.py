print("=================================================\n\n\n", "Caesar cipher".center(40),
      " \n\n\n================================================")
print("""Here's how it works:

Choose a shift value: This is the number of positions each letter will be moved. For example, with a shift value of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.
Apply the shift: Slide each letter in the message down the alphabet by the chosen shift value. Wrap around to the beginning of the alphabet if you reach the end.
Decrypting: To decode the message, simply shift each letter back up the alphabet by the same amount.\n
Here's an example:
Plaintext: "HELLO WORLD"
Shift value: 3
Ciphertext: "KHORZRUOG" \n""")

inputter = input("Enter the  secret word : ")
shifting = int(input("Enter the number for shifting : "))

def choosing ():
    print("Select  number for de/encryption method of caeser cipher (1/2) : ")
    choice = int(input())
    if choice == 1:
        decryption(inputter, shifting)
    elif choice == 2:
        encryption(inputter,shifting)

def decryption(str,num):
    decipherisied = ""
    for i in str :
        if i.isspace():
            continue
        else:
            if ord(i) >= ord("Z") or ord(i) >= ord("z"):
                coder = ord(i) -num
                decipherisied +=chr(coder)
    print("========================","\nDecipherised text: ",decipherisied,"\n========================")

def encryption(str, num):
 cipherisied = ""
 for i in str:
        if i.isspace():
            continue
        else:
            if ord(i) >= ord("Z") or ord(i) >= ord("z"):
                coder = ord(i) + num
                cipherisied += chr(coder)
 print("========================","\nCipherised text: ",cipherisied,"\n========================")


while inputter != "quit":
    choosing()
    # encryption(inputter, shifting)
    print("Do you want to try again ? (y/n)")
    a = input("Enter string : ")
    if a == "y":
        choosing()
        # encryption(inputter, shifting)
    else:
         break
