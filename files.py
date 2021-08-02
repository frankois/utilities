# -*- coding: utf-8 -*-

""" Files utility scripts.
Perform tasks accross files such are renaming, moving, copying...
"""

import click
import os
import pprint
import sys


@click.command()
@click.option('-R', '--recursive', is_flag=True, default=False)
@click.argument('directory_path', default="directory")
@click.argument('old_extension', default=".old")
@click.argument('new_extension', default=".new")
def rename_all_file_extensions(recursive, directory_path, old_extension, new_extension):
    """Rename all files replacing the old extension with the new one."""

    print(f'The extensions `.{old_extension}` in the directory `{directory_path}` '
          f'will be replaced by `.{new_extension}`')

    if not recursive:
        files = os.listdir(directory_path)

    elif recursive:
        files = []
        for (dirpath, _, filenames) in os.walk(directory_path):
            files += [os.path.join(dirpath, file_) for file_ in filenames]

    files_to_be_renamed = []
    for elt in files:
        try:
            file, extension = os.path.splitext(elt)
            if extension == f'.{old_extension}':
                new_filename = f'{file}.{new_extension}'
                files_to_be_renamed.append((elt, new_filename))

        except ValueError:  # not a correct filename
            pass

    print(f'The following files will be renamed')
    pprint.pprint(files_to_be_renamed)

    if not input("Do you want to proceed? (y/n): ").lower().strip()[:1] == "y": sys.exit(1)

    for elt in files_to_be_renamed:
        os.rename(f'{directory_path}/{elt[0]}', f'{directory_path}/{elt[1]}')
    print('Renaming over!')


@click.command()
@click.argument('directory_path', default="directory")
def rename_ableton_freeze_samples(directory_path):
    """Rename Ableton freezed samples so it keeps only the original track name."""

    files = os.listdir(directory_path)

    files_to_be_renamed = []
    for elt in files:
        try:
            file, extension = os.path.splitext(elt)
            if extension == '.wav':
                try:
                    file = file.split('Freeze')[1].split('[')[0].strip()
                    new_filename = f'{file}{extension}'
                    files_to_be_renamed.append((elt, new_filename))

                except IndexError:  # not a correct Ableton frozen filename
                    pass

        except ValueError:  # not a correct filename
            pass

    print(f'The following files will be renamed')
    pprint.pprint(files_to_be_renamed)

    if not input("Do you want to proceed? (y/n): ").lower().strip()[:1] == "y": sys.exit(1)
    for elt in files_to_be_renamed:
        os.rename(f'{directory_path}/{elt[0]}', f'{directory_path}/{elt[1]}')
    print('Renaming over!')


if __name__ == "__main__":
    print("This should not be called as a module but rather as a command line.")
