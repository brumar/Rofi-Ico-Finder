#!/bin/sh
if [ -z "$ROFI_FA_ICON_DIR" ]; then
    BASEDIR=$(dirname $0)
else
    BASEDIR="$ROFI_FA_ICON_DIR"
fi

if [ -z "$ROFI_FA_ICON_BIN" ]; then
    BIN='xclip -selection clipboard'
else
    BIN="$ROFI_FA_ICON_BIN"
fi

cat ${BASEDIR}/fa_icolist.txt | rofi -dmenu -i -p "Icon" | cut -d ' ' -f 2 | "${ROFI_FA_ICON_BIN}"
