			#	COMP 1405 A Assignment 4

#Student Number: 101146071

#Student Name: Ricky Gulati




			#	Source Code

import pygame

pygame.display.init()

#color definitions
GREEN = (0, 255, 0)


#Asking if user needs instructions
ch = input("\n\n\t\t\tWelcome to WIC Animations\n\n\nDo you need instructions on how to do a green screening operation?(yes/no) ")

if ch == "yes" or ch == "YES":
	print("\n1. Enter the filename of the image you wish to be the background image.\n2. Enter the filename of the image you wish to be the ghost image.\n3. Enter the coordinates you wish the image of the ghost to be centered at.\n4. That's it! The operation will be completed short after completing the previous three steps.\n\nThanks for using WIC Animations")


#Getting Background Image
BG_img_name = input("\nEnter the filename of the background image(with extension) ")
BG_image = pygame.image.load(BG_img_name)

#Getting Ghost Image
ghost_img_name = input("\nEnter the filename of the ghost image(with extension) ")
ghost_image = pygame.image.load(ghost_img_name)

#Getting dimensions of images
(ghost_width, ghost_height) = ghost_image.get_rect().size
(BG_width, BG_height) = BG_image.get_rect().size

#Blitting background image on a surface
background = pygame.display.set_mode((BG_width, BG_height))
background.blit(BG_image, (0,0))

#Updating pygame display
pygame.display.update()

#Getting coordinates of centre point 
while True:
	centre_left = int(input("What is the left coordinate of the point you wish to center the image at? "))
	centre_top = int(input("What is the top coordinate of the point you wish to center the image at? "))	
	if centre_left < 0 or centre_left > BG_width or centre_top < 0 or centre_top > BG_height:	
		print("\nInvalid input! Enter the coordinates again")
	else:
		break

#Pixel check and color formatting nested looping structure
for i in range(centre_left - (ghost_width//2), centre_left + (ghost_width//2)):
	for j in range(centre_top - (ghost_height//2), centre_left + (ghost_height//2)):
		if i > 0 and j > 0 and i < BG_width and j < BG_height:
			(ghost_R, ghost_G, ghost_B, _) = ghost_image.get_at((i - (centre_left - (ghost_width//2)), j - (centre_top - (ghost_height//2))))
			(BG_R, BG_G, BG_B, _) = background.get_at((i, j))
			if (ghost_R, ghost_G, ghost_B) != GREEN:
				background.set_at((i, j), ((BG_R + ghost_R)//2, (BG_G + ghost_G)//2, (BG_B + ghost_B)//2))

#Updating pygame display
pygame.display.update()

#Displaying completed image till user quits
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()



		

	
	 







 


