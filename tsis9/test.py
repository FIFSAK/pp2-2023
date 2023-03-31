import pygame

pygame.init()
sc = pygame.display.set_mode((600, 400))
check = True
check_draw = False
color = "white"
start_pos = None
rect_start = False
start_pos_rec, end_pos_rec = None, None
width_line = 2
eraser = pygame.image.load(
    r"C:\Users\Admin\Desktop\pp2-22B030386\tsis9\images\pngimg.com - eraser_PNG15.png")
eraser = pygame.transform.scale(eraser, (100, 80))
color = 'white'
while check:
    sc.blit(eraser, (390, 310))
    pygame.draw.circle(sc, 'red', (50, 350), 40)
    pygame.draw.circle(sc, 'blue', (150, 350), 40)
    pygame.draw.circle(sc, 'green', (250, 350), 40)
    pygame.draw.circle(sc, 'white', (350, 350), 40)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos_rec = event.pos
            rect_start = True
        if event.type == pygame.MOUSEMOTION:
            if rect_start:
                end_pos_rec = event.pos
                width_rect = end_pos_rec[0] - start_pos_rec[0]
                height_rect = end_pos_rec[1] - start_pos_rec[1]
                sc.fill('black')
                pygame.draw.rect(sc, color, (start_pos_rec[0], start_pos_rec[1], width_rect, height_rect))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            rect_start = False
    pygame.display.update()

pygame.quit()