import pgzrun

HEIGHT=800
WIDTH=600
TITLE="Gallaga Game"

score=0

spaceprotector=Actor("spaceprotector")

spaceprotector.x=(WIDTH/2)
spaceprotector.y=780

def draw():
    screen.fill("black")
    spaceprotector.draw()
def update():
    if keyboard.a:
        spaceprotector.x=spaceprotector.x-3
    if keyboard.d:
        spaceprotector.x=spaceprotector.x+3

pgzrun.go()