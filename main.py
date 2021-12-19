alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print (logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if shift_amount > 26:
    shift_amount = shift_amount % 26
  if cipher_direction == "decode":
    shift_amount *= -1
    
  for char in start_text:
    if char.isalpha() == True:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
      print(f"Here's the {cipher_direction}d result: {end_text}")
    elif char.isnumeric() == True:
      end_text += char
      print(f"Here's the {cipher_direction}d result: {end_text}")
    else:
      end_text += "*"
      print(f"Here's the {cipher_direction}d result: {end_text}")
  print(f"Here's the {cipher_direction}d result: {end_text}")

  againagain = input("Would you like decode / encode sth again?\nType yes or no.")
  while (againagain == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    againagain = input("Would you like decode / encode sth again?\nType yes or no.")
    if againagain == "no":
      break

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)