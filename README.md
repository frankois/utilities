# Utilities

Some personal utility scripts

- `files.py`: perform tasks accross files such are renaming, moving, copying...

To use it, you have to download the repository, then install the packages in your `virtualenv`.
To do so, you can go in the directory and run `pip install .`

## Commandes

**`rename_extensions`**

Rename all the extensions of files contained in a folder located at `<directory_path>`.
You can specify `-R` if you want to rename recursively the files, and so apply it to subfolders.

*Examples*
- `rename_extensions <directory_pach> <old_extension> <new_extension>`
- `rename_extensions -R /Users/test_directory 'WAV' 'wav`

### Sources

- https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
- https://dbader.org/blog/python-commandline-tools-with-click
- https://click.palletsprojects.com/en/7.x/setuptools/