import pygame

pygame.init()
sc = pygame.display.set_mode((700, 525))
bg = pygame.image.load(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\images\mickeyclock.jpg")
right_hand = pygame.image.load(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\images\right_hand.png")
left_hand = pygame.image.load(r"C:\Users\Admin\Desktop\pp2-22B030386\tsis7\images\left_hand.png")
bg = pygame.transform.scale(bg, (700, 525))
cent_bg = bg.get_rect(center=(350, 525 // 2))
sc.blit(bg, cent_bg)
sc.blit(right_hand, (100,100))
sc.blit(left_hand, (600,0))
check = True
while check:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
    pygame.display.update()
