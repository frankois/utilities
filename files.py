# -*- coding: utf-8 -*-

""" Files utility scripts.
Perform tasks accross files such are renaming, moving, copying...
"""

import click
import os
import pprint
import sys

@click.command()
@click.argument('directory_path', default="directory")
@click.argument('old_extension', default=".old")
@click.argument('new_extension', default=".new")
def rename_all_file_extensions(directory_path, old_extension, new_extension):
    """Rename all files replacing the old extension with the new one."""

    print(f'The extensions `.{old_extension}` in the directory `{directory_path}` '
          f'will be replaced by `.{new_extension}`')
    os.chdir(directory_path)
    files = os.listdir()
    files_to_be_renamed = []
    for elt in files:
        filename, extension = elt.split(".")

        if extension == old_extension:
            new_filename = f'{filename}.{new_extension}'
            files_to_be_renamed.append((elt, new_filename))

    print(f'The following files will be renamed')
    pprint.pprint(files_to_be_renamed)

    if not input("Do you want to proceed? (y/n): ").lower().strip()[:1] == "y": sys.exit(1)

    for elt in files_to_be_renamed:
        os.rename(elt[0], elt[1])
    print('Those have been renamed as requested Boss!')


if __name__ == "__main__":
    print("This should not be called as a module but rather as a command line.")