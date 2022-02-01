import wrap,time,random
from wrap import world,sprite,sprite_text

world.create_world(1920,1080)
world.set_back_color(70,70,70)
player=sprite.add("battle_city_tanks",960,540,"tank_enemy_size2_purple2")
y1 = random.randint(20, 1060)
bull1=sprite.add("battle_city_items",0, y1,"bullet")
sprite.set_size(bull1,30,30)
y2 = random.randint(20, 1060)
bull2=sprite.add("battle_city_items", 1920, y2,"bullet")
sprite.set_size(bull2,30,30)
health =5
armor=0

healthscore = sprite.add_text(str(health), 50, 50)
armorscore = sprite.add_text(str(armor), 50, 70)
sprite_text.set_text(healthscore,"health: " + str(health))
sprite_text.set_text(armorscore,"armor: "+str(armor))
x1 = random.randint(20, 1900)
y1 = random.randint(20, 1060)
x2 = random.randint(20, 1900)
y2 = random.randint(20, 1060)
healthup=sprite.add("battle_city_items",x1,y1,"block_gift_tank")
armorup=sprite.add("battle_city_items",x2,y2,"block_gift_star")


@wrap.always(5001)
def healthupp():
    global  health
    x1=random.randint(20,1900)
    y1=random.randint(20,1060)
    sprite.move_to(healthup,x1,y1)

@wrap.always(100)
def collidehealthup():
    global health
    if sprite.is_collide_sprite(player,healthup):
        sprite.move(healthup,2000,1200)
        health+=1
        sprite_text.set_text(healthscore, "health: " + str(health))
        sprite_text.set_text(armorscore, "armor: " + str(armor))



@wrap.always(5002)
def armorupp():
    x2=random.randint(20,1900)
    y2=random.randint(20,1060)
    sprite.move_to(armorup,x2,y2)


@wrap.always(100)
def collidearmor():
    global armor
    if sprite.is_collide_sprite(player,armorup):
        sprite.move(armorup, 2000, 1200)
        armor+=1
        size=sprite.get_height_percent(player)
        sprite.set_height_percent(player,size+10)
        size+=10
        size2 = sprite.get_width_percent(player)
        sprite.set_height_percent(player, size2 + 10)
        size2 += 10
        sprite_text.set_text(healthscore, "health: " + str(health))
        sprite_text.set_text(armorscore, "armor: " + str(armor))


@wrap.on_key_always(wrap.K_LEFT,50)
def move_left():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,270)
    sprite.move_at_angle_dir(player,10)
    if x <=20:
        sprite.move_to(player,20,y)

@wrap.on_key_always(wrap.K_RIGHT,50)
def move_right():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,90)
    sprite.move_at_angle_dir(player,10)
    if x >=1900:
        sprite.move_to(player,1900,y)

@wrap.on_key_always(wrap.K_UP,50)
def move_up():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,0)
    sprite.move_at_angle_dir(player,10)
    if y <=20:
        sprite.move_to(player,x,20)

@wrap.on_key_always(wrap.K_DOWN,50)
def move_up():
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    sprite.set_angle(player,180)
    sprite.move_at_angle_dir(player,10)
    if y >=1060:
        sprite.move_to(player,x,1060)


@wrap.always(10000)
def bullet1():
    global bull1
    sprite.set_size(bull1,30,30)
    sprite.set_angle(bull1,90)
    y=random.randint(20,1060)
    sprite.show(bull1)
    sprite.move_to(bull1,0,y)


@wrap.always(40)
def movebullet1():
    global bull1,health,armor,size,size2
    sprite.set_angle(bull1, 90)
    if not sprite.is_visible(bull1):
        return

    x = sprite.get_x(bull1)
    sprite.move_at_angle_dir(bull1, 10)
    if x >= 1920:
        sprite.hide(bull1)
        return


    if  sprite.is_collide_sprite(bull1, player):
        sprite.hide(bull1)
        sprite.set_costume_next(player)
        armor -= 1
        size = sprite.get_height_percent(player)
        sprite.set_height_percent(player, size - 10)
        size -= 10
        size2 = sprite.get_width_percent(player)
        sprite.set_height_percent(player, size2 - 10)
        size2 -= 10
        if armor == -1:
            size = sprite.get_height_percent(player)
            sprite.set_height_percent(player, size + 10)
            size += 10
            size2 = sprite.get_width_percent(player)
            sprite.set_height_percent(player, size2 + 10)
            size2 += 10
            armor = 0
            health -=1
            sprite.show(player)
    sprite_text.set_text(healthscore, "health: " + str(health))
    sprite_text.set_text(armorscore, "armor: " + str(armor))



@wrap.always(10000)
def bullet2():
    global bull2
    sprite.set_size(bull2,30,30)
    sprite.set_angle(bull2,270)
    y=random.randint(20,1060)
    sprite.move_to(bull2,1920,y)
    sprite.show(bull2)


@wrap.always(40)
def movebullet2():
    global bull2,health,armor,size,size2
    sprite.set_angle(bull2, 270)
    if not sprite.is_visible(bull2):
        return

    x = sprite.get_x(bull2)
    sprite.move_at_angle_dir(bull2, 10)
    if x <= 0:
        sprite.hide(bull2)
        return


    if  sprite.is_collide_sprite(bull2, player):
        sprite.hide(bull2)
        sprite.set_costume_next(player)
        armor -= 1
        size = sprite.get_height_percent(player)
        sprite.set_height_percent(player, size - 10)
        size -= 10
        size2 = sprite.get_width_percent(player)
        sprite.set_height_percent(player, size2 - 10)
        size2 -= 10
        if armor == -1:
            size = sprite.get_height_percent(player)
            sprite.set_height_percent(player, size + 10)
            size += 10
            size2 = sprite.get_width_percent(player)
            sprite.set_height_percent(player, size2 + 10)
            size2 += 10
            armor = 0
            health -=1
            sprite.show(player)
    sprite_text.set_text(healthscore, "health: " + str(health))
    sprite_text.set_text(armorscore, "armor: " + str(armor))




@wrap.always(100)
def debug():

    print(sprite.get_pos(bull1))
