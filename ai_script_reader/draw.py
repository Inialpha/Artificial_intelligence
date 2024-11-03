from PIL import Image, ImageDraw

# Load the image with the shape
shape_image = Image.open("fa.webp")

# Create a blank staff (or load a staff image)
staff = Image.new('RGB', (200, 120), color='white')
draw = ImageDraw.Draw(staff)

# Draw the staff lines
line_y_positions = [30, 50, 70, 90, 110]  # Positions for the 5 staff lines
for y in line_y_positions:
    draw.line([(10, y), (190, y)], fill='black', width=2)

# Ensure the shape image has an alpha channel (RGBA)
shape_image = shape_image.convert("RGBA")

# Extract the alpha channel as a mask
shape_mask = shape_image.split()[3]  # Get the alpha channel

# Calculate the position to paste the shape
position = (50, line_y_positions[0] - shape_image.size[1] // 2)

# Paste the shape onto the staff using the mask
staff.paste(shape_image, position, mask=shape_mask)

# Save or display the result
staff.show()
staff.save("shape_on_first_line_fixed.png")

