from PIL import Image
import os

# --- CONFIGURATION ---
gif_path = "star.gif"  # Replace with your GIF file path
output_folder = "star"     # Folder to save the resized frames
frame_size = (16, 16)            # Target size for each frame (16x16)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Open the GIF file
gif = Image.open(gif_path)

# Process each frame in the GIF
frame_index = 0
while True:
    # Resize the current frame to 16x16
    resized_frame = gif.resize(frame_size, Image.ANTIALIAS)
    
    # Save the resized frame as a PNG file
    frame_path = os.path.join(output_folder, f"frame_{frame_index:03d}.png")
    resized_frame.save(frame_path, format="PNG")
    print(f"Saved frame {frame_index} as {frame_path}")
    
    frame_index += 1
    
    try:
        # Move to the next frame in the GIF
        gif.seek(frame_index)
    except EOFError:
        # No more frames in the GIF
        break

print(f"All frames resized and saved to '{output_folder}'.")