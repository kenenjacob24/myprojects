import pygame 
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")
text = pygame.font.Font(None, 36).render("Hello!", True, "black")

screen.fill("white")
pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
screen.blit(text, (280,120))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.wait(10)
pygame.quit()
