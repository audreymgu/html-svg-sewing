import drawsvg as draw

d = draw.Drawing(400, 100, origin='top-left')


d.append(draw.Text(
    text='Hello World', 
    font_size=40, 
    x=20, 
    y=65, 
    font_family='Arial, Helvetica, sans-serif', 
    font_weight='bold',
    fill='#2c3e50'
))

d.save_svg('hello_world.svg')

print("Successfully generated 'hello_world.svg'!")
