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

    window.display()

