"""
Stanford CS106AP Warmups
Adapted from Nick Parlante's image warmups by
Sonja Johnson-Yu, Kylie Jue, and Nick Bowman.
"""

"""
This line imports SimpleImage for use here
This line depends on the Pillow package being installed
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename, pixel=1):
    """
    Saturates the "red" pixels and grayscales all other pixels in the
    image in order to highlight areas of wildfires.

    Input:
        filename (string): name of image file to be read in

    Returns:
        highlighted (SimpleImage): image with reddish pixels highlighted
    """
    image = SimpleImage(filename)
    # Your code to highlight the fires goes here
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * 1.05:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = average
            pixel.blue = average
            pixel.green = average
    return image

def reflect(filename):
    """
    Vertically "reflects" an image over the bottom horizontal axis and
    returns an image of twice the original height.

    Input:
        filename (string): name of image file to be read in

    Returns:
        reflected (SimpleImage): reflected image, twice original height
    """
    image = SimpleImage(filename)
    reflected = SimpleImage.blank(width=image.width, height=2*image.height)
    # Your code to reflect the image goes here
    reflected = SimpleImage.blank(image.width, image.height * 2)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_up = reflected.get_pixel(x, y)
            pixel_up.red = pixel.red
            pixel_up.green = pixel.green
            pixel_up.blue = pixel.blue

            pixel_bottom = reflected.get_pixel(x, reflected.height - 1 - y)
            pixel_bottom.red = pixel.red
            pixel_bottom.green = pixel.green
            pixel_bottom.blue = pixel.blue
    return reflected


def main():

    # Comment/uncomment these out as you implement them!
    # When you submit this file, make sure all lines in main are uncommented

    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()

    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
