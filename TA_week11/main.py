import pygame

pygame.init()
width, height = 680, 400
pygame.display.set_caption("LASERS")
window = pygame.display.set_mode((width, height))
middle = (width /2, height / 2)
velocity = 0.5
x = width / 2
y = height / 2
def draw_window():
    pygame.draw.circle(window, ((0, 0, 255)), (x, y), 4)
    pygame.draw.rect(window, ((0, 255, 0)), (200, 150, 100, 50), 30)
    pygame.draw.line(window, ((255, 0, 0)), (x, y),(height, width), 3)
    pygame.draw.line(window, ((0, 0, 255)), middle, (width, height), 3)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.fill((255, 255, 255))
    draw_window()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity
    pygame.display.update()
