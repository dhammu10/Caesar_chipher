alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(satrt_text, shift_amount, direction):
    final_text = " "
    if direction == "decode":
        shift_amount *= -1
    for letter in satrt_text:
        position = alphabet.index(letter)

        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        final_text += new_letter
    print(final_text)

loop_end = "Yes"
while loop_end == "Yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(satrt_text=text,shift_amount=shift,direction=direction)
    restart = input("Do you want to run again? type yes/No ")
    if restart == "No":
        loop_end = "No"
        print("Good Byy")
