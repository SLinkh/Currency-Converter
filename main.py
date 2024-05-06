import pygame
import random
import time
from bird import Bird
from balloon import Balloon


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
game_start_or_end_font = pygame.font.SysFont('Arial', 50)
pygame.display.set_caption("Balloon Flight!")





# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BIRD_START_X = 500


bg = pygame.image.load("background.png")
house = pygame.image.load("house.png")
tree = pygame.image.load("tree.png")




bird = Bird(BIRD_START_X, 250)
b = Balloon(300, 200)
end_click = False




INITIAL_HOUSE_X = random.randint(0,600)
INITIAL_TREE_X = random.randint(0,600)
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X








points = 0




# render the text for later


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
moved_object = False
game_over = False



# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0

while run:
   moved_object = False
   display_points = my_font.render("Score: " + str(points), True, (255, 255, 255))


   # --- Main event loop
   if end_click:
       clock.tick(60)
       if frame % 30 == 0:
           bird.switch_image()
       bird.move_bird()
       house_x = house_x + 1
       tree_x = tree_x + 1


       if house_x >= 820:
           house_x = -200
       if tree_x >= 820:
           tree_x = -200


   if not end_click:
       welcome_message = game_start_or_end_font.render("Welcome to balloon flight!", True, (255, 0, 0))
       display_instruction_one = my_font.render(str("Click the mouse to move the balloon up or down "), True, (255, 255, 255))
       display_instruction_two = my_font.render(str("Dodge the flying birds!"), True, (255, 255, 255))
       display_instruction_three = my_font.render(str("Click anywhere to start!"), True, (255, 255, 255))
       # display_instruction_four = my_font.render("W")


   if bird.rect.colliderect(b.rect):
       game_over = True
       game_over_message = game_start_or_end_font.render("GAME OVER!", True, (255, 0, 0))
       final_score = my_font.render("Final Score: " + str(points), True, (255, 255, 255))

   if not game_over:
       if bird.x == b.x and bird.y != b.y:
           points += 1


       for event in pygame.event.get():  # User did something
           if event.type == pygame.QUIT:  # If user clicked close
               run = False
           if event.type == pygame.MOUSEBUTTONDOWN and end_click == False:
               end_click = True
       keys = pygame.key.get_pressed()
       if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
           if frame % 2 == 0:
               b.move_balloon("up")
           moved_object == False
       elif not moved_object:
           if frame % 2 == 0:
               b.move_balloon("down")


   screen.blit(bg, (0, 0))
   if not end_click:
       screen.blit(welcome_message, (250, 225))
       screen.blit(display_instruction_one, (250, 275))
       screen.blit(display_instruction_two, (250, 300))
       screen.blit(display_instruction_three, (250, 325))
   if end_click == True and not game_over:
       screen.blit(house, (house_x, 360))
       screen.blit(tree, (tree_x, 360))
       screen.blit(bird.image, bird.rect)
       screen.blit(b.image, b.rect)
       screen.blit(display_points, (0, 10))
   if game_over:
       screen.blit(game_over_message, (250, 225))
       screen.blit(final_score, (250, 275))

   pygame.display.update()


   frame += 1


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()



