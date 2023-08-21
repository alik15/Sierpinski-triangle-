
import pygame
import random
import lib


pygame.init()
screen = pygame.display.set_mode([500, 500])



current_position=[0,0]
x=0


A = [0,80]

B = [80,400]
C = [420,400]


objects=[A,B,C]

running = True

while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    
    screen.fill((255, 255, 255))

    
    for item in objects:
    
            pygame.draw.circle(screen, (0,0,255),item,1)
           

            chosen_corner=random.choice([A,B,C])
   
            current_position = lib.mid_point(current_position,chosen_corner)
   
            objects.append(current_position)
    
    
            pygame.display.flip()
        
      


# Done! Time to quit.

pygame.quit()











