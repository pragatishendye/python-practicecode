"""
This program implements Caesar's Cipher - the simplest encryption technique.
Created by Pragathi Shendye
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(message, key, action):
    new_msg = list()
    for letter in message:
        if letter not in alphabet:
            new_msg.append(letter)
        else:
            current_index = alphabet.index(letter)
            if action == "encode":
                new_index = current_index + key
                while new_index > 25:                       # for indexes exceeding the alphabet list due to large key value
                    new_index -= 26
            else:
                new_index = current_index - key
                while new_index < -26:                      # for indexes exceeding the alphabet list due to large key value
                    new_index += 26
            new_msg.append(alphabet[new_index])

    cipher = ''.join(new_msg)
    print(f"The {action}d text is: {cipher}")


go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("Invalid operation")
    repeat = input("Type 'yes' to go again, else type 'no': ")
    if repeat == "no":
        go_again = False
        print("Goodbye!")
