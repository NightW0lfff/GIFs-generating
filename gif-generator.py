import imageio

# List of image file paths you want to include in the GIF
image_paths = ['image1.png', 'image2.png', 'image3.png'] # Add as many images as you want

# Create a writer object specifying the output GIF file
with imageio.get_writer('my_animation.gif', mode='I', duration=500, loop=0) as writer:
    for image_path in image_paths:
        image = imageio.imread(image_path)
        writer.append_data(image)

print("GIF created successfully!")