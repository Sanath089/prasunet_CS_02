from PIL import Image
import numpy as np
from termcolor import colored

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    np_image = np.array(image)

    # Simple pixel manipulation: XOR each pixel with the key
    encrypted_image = np_image ^ key

    encrypted_image = Image.fromarray(encrypted_image)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    np_image = np.array(image)

    # Reverse the pixel manipulation: XOR each pixel with the key
    decrypted_image = np_image ^ key

    decrypted_image = Image.fromarray(decrypted_image)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print(colored("   _                                                  __ ", 'red'))
    print(colored("  (_)_ _  ___ ____ ____   ___ ___  __________ _____  / /_", 'green'))
    print(colored(" / /  ' \\/ _ `/ _ `/ -_) / -_) _ \\/ __/ __/ // / _ \\/ __/", 'yellow'))
    print(colored("/_/_/_/_/\\_,_/\\_, /\\__/  \\__/_//_/\\__/_/  \\_, / .__/\\__/", 'blue'))
    print(colored("             /___/                       /___/_/         ", 'magenta'))

    while True:
        mode = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
        if mode not in ('e', 'd'):
            print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        image_path = input("Enter the path to the image: ")
        output_path = input("Enter the path to save the output image (including filename and extension, e.g., output.png): ")
        key = int(input("Enter an integer key for encryption/decryption: "))

        if mode == 'e':
            encrypt_image(image_path, output_path, key)
        else:
            decrypt_image(image_path, output_path, key)

        repeat = input("Do you want to process another image? (y/n): ").lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()
