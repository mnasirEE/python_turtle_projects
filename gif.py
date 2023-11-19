from PIL import Image, ImageDraw

# Set up the dimensions and frames
width, height = 200, 200
num_frames = 20

# Create a list to store the frames
frames = []

# Generate frames
for i in range(num_frames):
    # Create a new image for each frame
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw something on each frame (e.g., a moving circle)
    x, y = i * 10, height // 2
    radius = 10
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill="blue")

    # Append the frame to the list
    frames.append(image)

# Save the frames as a GIF
frames[0].save("animated_circle.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
