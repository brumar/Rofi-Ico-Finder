#!/bin/sh
BASEDIR=$(dirname $0)
cat $BASEDIR/fa_icolist.txt | rofi -dmenu -i -p "icon:" | cut -d ' ' -f 2 | xclip -selection clipboard
