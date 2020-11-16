
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

answer = ''

for char in range(len(message)):
    if message[char] is not None:
        character = message[char]           #get character
        character_bin = bin(ord(character)) #get decimal value of chacter
        character_bin = character_bin[2:]   #get binary value of character

        bin_digit = ''                      #blank out the digit being compared each binary character update
        print(character_bin[0])
        while character_bin is not None:
            locator = 0
            bin_digit = character_bin[0]
            
            if bin_digit == '1':
                answer = answer + '0 '
            elif bin_digit == 0:
                answer = answer + '00 '
            else:
                answer = answer + ' ' 

            if character_bin[0] == '0' or character_bin[0] == '1':
                while bin_digit == character_bin[0]:
                    answer = answer + '0'
                    character_bin = character_bin[1:]
            else:
                character_bin = None
        print(answer)
            
    message = message[1:]

print(answer)
