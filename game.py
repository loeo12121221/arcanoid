import pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
col = (232, 246, 250)
window.fill(col)
class Area():
    def __init__(self, col, width, length, x, y):
        self.col = col
        self.rect = pygame.Rect(x, y, width, length)
    def color_new(self, col):
        self.col = col
    def fillrect(self):
        pygame.draw.rect(window, self.col, self.rect)
    def outline(self, colr, width):
        pygame.draw.rect(window, colr, self.rect, width)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Picture(Area):
    def __init__(self, col, width, length, x, y, files):
        super().__init__(col, width, length, x, y)
        self.image = pygame.image.load(files)
    def drawp(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Label(Area):
    def set_text(self, text, big=25, color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', big).render(text, True, color)
    def draw(self, shiftx, shifty):
        self.fillrect()
        window.blit(self.image, (self.rect.x+shiftx, self.rect.y+shifty))
    def colidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    
platform = Picture(col, 100, 30, 150, 500, 'platform.png')
platform.drawp()
ball = Picture(col,50,50, 152, 406, 'ball.png')
ball.drawp()
monsters = list()
startx = 5
starty = 10
monsterscount = 9
move_right = False
move_left = False
game_over = False
ball_speedx = 3
ball_speedy = 3
for i in range(3):

    x = startx + (27.5 * i)
    y = starty + (55 * i)
    for k in range(monsterscount):
        en3 = Picture(col, 50, 50, x, y, 'enemy.png')
        monsters.append(en3)
        x += 55
        en3.drawp()
    monsterscount -= 1
while game_over == False:

    ball.fillrect()
    platform.fillrect()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
    if move_right == True:
        platform.rect.x += 3
    if move_left == True:
        platform.rect.x -= 3
    ball.rect.x += ball_speedx
    ball.rect.y += ball_speedy
    if ball.colliderect(platform.rect):
        ball_speedy *= (-1)
    if ball.rect.y < 0:
        ball_speedy *= (-1)
    if ball.rect.x < 0 or ball.rect.x > 450:
        ball_speedx *= (-1)
    if ball.rect.y > (platform.rect.y + 20):
        text_time = Label(col, 50, 50, 150, 170)
        text_time.set_text('Ты проиграл!!', 50, (255, 0, 0))
        text_time.draw(10, 10)
        game_over = True

    for en3 in monsters:
        en3.drawp()
        if en3.colliderect(ball.rect):
            monsters.remove(en3)
            en3.fillrect()
            ball_speedy *= (-1)
    
    if len(monsters) == 0:
        text_end = Label(col, 50, 50, 150, 250)
        text_end.set_text('Ты выиграл!!', 50, (0, 250, 0))
        text_end.draw(10, 10)
        game_over = True
    ball.drawp()
    platform.drawp()

    pygame.display.update()
    clock.tick(40)
pygame.display.update()
