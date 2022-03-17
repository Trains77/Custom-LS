# Custom-LS

A custom python wrapper I have made for the ls command

If script is in another directory, it will list the contents of the current working directory

So if it were in ~/Downloads and was run while in ~/Pictures, it will display the contents of the Pictures folder

## Usage:

Arguments are the same as ls

### Running:
`python main.py`

## Features:

Refuses to read folders with the file .hide in them, displaying a permission denied error

# Known bugs

Files with spaces in names do not work
