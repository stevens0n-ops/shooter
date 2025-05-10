#Создай собственный Шутер!

from pygame import *
from random import *
class GameSprite(sprite.Sprite):
    def __init__(self, play_image, play_x, play_y, height, width, play_speed):
        super().__init__()
        self.image = transform.scale(image.load(play_image), (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = play_x
        self.rect.y = play_y
        self.play_speed = play_speed
    def res(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.play_speed
        if key_pressed[K_d] and self.rect.x < window.get_width()-100:
            self.rect.x += self.play_speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 20,15, -5)
        bullets.add(bullet)
        

lost = 0          
class Enemy(GameSprite):
    def update(self):
        direction = 'left'
        self.rect.y += self.play_speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,500-60)
            lost = lost+1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.play_speed
        if self.rect.y < 0:
            self.kill()
    




window = display.set_mode((700, 500))
wind = transform.scale(image.load('galaxy.jpg'),(700, 500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()
sounds = mixer.Sound('fire.ogg ')
font.init()
win = font.SysFont('Times New Roman', 50).render('YOU WIN!', True, (255, 0, 0))
win1 = font.SysFont('Times New Roman', 50).render('YOU LOST!', True, (255, 0, 0))


game = True
finish = False
clock = time.Clock()
hero = Player('rocket.png', 50, 350,80, 60, 3)
bullets = sprite.Group()

monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(0,500-60), -40,40,60, randint(1,2))
    monsters.add(enemy)


    
counter = 0   

while game == True:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                hero.fire()
              
    if not finish:
        window.blit(wind, (0,0))
       
        hero.res()
        monsters.update()
        monsters.draw(window)
       
        hero.update()
        bullets.draw(window)
        bullets.update()
        sprie = sprite.groupcollide(monsters, bullets, True, True)
        for i in sprie:
            counter += 1
            enemy = Enemy('ufo.png', randint(0,500-60), -40,40,60, randint(1,3))
            monsters.add(enemy)
        win2 = font.SysFont('Times New Roman', 30).render('Пропущено:'+ str(lost), True, (255, 0, 0))
        window.blit(win2, (20,30))
        win3 = font.SysFont('Times New Roman', 30).render('Убито:'+ str(counter), True, (255, 0, 0))
        window.blit(win3, (490,30))
        if lost >= 5:
            window.blit(win1, (230,210))
            finish = True
        if counter >= 10:
            window.blit(win, (230,210))
            finish = True
        
    display.update()
    clock.tick(80)

