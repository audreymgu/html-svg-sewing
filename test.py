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

text = "Hello <world>, <p>Paolo de paolo <p>chimmichurri</p></p> is here to <h1><a>welcome</a></h1> you."

open_tag = re.compile(r'(?<=<)\w+')
close_tag = re.compile(r'(?<=\/)\w+')
closing_caret = re.compile(r'[^<]*>')

class State(Enum):
    CUR_ADV = auto()
    TAG_BRANCH = auto()
    OPEN_TAG = auto()
    OPEN_TAG_ADV = auto()
    CLOSE_TAG = auto()
    READ_BODY = auto()

state = State.CUR_ADV
start = 0
index = 0
current_tag = ""
stack = []

while index < len(text):
    if state == State.CUR_ADV:
        if text[index] == "<":
            state = State.TAG_BRANCH
        else:
            index += 1
    if state == State.TAG_BRANCH:
        index += 1
        if text[index] == "/":
            state = State.CLOSE_TAG
        else:
            state = State.OPEN_TAG
    if state == State.OPEN_TAG:
        if tag := open_tag.search(text, pos=index):
            if tag.group() in tag_list:
                current_tag = tag.group()
                print('opening tag found: ' + current_tag)
                index = tag.end()
                state = State.OPEN_TAG_ADV
            else:
                index = tag.end()
                state = State.CUR_ADV
    if state == State.OPEN_TAG_ADV:
        if close := closing_caret.search(text, pos=index):
            index = close.end()
            stack.append((current_tag, index))
            state = State.CUR_ADV
        else:
            print("E: closing caret for opening tag not found.")
            sys.exit(1)
    if state == State.CLOSE_TAG:
        if tag := close_tag.search(text, pos=index):
            current_tag = tag.group()
            if current_tag == stack[-1][0]:
                print(text[stack[-1][1]:(tag.start() - 2)])
                stack.pop()
        index = closing_caret.search(text, pos=index).end()
        state = State.CUR_ADV

        
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
