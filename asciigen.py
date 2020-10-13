from PIL import Image, ImageDraw, ImageOps
import numpy as np
import random
import sys
from typing import List


def module_help():
    """ Display usage of module """
    print(f'Usage: {__file__} <from_path> [to_path=out.txt] [size=200x200] [mode=simple|complex]')


def char_score(char: str) -> int:
    """ calculates the fill rate of a character.

    :param char: Character to print
    :return: Filling rate
    """
    img = Image.new('L', (20, 20))
    d = ImageDraw.Draw(img)
    d.text((2, 0), char, fill=(255), align='center')

    return np.array(img.getdata()).reshape((20, 20)).mean()


def picture_to_ascii(from_path: str, to_path: str, size: str = '200x200', mode: str = 'simple') -> None:
    """ Convert picture to ascii art and write it into output text file.

    :param from_path: Path to the picture
    :param to_path: Path to output text file
    :param size: Size of ascii art
    :param mode: Complexity of ascii art (10 or 95 chars)
    """
    if mode == 'simple':
        ascii_chars = '@#%*+=-:. '
    else:
        ascii_chars = ''.join([chr(i) for i in range(32, 127)])

    scores = {char: char_score(char) for char in ascii_chars}
    max_score = max(scores.values())
    scores = {char: 1 - score / max_score for char, score in scores.items()}

    simon = Image.open(from_path)

    output_size = tuple(int(x) for x in size.split('x'))

    simon = ImageOps.grayscale(simon.resize(output_size))

    data = np.array(simon.getdata())
    data -= data.min()
    data = (data / data.max()).reshape(output_size[::-1])

    img = Image.fromarray(data * 255)
    img.convert('RGB').resize((300, 300))

    results = []
    for line in data:
        new_line = ''
        for v in line:
            matches = []
            best_match = 100
            for char, score in scores.items():
                diff = abs(v - score)
                if diff < best_match:
                    best_match = diff
                    matches = [char]
                elif diff == best_match:
                    matches.append(char)
            new_line += random.choice(matches)
        results.append(new_line)
    result = '\n'.join(results)

    with open(to_path, 'w') as file:
        file.write(result)


def main(args: List[str]) -> None:
    """ Convert call arguments into parameters and call picture_to_ascii function.

    :param args: List of arguments
    """
    l_args = len(args)
    if l_args >= 1:
        from_path = args[0]
        to_path = 'out.txt'
        size = '200x200'
        mode = 'simple'

        if l_args >= 2:
            to_path = args[1]
            if l_args >= 3:
                size = args[2]
                if l_args >= 4:
                    mode = args[3]

        picture_to_ascii(from_path, to_path, size, mode)
    else:
        module_help()


if __name__ == '__main__':
    main(sys.argv[1:])
