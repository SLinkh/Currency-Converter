import pygame
from start_searching_button import Start_Searching_Button
from input_box import TextInputBox
import openpyxl
import pandas as pd
clock = pygame.time.Clock()

# Create a new Excel workbook
workbook = openpyxl.Workbook()
# Select the default sheet (usually named 'Sheet')
sheet = workbook.active

input_rect = pygame.Rect(200,200,200,72)
text = ""
input_active = True


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
title_font = pygame.font.SysFont('Arial', 35)
pygame.display.set_caption("AP CSP Pygame!")
s = Start_Searching_Button(135, 200)
spreadsheet_created = False

# set up variables for the display

size = (400, 300)
screen = pygame.display.set_mode(size)
end_title_click = False
name = "JSTOR Law Database"

# Setting up Main Screen to Set up Start Searching Button


# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
finish_input_case = False

# -------- Main Program Loop -----------
while run:
    clock.tick(60)
    # --- Main event loop
    title_screen = title_font.render("JSTOR Law Database", True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not end_title_click:
            pos = pygame.mouse.get_pos()
            if s.rect.collidepoint(pos):
                finish_input_case = False
                end_title_click = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

        if end_title_click:
            input_case_name = input("Case Name: ")
            display_input_case_name = my_font.render(input_case_name, True, (255, 255, 255))
            # Put an input box next to the display input case name, and do for the rest of the inputs
            # once the number of cases ends, and the person hits enter, it goes back to the title screen
            input_ruling = input("Plantiff or Defense")
            display_input_ruling = my_font.render(input_ruling, True, (255, 255, 255))
            input_case_type = input("Criminal or Civil")
            display_input_case_type = my_font.render(input_case_type, True, (255, 255, 255))
            if input_case_type == "Civil":
                civil_case_type = input("What sector of law is this?")
                display_civil_case_typed = my_font.render(civil_case_type, True, (255, 255, 255))
            input_ruling_court = input("What type of court was this ruling in: Supreme, Circuit, or Court of Appeals?")
            display_input_ruling_court = my_font.render(input_ruling_court, True, (255, 255, 255))
            if input_ruling_court == "Circuit":
                circuit_name = input("Which Federal Circuit did this ruling take place?")
                display_circuit_name = my_font.render(circuit_name, True, (255, 255, 255))
            finish_input_case = True
            data = [
                ["Case Name", "Ruling", "Case Type", "Civil Case Type", "Ruling Court", "Circuit Name"],
                [input_case_name, input_ruling, input_case_type, civil_case_type, input_ruling_court, circuit_name]
            ]
            for row in data:
                sheet.append(row)
            workbook.save(case_excel_spreadsheet.xlsx)
            spreadsheet_created = True
            display_case_spreadsheet = (case_excel_spreadsheet.xlsx, True, (255, 255, 255))



        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((100, 100, 100))
    if not end_title_click:
        screen.blit(title_screen, (35, 75))
        screen.blit(s.image, s.rect)

    if end_title_click:
        screen.fill(0, 0, 0)
        text_surf = my_font.render(text, True, (255, 0, 0))
        screen.blit(text_surf, text_surf.get_rect(center=screen.get_rect().center))
        pygame.display.flip()
        # screen.fill((100, 100, 100))
        # screen.blit(display_input_case_name, (0, 10))
        # screen.blit(display_input_ruling, (0, 20))
        # screen.blit(display_input_case_type, (0, 30))
        # screen.blit(display_civil_case_typed, (0, 40))
        # screen.blit(display_input_ruling_court, (0, 50))
        # screen.blit(display_circuit_name, (0, 60))

    if end_title_click and spreadsheet_created:
        screen.blit(display_case_spreadsheet)
    if finish_input_case:
        #Give an option to play a "game"
        # Give an option to view the spreadsheet
        # Give an option to add another case
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

