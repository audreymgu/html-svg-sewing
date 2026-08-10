import drawsvg as draw

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
print(content)

d = draw.Drawing(400, 100, origin='top-left')


d.append(draw.Text(
    text=content, 
    font_size=40, 
    x=20, 
    y=65, 
    font_family='Arial, Helvetica, sans-serif', 
    font_weight='bold',
    fill='#2c3e50'
))

d.save_svg('hello_world.svg')

print("Successfully generated 'hello_world.svg'!")
