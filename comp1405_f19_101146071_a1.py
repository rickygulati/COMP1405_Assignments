# Name: RICKY GULATI
#Student Number: 101146071



import pygame


pygame.display.init()


house=pygame.display.set_mode((500,500))


# sky
house.fill((78,226,236))                    #Sky: color- blue diamond (78,226,236)


# grass
pygame.draw.rect(house,(82,203,28),(0,180,500,320))  #Grass: color- yellow green (82, 208, 23); shape- rectangle          


# sun
pygame.draw.circle(house,(255,255,0),(38,35),24)   #Sun: color- yellow (255, 255, 0); shape- circle


# House main
pygame.draw.rect(house,(255,0,0),(290,124,132,111))   #House: color- red (255, 0, 0);shape- rectangle


# house windows
pygame.draw.rect(house,(21,27,84),(304,135,33,27))   #Window: color- midnight blue (21, 27, 84); shape- rectangle
pygame.draw.rect(house,(21,27,84),(372,135,33,27))   #Window: color- midnight blue (21, 27, 84); shape- rectangle


# door
pygame.draw.rect(house,(255,166,47),(342,196,28,41))  #Door: color- cantaloupe (255, 166, 47); shape- rectangle


# doorknob
pygame.draw.circle(house,(0,0,0),(363,219),5)  #Doorknob: color- black (0, 0, 0); shape- circle


# tree trunks
pygame.draw.rect(house,(127,70,44),(97,157,15,80))   #Tree trunks: color- sepia (127, 70, 44); shape- rectangle
pygame.draw.rect(house,(127,70,44),(146,157,15,80))  #Tree trunks: color- sepia (127, 70, 44); shape- rectangle


# tree leaves
pygame.draw.ellipse(house,(0,255,0),(88,90,33,92))  #Tree leaves: color- green (0, 255, 0); shape- ellipse                 
pygame.draw.ellipse(house,(0,255,0),(137,90,33,92)) #Tree leaves: color- green (0, 255, 0); shape- ellipse


# house top
pygame.draw.polygon(house,(229,255,180),((293,90),(424,90),(452,124),(262,124))) #House top: color- peach (255, 229, 180); shape- polygon


# door top
pygame.draw.polygon(house,(175,155,96),((338,189),(376,189),(381,195),(333,195))) #Door top: color- bullet shell (175, 155, 96); shape- polygon


# Pavement
pygame.draw.polygon(house,(173, 169, 110),((340,236),(367,236),(312,330),(239,330)))  #Pavement: color- khaki (173, 169, 110); shape- polygon


# Fences
pygame.draw.rect(house,(150, 111, 51),(0,265,234,65))  #Fences: color- wood (150, 111, 51); shape- rectangle
pygame.draw.rect(house,(150, 111, 51),(316,265,234,65))  #Fences: color- wood (150, 111, 51); shape- rectangle


# update
pygame.display.update()


# Time delay for 3 seconds
pygame.time.delay(3000)


# Saving Image
pygame.image.save(house,"house_101146071.bmp")


# Quit 
pygame.display.quit()
