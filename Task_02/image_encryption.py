from PIL import Image

def process_image(input_path, output_path, key, mode):
    # Open the image and force it into standard RGB mode (fixes the PNG error!)
    try:
        img = Image.open(input_path).convert('RGB')
    except FileNotFoundError:
        print(f"Error: Could not find the file '{input_path}'. Please check the name and try again.")
        return

    pixels = img.load()
    width, height = img.size

    # Loop through every single pixel in the image
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # XOR (^) is symmetric. The exact same operation encrypts AND decrypts!
            if mode in ['encrypt', 'decrypt']:
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)
            else:
                print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
                return

    # Save the manipulated image
    img.save(output_path)
    print(f"Success! Your {mode}ed image has been saved as: {output_path}")

def main():
    print("\n--- 🔐 Pro Image Encryption Tool (XOR) ---")
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    path = input("Enter the exact filename of your image (e.g., test.png): ").strip()
    
    try:
        # We limit the key to 255 because RGB values only go up to 255
        key = int(input("Enter an encryption key (a number from 1 to 255): "))
        if key < 1 or key > 255:
            print("Please pick a number between 1 and 255.")
            return
    except ValueError:
        print("Error: The key must be a number.")
        return

    output = "encrypted_image.png" if choice == "encrypt" else "decrypted_image.png"

    process_image(path, output, key, choice)

if __name__ == "__main__":
    main()