import sys
import re
import drawsvg as draw
from svg_text2path import Text2PathConverter

# pass name of file to script
# specify drawing area
# read in the file
# walk character by character over the output
# when an opening brace is hit, 
# grab substring from opening brace to first space
# ignore any additional parameters attached (e.g. class, href, etc.)
# pass substring to tag checker function to resolve tag
# should tag checker be the one to grab the contents, or just pass back formatting information?
# perhaps this should be a recursive function call?
# take all text starting from > to </ (this will require additional validation even in the case where we are only evaluating tags at a single level of depth)

document = open("test.html", "r")
content = document.read()
doctype = "<!DOCTYPE html>"

if doctype not in content:
    print("E: DOCTYPE not declared.")
    sys.exit(1)

tag_list = [("<h1>","</h1>"), ("<p>", "</p>"), ("<a>", "</a>")]

text = "Hello <world>,<h1> welcome to <p><Python>."

index = 0

while index < len(text):
    if text[index] == "<":
        tag = re.split(r'(?<=[>])\s*', text[index:])[0]
        if any(tag in tuple for tuple in tag_list):
            print('tag found:' + tag)
        index += len(tag)
    else:
        index += 1
        
d = draw.Drawing(400, 100, origin='top-left')


d.append(draw.Text(
    text=content, 
    font_size=40, 
    x=20, 
    y=65, 
    font_family='sans-serif', 
    font_weight='bold',
    fill='#2c3e50'
))

converter = Text2PathConverter()
raw_svg = d.as_svg()
flat_svg = converter.convert_string(raw_svg)

with open("output.svg", "w", encoding="utf-8") as f:
    f.write(flat_svg)

print("Successfully generated 'output.svg!")
