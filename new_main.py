import pygame

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
title_font = pygame.font.SysFont('Arial', 35)
pygame.display.set_caption("AP CSP Pygame!")

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
    # Loop if Title Screen Remains
    while not end_title_click:
        title_screen = my_font.render("JSTOR Law Database", True, (255, 255, 255))
        screen.blit(title_screen, (200, 150))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and end_title_click == False:
                end_title_click = True


    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN and end_title_click == False:
            end_title_click = True

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    screen.blit(display_name, (0, 0))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

