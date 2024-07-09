import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, Label, Frame
import os

# Function to swap pixels in the image array
def swap_pixels(img_array):
    img_array_shape = img_array.shape
    img_flattened = img_array.flatten()
    
    # Swap pixels in chunks of 7
    for i in range(0, img_flattened.shape[0], 7):
        if i + 7 < img_flattened.shape[0]:
            img_flattened[i], img_flattened[i + 6] = img_flattened[i + 6], img_flattened[i]
    
    img_array = img_flattened.reshape(img_array_shape)
    return img_array

# Function to encrypt an image by swapping pixels
def encrypt_image(input_path, output_path):
    # Open image from input path
    img = Image.open(input_path)
    img_array = np.array(img)

    # Encrypt image by swapping pixels
    encrypted_array = swap_pixels(img_array)

    # Save encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)

# Function to decrypt an encrypted image
def decrypt_image(input_path, output_path):
    # Open encrypted image from input path
    img = Image.open(input_path)
    img_array = np.array(img)

    # Decrypt image (same as encryption as per provided code)
    decrypted_array = swap_pixels(img_array)

    # Save decrypted image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)

# Function to open file dialog and return selected image path
def browse_files():
    filename = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return filename

# Function to display encrypted and decrypted images using tkinter
def display_images(encrypted_image_path, decrypted_image_path):
    display_root = tk.Toplevel()
    display_root.title("Encrypted and Decrypted Images")

    frame1 = Frame(display_root)
    frame1.pack(side="left", padx=10, pady=10)
    frame2 = Frame(display_root)
    frame2.pack(side="right", padx=10, pady=10)

    # Open and resize encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_img.thumbnail((400, 400))
    tk_encrypted_img = ImageTk.PhotoImage(encrypted_img)

    # Open and resize decrypted image
    decrypted_img = Image.open(decrypted_image_path)
    decrypted_img.thumbnail((400, 400))
    tk_decrypted_img = ImageTk.PhotoImage(decrypted_img)

    # Display encrypted image
    label1 = Label(frame1, image=tk_encrypted_img)
    label1.image = tk_encrypted_img  
    label1.pack()

    # Display decrypted image
    label2 = Label(frame2, image=tk_decrypted_img)
    label2.image = tk_decrypted_img  
    label2.pack()

    # Handle closing of display window
    def on_closing():
        display_root.destroy()
        root.destroy()

    display_root.protocol("WM_DELETE_WINDOW", on_closing)
    display_root.mainloop()

# Main function to run the program
def main():
    global root
    root = tk.Tk()
    root.withdraw()  # Hide main tkinter window

    # Prompt user to select an image file
    input_image_path = browse_files()
    if not input_image_path:
        print("No file selected")
        root.destroy()
        return

    # Generate paths for encrypted and decrypted images
    encrypted_image_path = os.path.splitext(input_image_path)[0] + "_encrypted.png"
    decrypted_image_path = os.path.splitext(input_image_path)[0] + "_decrypted.png"

    # Encrypt and decrypt the selected image
    encrypt_image(input_image_path, encrypted_image_path)
    decrypt_image(encrypted_image_path, decrypted_image_path)

    # Print status and paths of encrypted and decrypted images
    print(f"Encryption and decryption done!\nEncrypted image saved as: {encrypted_image_path}\nDecrypted image saved as: {decrypted_image_path}")

    # Display encrypted and decrypted images
    display_images(encrypted_image_path, decrypted_image_path)

# Run main function if this script is executed directly
if __name__ == "__main__":
    main()
