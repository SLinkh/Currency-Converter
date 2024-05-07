import pygame
from start_searching_button import Start_Searching_Button

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
title_font = pygame.font.SysFont('Arial', 35)
pygame.display.set_caption("AP CSP Pygame!")
s = Start_Searching_Button(135, 200)

# set up variables for the display

size = (400, 300)
screen = pygame.display.set_mode(size)
end_title_click = False
name = "JSTOR Law Database"

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    title_screen = title_font.render("JSTOR Law Database", True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not end_title_click:
            pos = pygame.mouse.get_pos()
            if s.rect.colldepoint(pos):
                end_title_click = True

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((100, 100, 100))
    if not end_title_click:
        screen.blit(title_screen, (35, 75))
        screen.blit(s.image, s.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

