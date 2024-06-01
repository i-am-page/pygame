from PIL import Image

# Load the images
bg_blue = Image.open("shooting-gallery-pack/PNG/Stall/bg_blue.png")
bg_green = Image.open("shooting-gallery-pack/PNG/Stall/bg_green.png")
bg_red = Image.open("shooting-gallery-pack/PNG/Stall/bg_red.png")
bg_wood = Image.open("shooting-gallery-pack/PNG/Stall/bg_wood.png")

# Get dimensions
width, height = bg_blue.size

# Create a new image with combined width and same height
combined_width = width * 10
combined_height = height * 6
combined_image = Image.new('RGBA', (combined_width, combined_height))

for i in range(10):
    for j in range(6):
        combined_image.paste(bg_blue,(i* width,j* height))
# Paste the images side by side
# combined_image.paste(bg_blue, (0, 0))
# combined_image.paste(bg_green, (width, 0))
# combined_image.paste(bg_red, (width * 2, 0))
# combined_image.paste(bg_wood, (width * 3, 0))

# Save the combined image
combined_image_path = "assets/img/bg_game_blue.png"
combined_image.save(combined_image_path)

combined_image.show()
