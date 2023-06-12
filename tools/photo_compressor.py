"""
This file provides functionality to do the following:

1. Compress all photos in the full_res folder to a specified size.
2. Generate the HTML code for the photos
"""
import argparse
import os
import shutil

from PIL import Image

PENTAX_ASPECT_RATIO = 1.5
HTML_TEMPLATE = '<a href="{full_res_path}"><img src="{compressed_path}" /></a>\n'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The folder to compress', type=str)
    parser.add_argument('--width', help='The width to make the output images', default=543, type=int)
    parser.add_argument('--height', help='The height to make the output images', type=int)
    parser.add_argument('--generated-code-file', help='The file to put the generated code into', type=str, default='generated.html')
    args = parser.parse_args()

    # remove trailing slash from
    if args.path.endswith('/'):
        args.path = args.path[:-1]

    # Fill in height if not provided
    if not args.height:
        args.height = int(args.width / PENTAX_ASPECT_RATIO)

    # make sure passed in image folder is a directory
    assert(os.path.isdir(args.path)), f'{args.path} is not a directory'

    return args


def clean_up(input_folder):
    try:
        shutil.rmtree(f'{input_folder}/compressed')
    except FileNotFoundError:
        pass
    os.mkdir(f'{input_folder}/compressed')


def compress_photos(input_folder, width, height):
    for image in os.listdir(input_folder):
        try:
            old_image = Image.open(f'{input_folder}/{image}')
            resized_image = old_image.resize((width, height), Image.ANTIALIAS)
            resized_image.save(f'{input_folder}/compressed/{image}')
        except IsADirectoryError:
            pass
        except OSError:
            pass


def generate_md(input_folder, output_file):
    full_md = ''
    for image in os.listdir(input_folder):
        try:
            Image.open(f'{input_folder}/{image}')
            md_to_append = HTML_TEMPLATE.format(full_res_path=f'{input_folder}/{image}', compressed_path=f'{input_folder}/compressed/{image}' )
            full_md += md_to_append
        except IsADirectoryError:
            pass
        except OSError:
            pass

    with open(output_file, 'w') as f:
        f.write(full_md)

    return full_md


if __name__ == '__main__':
    args = parse_args()
    clean_up(args.path)
    compress_photos(args.path, args.width, args.height)
    generate_md(args.path, args.generated_code_file)
