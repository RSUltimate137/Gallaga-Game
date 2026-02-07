import pgzrun

HEIGHT=800
WIDTH=600
TITLE="Gallaga Game"

score=0

game=True

spaceprotector=Actor("spaceprotector")

spacebugs=[]

spacebullets=[]

for i in range(5):
    for j in range(5):
        spacebug=Actor("spacebug")
        spacebug.x=100+i*100
        spacebug.y=100+j*50
        spacebugs.append(spacebug)

spaceprotector.x=(WIDTH/2)
spaceprotector.y=725

def draw():
    global game
    screen.fill("black")
    spaceprotector.draw()
    for bug in spacebugs:
        bug.draw()
    for bullet in spacebullets:
        bullet.draw()
    if game == "Lost":
        screen.fill("black")
        screen.draw.text("You Got Eaten!",(70,70),fontsize=72)
    if game == "Won":
        screen.fill("black")
        screen.draw.text("You Defeated The Bugs!",(20,70),fontsize=72)

def update():
    global game

    if game != True:
        return
    
    if len(spacebugs) == 0:
        game = "Won"
        True

    if game == "Lost":
        return

    if keyboard.a and spaceprotector.x > 37:
        spaceprotector.x -= 3
    if keyboard.d and spaceprotector.x < 560:
        spaceprotector.x += 3

    for bullet in spacebullets[:]:
        bullet.y -= 5
        if bullet.y < 0:
            spacebullets.remove(bullet)

    for bug in spacebugs[:]:
        bug.y += 0.8

        if bug.colliderect(spaceprotector):
            game = "Lost"

        for bullet in spacebullets[:]:
            if bullet.colliderect(bug):
                spacebullets.remove(bullet)
                spacebugs.remove(bug)
                break


def on_key_down(key):
    global spacebullets,game
    if key == keys.SPACE:
        spacebullet=Actor("spacebullet")
        spacebullet.x=spaceprotector.x
        spacebullet.y=spaceprotector.y
        spacebullets.append(spacebullet)

pgzrun.go()