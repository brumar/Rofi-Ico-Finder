# python 3.5
import yaml
import os.path as path
if __name__ == "__main__":
    mypath = "/home/bruno/awesome-icons-generators/"  # change this line
    yaml_filepath = path.join(mypath, "fa_icons.yml")  # taken from there : https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/src/icons.yml
    out_filepath = path.join(mypath, "fa_icolist.txt")
    with open(yaml_filepath, 'r') as stream:
        try:
            mydic = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    icos = mydic['icons']
    mystr = ""
    for ico in icos:
        symbol = chr(int(ico["unicode"], 16))  # need to convert HEXA code into Base 10 before calling chr
        name = ico["name"].replace(" ", "_")  # avoid that, in rofi_ico_finder.sh, the trick "cut -d ' '" fails because of names with spaces
        try:
            keywords = "("+",".join(ico["filter"])+")"
        except: #sometimes there is no filter. Easier to ask forgiveness.
            keywords = ""
        line = name+" "+symbol+"  "+keywords+"\n"
        mystr += line

    with open(out_filepath, 'w') as fout:
        fout.write(mystr)