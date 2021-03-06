# Utilities

Some personal utility scripts

- `files.py`: perform tasks accross files such are renaming, moving, copying...

To use it, you have to download the repository, then install the packages in your `virtualenv`.
To do so, you can go in the directory and run `pip install .`

## Commands

### Files (`files.py`)

**`rename_extensions`**

Rename all the extensions of files contained in a folder located at `<directory_path>`.  
You can specify `-R` if you want to rename recursively the files, and so apply it to subfolders.

*Examples*
- `rename_extensions <directory_path> <old_extension> <new_extension>`
- `rename_extensions -R /Users/test_directory WAV wav`

**`rename_ableton_freeze`**

Rename all the frozen wav files generated by Ableton of the specified `<directory_path>`. This came from the idea to speed up drum rack export process, which is done by freezing individual tracks. *(article describing the process to link here)*

*Examples*

- `rename_ableton_freeze <directory_path>`


### Sources

- https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
- https://dbader.org/blog/python-commandline-tools-with-click
- https://click.palletsprojects.com/en/7.x/setuptools/