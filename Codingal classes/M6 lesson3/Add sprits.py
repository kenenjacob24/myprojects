import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving Sprites")

blue = pygame.Rect(100, 200, 50, 50)
red = pygame.Rect(400, 200, 50, 50)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    blue.x += 4 * (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    blue.y += 4 * (keys[pygame.K_DOWN] - keys[pygame.K_UP])

    red.x += 4 * (keys[pygame.K_d] - keys[pygame.K_a])
    red.y += 4 * (keys[pygame.K_s] - keys[pygame.K_w])

    blue.clamp_ip(screen.get_rect())
    red.clamp_ip(screen.get_rect())

    screen.fill("white")
    pygame.draw.rect(screen, "blue", blue)
    pygame.draw.rect(screen, "red", red)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()