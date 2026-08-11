import sys
import re
import drawsvg as draw
from svg_text2path import Text2PathConverter
from enum import Enum, auto

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

tag_list = ["h1", "p", "a"]

text = "Hello <world>, <p>Paolo</p> is here to <h1>welcome</h1> you."
        
def map_dom(text, tag_name="none", index=0):
    buffer = ""

    open_tag = re.compile(r'(?<=<)\w+')
    closing_caret = re.compile(r'[^<]*>')

    print(index, text[index:])

    while index < len(text):
        # if we find an opening caret,
        if text[index] == "<":
            print(tag_name)
            # if it's an opening tag,
            if tag := open_tag.search(text, pos=index):
                name = tag.group()
                # and if the tag is recognized,
                if name in tag_list:
                    print('opening tag found: ' + name)
                    # move the cursor up to the end of the name.
                    index = tag.end()
                    # if we find a closing caret not interrupted by another tag,
                    if close := closing_caret.search(text, pos=index):
                        # move the cursor upand set the starting point of our buffer to this point.
                        start = index = close.end()
                        # call the function recursively, passing the current index and tag name.
                        index = map_dom(text, name, index)
                    else:
                        # otherwise, throw an error.
                        print("E: closing caret for opening " + name + " tag not found.")
                        sys.exit(1)
                else:
                    index += len(name)
            # if it's a closing tag that matches the name we've been given,
            if (end := text.find("</" + tag_name + ">", index)) != -1:
                print("tag content: " + text[start:end])
                # move our index past the closing tag.
                return end + len(end)
        # otherwise advance cursor by one.
        else:
            index += 1

map_dom(text)

# map_dom
# look for first opening tag
    # call function again with tag we're looking for and updated index
# if we find closing tag
    # 

        
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
