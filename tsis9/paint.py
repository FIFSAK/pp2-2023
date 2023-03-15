import pygame

pygame.init()
sc = pygame.display.set_mode((600, 400))
check = True
check_draw = False
color = "white"
start_pos = None
width_line = 2
eraser = pygame.image.load(
    r"C:\Users\Admin\Desktop\pp2-22B030386\tsis9\images\pngimg.com - eraser_PNG15.png")
eraser = pygame.transform.scale(eraser, (100, 80))
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
            start_pos = event.pos
            check_draw = True
        elif event.type == pygame.MOUSEMOTION:
            if check_draw:
                end_pos = event.pos
                pygame.draw.line(sc, color, start_pos, end_pos, width_line)
                start_pos = end_pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            check_draw = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 10 <= event.pos[0] <= 90 and 310 <= event.pos[1] <= 390:
                color = 'red'
                width_line = 2
            if 110 <= event.pos[0] <= 190 and 310 <= event.pos[1] <= 390:
                color = "blue"
                width_line = 2
            if 210 <= event.pos[0] <= 290 and 310 <= event.pos[1] <= 390:
                width_line = 2
                color = "green"
            if 310 <= event.pos[0] <= 390 and 310 <= event.pos[1] <= 390:
                color = "white"
                width_line = 2
            if 390 <= event.pos[0] <= 490 and 310 <= event.pos[1] <= 490:
                color = "black"
                width_line=40
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            sc.fill(0)
    pygame.display.update()

pygame.quit()
