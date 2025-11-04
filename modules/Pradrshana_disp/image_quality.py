from PIL import Image

# Load the image from file
image_path = "C:/Users/manis/OneDrive/Desktop/mapping_values/82.png"
image = Image.open(image_path)

# Get the image dimensions
width, height = image.size

print(width,height)