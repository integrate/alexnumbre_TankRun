import wrap,time,random
from wrap import world,sprite,sprite_text
a=1366
b=738
world.create_world(a,b)
world.set_back_color(70,70,70)
player=sprite.add("battle_city_tanks",a/2,b/2,"tank_enemy_size2_purple2")
y1 = random.randint(20, b-20)
bull1=sprite.add("battle_city_items",0, y1,"bullet")
sprite.set_size(bull1,30,30)
y2 = random.randint(20, b-20)
bull2=sprite.add("battle_city_items", a, y2,"bullet")
sprite.set_angle(bull2,270)
sprite.set_angle(bull1,90)
sprite.set_size(bull2,30,30)
health =5
armor=0

healthscore = sprite.add_text("health: "  +str(health), 50, 50)
armorscore = sprite.add_text("armor: "+str(armor), 50, 70)

x1 = random.randint(20, a-20)
y1 = random.randint(20, b-20)
x2 = random.randint(20, a-20)
y2 = random.randint(20, b-20)
healthup=sprite.add("battle_city_items",x1,y1,"block_gift_tank")
armorup=sprite.add("battle_city_items",x2,y2,"block_gift_star")

def updatestat():
    sprite_text.set_text(healthscore,"health: "+str(health))
    sprite_text.set_text(armorscore,"armor: "+str(armor))

def updatesize(num):
   global size
   sprite.set_height_proportionally(player,sprite.get_height(player)+num)

@wrap.always(5001)
def healthupp():
    x1=random.randint(20,a-20)
    y1=random.randint(20,b-20)
    sprite.move_to(healthup,x1,y1)

def collidehealthup():
    global health
    if sprite.is_collide_sprite(player,healthup):
        sprite.move(healthup,2000,1200)
        health+=1
        updatestat()



@wrap.always(5002)
def armorupp():
    x2=random.randint(20,a-20)
    y2=random.randint(20,b-20)
    sprite.move_to(armorup,x2,y2)



def collidearmor():
    global armor
    if sprite.is_collide_sprite(player,armorup):
        sprite.move(armorup, 2000, 1200)
        armor+=1
        updatesize(10)
        updatestat()


@wrap.on_key_always(wrap.K_LEFT,50)
def move_left():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,270)
    sprite.move_at_angle_dir(player,10)
    if x <=20:
        sprite.move_to(player,20,y)
    collidearmor()
    collidehealthup()

@wrap.on_key_always(wrap.K_RIGHT,50)
def move_right():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,90)
    sprite.move_at_angle_dir(player,10)
    if x >=a-20:
        sprite.move_to(player,a-20,y)
    collidearmor()
    collidehealthup()

@wrap.on_key_always(wrap.K_UP,50)
def move_up():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,0)
    sprite.move_at_angle_dir(player,10)
    if y <=20:
        sprite.move_to(player,x,20)
    collidearmor()
    collidehealthup()

@wrap.on_key_always(wrap.K_DOWN,50)
def move_down():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,180)
    sprite.move_at_angle_dir(player,10)
    if y >=b-20:
        sprite.move_to(player,x,b-20)
    collidearmor()
    collidehealthup()


def podgotovka_pyli(bull,x):
    y = random.randint(20, b-20)
    sprite.show(bull)
    sprite.move_to(bull, x, y)

@wrap.always(10000)
def bullet():
    podgotovka_pyli(bull1,0)
    podgotovka_pyli(bull2,a)


def howmovebullet(bull):
    global bull1,health,armor,size,size2
    if not sprite.is_visible(bull):
        return

    x = sprite.get_x(bull)
    sprite.move_at_angle_dir(bull, 10)
    if x >= a+50 or x<-50:
        sprite.hide(bull)
        return


    if not sprite.is_collide_sprite(bull, player):
        return

    sprite.hide(bull)
    armor -= 1
    updatesize(-10)
    if armor == -1:
        armor = 0
        health -=1
        updatesize(10)
    updatestat()



@wrap.always(40)
def movebullet():
    howmovebullet(bull1)
    howmovebullet(bull2)


