from pygame import*


okno = display.set_mode((1000,700))

game = True
clock = time.Clock()

class karta(sprite.Sprite):
    def __init__(self,pik, x,y):
        super().__init__()
        self.image = transform.scale(image.load(pik), (80,120))
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 
    def ris(self): # сокращение команды для отображения на экране
        okno.blit(self.image, (self.rect.x, self.rect.y))

from random import*
colors = ['red', 'green', 'yellow']
numes = ['0','1','2','3','4','5','6','7','8','-=','=-','+2','+4',]
naokno = []

fon = transform.scale(image.load('derevo.jpg'), (1000,700))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                wen = choice(colors)+choice(numes)+'.png'
                print(wen)
                nk = karta(wen, 10,500)
                naokno.append(nk)
            if e.key == K_LSHIFT:
                   wen = choice(colors)+choice(numes)+'.png'
                   print(wen)
                   nk = karta(wen, 10,300)
                   naokno.append(nk)
        if e.type==MOUSEBUTTONDOWN:
            if e.button==1:
                for k1 in naokno:
                    if k1.rect.collidepoint(e.pos):
                        k1.rect.y = 300
    okno.fill((0,250,255))
    okno.blit(fon,(0,0))
    for k in range(len(naokno)):
        naokno[k].ris()
        naokno[k].rect.x = k*90 +10
    display.update() 
    clock.tick(40)  
