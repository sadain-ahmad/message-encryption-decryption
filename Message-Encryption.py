import random
import string

# message Input
message = input("Enter your message : ")

# input code or Decode
choice = int(input("1: Press 1 to encrypt the message\n2: Press 2 to decrypt the message : "))

# to store the final output
final_message = ""

# spllit the string into tokens to the all tokens easily
words = message.split()

########  M A I N    L O G I C  #############

# Message Encrypting Part
if (choice==1):
    # performing operations on one token/word
    for token in words:

        # random letters to code or decode the tokens
        r1 = r2 = ""
        for i in range(3):
            r1 = r1 + random.choice(string.ascii_letters)
            r2 = r2 + random.choice(string.ascii_letters)
            
        # if there are 5 ar more than 5 characters in a word, then we add three random letters in the start and the end, the first two letters would be replaced by the last two letters and the remaining word will be same, and than append it back to the final_message.
        if (len(token)>=5):
            new_word = r1 + token[-2:] + token[2:-2] + token[0:2] + r2
            final_message += new_word + " "

        # if there are 3 ar more than 3 characters in a word, then we add three random letters in the start and the end, the first letter would be replaced by the last letter and the remaining word will be same, and than append it back to the final_message.
        elif (len(token)>=3):
            new_word = r1 +token[-1] + token[1:-1] + token[0] + r2
            final_message += new_word + " "

        # if there are less than 3 characters in the string than we simply reverse it, and than append it back to the final_message.
        else:
            new_word = token[::-1]
            final_message += new_word + " "

# Message Decrypting Part
elif (choice==2):
    # perform operatioin on tokens/words
    for token in words:
        # if the word contain 11 or more than 11 characters than we remove the first three and the last three letters, and than the first two letters would be replaced by the last two letters and the remaining letters would be same, and than append it back to the final_message.
        if (len(token)>=11):
            new_word = token[-5:-3] + token[5:-5] + token[3:5]
            final_message += new_word + " "

        # if the word contain 9 or more than 9 characters than we remove the first three and the last three letters, and than the first letter would be replaced by the last letter and the remaining letters would be same, and than append it back to the final_message.
        elif (len(token)>=9):
            new_word = token [-4] + token[4:-4] + token[3]
            final_message += new_word + " "
        
        # if there are less than 9 letters in  a single word than we simply reverse it, and than append it back to the final_message. 
        else:
            new_word = token[::-1]
            final_message += new_word + " "
        
# Display the final message after performing operations.
print(final_message)