#!/bin/sh
cat fa_icolist.txt | rofi -dmenu -i -p "icon:" | cut -d ' ' -f 2 | xclip -selection clipboard
