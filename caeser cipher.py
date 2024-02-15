print("=================================================\n\n\n","Caesar cipher".center(40)," \n\n\n================================================")
print("""Here's how it works:

Choose a shift value: This is the number of positions each letter will be moved. For example, with a shift value of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.
Apply the shift: Slide each letter in the message down the alphabet by the chosen shift value. Wrap around to the beginning of the alphabet if you reach the end.
Decrypting: To decode the message, simply shift each letter back up the alphabet by the same amount.
Here's an example:

Plaintext: "HELLO WORLD"
Shift value: 3
Ciphertext: "KHORZRUOG" \n\n\n""")
inputter = input("Enter the  secret word : ")
shifting = int(input("Enter the number for shifting : "))

cipherisied = ""
for i in inputter:
    if i.isspace():continue
    else:
       if ord(i)>= ord("Z") or ord(i) >= ord("z"):
         coder = ord(i)+shifting
         cipherisied += chr(coder)

print(cipherisied)
