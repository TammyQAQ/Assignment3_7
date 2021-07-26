"""
Stanford CS106AP Parse Mystery Project
Adapted from Nick Parlante's version of Parse Mystery
Written by Sonja Johnson-Yu, Kylie Jue, and Nick Bowman.

YOUR DESCRIPTION HERE
"""

import sys

"""
This line imports SimpleImage for use here
This line depends on the Pillow package being installed
"""
from simpleimage import SimpleImage


def decorrupt_red(s):
    """
    Given a string, remove non-numeric characters and return the
    resulting int.

    Input:
        s (string): string to be processed
    Returns:
        red (int): red value extracted from string
    >>> decorrupt_red('ake&1js4ls5')
    145
    >>> decorrupt_red('111')
    111
    >>> decorrupt_red('f9s')
    9
    """
    pass


def decorrupt_green(s):
    """
    Given a string, change 'a's to 1's, reverse the string and return
    the resulting int.

    Input:
        s (string): string to be processed
    Returns:
        green (int): green value extracted from string
    >>> decorrupt_green('602')
    206
    >>> decorrupt_green('7')
    7
    >>> decorrupt_green('78a')
    187
    """
    pass


def decorrupt_blue(s):
    """
    Given a string, retrieve the string between the two ^'s and return
    the resulting int.

    Input:
        s (string): string to be processed
    Returns:
        blue (int): blue value extracted from string

    >>> decorrupt_blue('asd^6^n')
    6
    >>> decorrupt_blue('^213^')
    213
    >>> decorrupt_blue('2349^67^')
    67
    """
    pass


def parse_line(line):
    """
    Given a string, parse the RGB values out of it and return them as a
    list of int values. You can assume that the number of RGB values
    in a line is always a multiple of 3 and the order is always
    red, green, blue.

    Input:
        line (string): string to be processed containing corrupted RGB values
    Returns:
        rgb_values (List[int]): red, green, and blue values from string

    >>> parse_line('asd56as&* 93a sdffbsdf^200^asd')
    [56, 139, 200]
    >>> parse_line('45 54 *(&^45^')
    [45, 45, 45]
    >>> parse_line('j78 32 *$^240^8 k79 32a asd^32^hg')
    [78, 23, 240, 79, 123, 32]
    """
    pass


def parse_file(filename):
    """
    Given a filename, parse out and return a list containing
    the width and the height of the image followed by all of the RGB
    values contained in the file.

    Input:
        filename (string): file containing corrupted RGB values
    Returns:
        rgb_values (List[int]): list where the first two values are
        width and height of image, followed by list of red, green,
        and blue values
    """
    pass


def solve_mystery(filename):
    """
    Solve the mystery as described in the handout.
    Display image hidden in corrupted text file.
    """

    # SimpleImage boilerplate provided as a starting point
    rgb_values = parse_file(filename)

    ### YOUR CODE HERE ###
    width = 0  # FIXME
    height = 0  # FIXME

    ### YOUR CODE ENDS HERE ###

    image = SimpleImage.blank(width, height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            ### YOUR CODE HERE ###
            # manipulate pixel in here


            ### YOUR CODE ENDS HERE ###

    # This displays image on screen
    image.show()


def main():
    # (provided code, DO NOT MODIFY)
    # Command lines:
    # 1. -nums file.txt -> prints numbers
    # 2. file.txt -> shows image solution
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-nums':
        nums = parse_file(args[1])
        print(nums)
    if len(args) == 1:
        solve_mystery(args[0])


if __name__ == '__main__':
    main()
