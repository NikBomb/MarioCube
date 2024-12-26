from PIL import Image
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
image_path = "star/pixil-frame-2.png"  # Replace with your image path
output_txt_path = "star_1.txt"
rotation_angle = 0  # Rotation angle in degrees (e.g., 0, 90, 180, 270)
size = None , None  # Set custom size if needed, e.g., (16, 16)

# --- LOAD IMAGE ---
# Open the image
image = Image.open(image_path)


# Rotate the image
image = image.rotate(rotation_angle, expand=True)

# Resize the image if dimensions are provided
#if size:
#    image.thumbnail(size)
# Show the image for preview
plt.imshow(image)
plt.axis("off")  # Remove axis for a cleaner view
plt.title("Preview of the Image for LEDs")
plt.show()

# Convert the image to RGB
image = image.convert("RGB")
width, height = image.size

# --- PROCESS IMAGE AND WRITE FILE ---
with open(output_txt_path, "w") as txt_file:
    for y in range(height):
        row_pixels = []
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            # Convert to 32-bit hexadecimal in 0xAARRGGBB format (alpha is always FF)
            hex_32bit = f"0xFF{r:02X}{g:02X}{b:02X}"
            row_pixels.append(hex_32bit)
        
        # Reverse even rows for serpentine layout
        if y % 2 != 0:
            row_pixels.reverse()
        
        # Write row to file
        txt_file.write(", ".join(row_pixels) + ",\n")
image.save("processed.png")
print(f"Serpentine 32-bit hex color codes written to {output_txt_path}")