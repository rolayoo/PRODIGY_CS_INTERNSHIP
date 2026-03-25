def encrypt_decrypt(text, shift_key, mode):
    result = ""
    
    # If the user wants to decrypt, we simply reverse the shift direction
    if mode == 'decrypt':
        shift_key = -shift_key
        
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if the letter is uppercase or lowercase to keep the formatting
            ascii_offset = 65 if char.isupper() else 97
            
            # Apply the shift and wrap around the alphabet using modulo 26
            new_char = chr((ord(char) - ascii_offset + shift_key) % 26 + ascii_offset)
            result += new_char
        else:
            # If it's a space, number, or symbol, leave it as is
            result += char
            
    return result

# Main program loop
print("=== Caesar Cipher Tool ===")
while True:
    mode = input("\nWould you like to 'encrypt' or 'decrypt'? (Type 'exit' to quit): ").lower()
    
    if mode == 'exit':
        print("Goodbye!")
        break
        
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please type 'encrypt', 'decrypt', or 'exit'.")
        continue
        
    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Please enter a valid number for the shift.")
        continue
        
    # Call the function and print the result
    output = encrypt_decrypt(message, shift, mode)
    print(f"\nResult: {output}")
    print("-" * 25)