from sfml import sf
from Graphics import Board

window = sf.RenderWindow(sf.VideoMode(600, 600), "Tic Tac Toe")

# png
textureX = sf.Texture.from_file("./x.png")
textureO = sf.Texture.from_file("./o.png")
textureS = sf.Texture.from_file("./skull.png")

while window.is_open:
    window.clear(sf.Color.WHITE)

    for event in window.events:
        pass

    # exit
    if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
        window.colse()

    # body game
    rectangle_one = sf.RectangleShape()
    rectangle_one.size = (600, 0)
    rectangle_one.outline_color = sf.Color.BLACK
    rectangle_one.outline_thickness = 2
    rectangle_one.position = (0, 200)

    rectangle_two = sf.RectangleShape()
    rectangle_two.size = (600, 0)
    rectangle_two.outline_color = sf.Color.BLACK
    rectangle_two.outline_thickness = 2
    rectangle_two.position = (0, 400)

    rectangle_three = sf.RectangleShape()
    rectangle_three.size = (0, 600)
    rectangle_three.outline_color = sf.Color.BLACK
    rectangle_three.outline_thickness = 2
    rectangle_three.position = (200, 0)

    rectangle_four = sf.RectangleShape()
    rectangle_four.size = (0, 600)
    rectangle_four.outline_color = sf.Color.BLACK
    rectangle_four.outline_thickness = 2
    rectangle_four.position = (400, 0)

    window.draw(rectangle_one)
    window.draw(rectangle_two)
    window.draw(rectangle_three)
    window.draw(rectangle_four)
    window.display()

