# Rofi Ico Finder 
This reduces the time consuming aspect of searching for an icon as a unicode character.

## Usage
`./rofi_fa_ico_finder.sh`, then type your keywords, then "enter" then the symbol should be in your clipboard.
![screenshot](./screenshot.png?raw=true)

## Requirements

font-awesome installed on your machine (I am not sure about that...)

rofi
xclip (default, could be changed through environment variable).

## Environment variables

Use the following variables to modify the directory (in case of linking the
executable to other folder, ie. /usr/local/bin). Also to change the default
command for copying.

```bash
# Set to the directory where the repository is forked.
export ROFI_FA_ICON_DIR="foo/bar"
# Set to the binary for copying
export ROFI_FA_ICON_BIN='wl-copy'
```

## Internals

It works on a list generated with the python script in this repo taking the [awesome yaml](https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/src/icons.yml) of the font-awesome github repository into input. As a consequence, at the moment, only the characters supported by font-awesome is supported by this script. If you made a better list, pull it there :).

## License
MIT
