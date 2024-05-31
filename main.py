import pygame
from start_searching_button import Start_Searching_Button
from input_box import TextInputBox
import openpyxl
import pandas as pd
from input_box_button import Input_Box_Button
from view_case_button import View_Case_Button
from input_done import Input_Done

clock = pygame.time.Clock()

# Create a new Excel workbook
workbook = openpyxl.Workbook()
# Select the default sheet (usually named 'Sheet')
sheet = workbook.active

input_rect = pygame.Rect(200,200,200,72)
color = pygame.Color('lightskyblue3')
text = ""
input_active = True




# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
title_font = pygame.font.SysFont('Arial', 35)
pygame.display.set_caption("AP CSP Pygame!")
id = Input_Done(100, 190)
s = Start_Searching_Button(135, 200)
i = Input_Box_Button(135, 200)




case_input_box = TextInputBox(100, 200, 10, my_font)
case_ruling_input = TextInputBox(100, 220, 10, my_font)
criminal_or_civil_input = TextInputBox(100, 240, 10, my_font)
specify_case_type_input = TextInputBox(100, 260, 10, my_font)
ruling_court_input = TextInputBox(100, 280, 10, my_font)
circuit_name_input = TextInputBox(100, 300, 10, my_font)


v = View_Case_Button(135, 220)
spreadsheet_created = False

# set up variables for the display

size = (400, 300)
screen = pygame.display.set_mode(size)
end_title_click = False
name = "JSTOR Law Database"
number_of_enter = 0

i.rect = pygame.draw.rect(screen, color, i, 2)
id.rect = pygame.draw.rect(screen, color, id, 2)
v.rect = pygame.draw.rect(screen, color, v, 2)
pygame.display.flip()

name_text_input = (" ")
case_ruling_text = (" ")
criminal_or_civil_text = (" ")
criminal_case_type_text = (" ")
civil_case_type_text = (" ")
ruling_court_text = (" ")
circuit_name_text = (" ")


run = True
finish_input_case = False
input_screen = False

# Setting up statements to be blit later
# In the Input Case Screen:
case_input = my_font.render("What was the name of this case? ", True, (255, 255, 255))
ruling_input = my_font.render("What was the ruling in this case?", True, (255, 255, 255))
case_type = my_font.render("What type of sector of law was this case: Criminal or Civil: ", True, (255, 255, 255))
specify_case_type = my_font.render("What type of criminal or civil case is this case?", True, (255, 255, 255))
ruling_court_instruction = my_font.render("What was the ruling court in this case? ", True, (255, 255, 255))
circuit_name_instruction = my_font.render("What circuit did this case take place in? ", True, (255, 255, 255))

# Setting up and initializing the rectangles
case_input_box.render_text()
case_ruling_input.render_text()
criminal_or_civil_input.render_text()
specify_case_type_input.render_text()
ruling_court_input.render_text()
circuit_name_input.render_text()

# -------- Main Program Loop -----------
while run:
    clock.tick(60)
    # --- Main event loop
    title_screen = title_font.render("JSTOR Law Database", True, (255, 255, 255))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and not end_title_click:
            if s.rect.collidepoint(pos):
                finish_input_case = False
                end_title_click = True
            if i.rect.collidepoint(pos) and end_title_click:
                input_screen = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                number_of_enter += 1
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode


    def case_name():
        case_input_rect = case_input_box.rect.update(event.type)
        case_name_text = text
        return case_input_rect and case_name_text

    def case_ruling():
        ruling_text_surface = case_ruling_input.rect.update(event.type)
        case_ruling_text = text
        return ruling_text_surface and case_ruling_text


    def criminal_or_civil_type():
        criminal_or_civil_text_surface = criminal_or_civil_input.rect.render_text()
        criminal_or_civil_input.rect.update(event.type)
        criminal_or_civil_text = text
        return criminal_or_civil_text_surface and criminal_or_civil_text


    def specify_case_type(criminal_or_civil_text):
        if criminal_or_civil_text == "Civil":
            civil_case_text_surface = specify_case_type_input.rect.update(event.type)
            civil_case_type_text = text
            return civil_case_text_surface and civil_case_type_text
        else:
            criminal_case_text_surface = specify_case_type_input.rect.update(event.type)
            criminal_case_type_text = text
            return criminal_case_type_text and criminal_case_text_surface


    def ruling_court():
        ruling_court_text_surface = ruling_court_input.rect.update(event.type)
        ruling_court_text = text
        return ruling_court_text_surface and ruling_court_text


    def circuit_name():
        circuit_name_text_surface = circuit_name_input.rect.update(event.type)
        name_text_input = text
        circuit_name_text_surface = my_font.render(circuit_name_text, True, (255, 255, 255))
        return circuit_name_text_surface and name_text_input

    if end_title_click and input_screen and finish_input_case:
        # Rectangle 1, case name
        case_input_rect = pygame.Rect(100, 200, 10, 70)
        pygame.draw.rect(screen, color, case_input_rect, 2)
        if case_input_rect.collidepoint(pos):
            name_text_input = case_name(event.type)

        # Rectangle 2, ruling input
        case_ruling_input = pygame.Rect(200, 200, 100, 72)
        pygame.draw.rect(screen, color, case_ruling_input, 2)
        if case_ruling_input.collidepoint(pos):
            ruling_text_surface = case_ruling(event.type)

        # Rectangle 3, criminal or civil
        criminal_or_civil_input = pygame.Rect(100, 200, 10, 110)
        pygame.draw.rect(screen,color, criminal_or_civil_input,2 )
        if criminal_or_civil_input.collidepoint(pos):
            criminal_or_civil = case_type(event.type)

        # Rectangle 4, Specify Case Type
        specify_case_type_rect = pygame.Rect(100, 200, 10, 130)
        pygame.draw.rect(screen, color, specify_case_type_rect, 2)
        if specify_case_type_rect.collidepoint(pos):
            specify_case_type(criminal_or_civil_text, event.type)

        # Rectangle 5, what was the ruling court?
        ruling_court_input = pygame.Rect(100, 200, 10, 150)
        pygame.draw.rect(screen, color, ruling_court_input, 2)
        if ruling_court_input.collidepoint(pos):
            ruling_court(event.type)

        # Rectangle 6 - what was the circuit, if applicable
        circuit_name_input = pygame.Rect(100, 200, 10, 170)
        pygame.draw.rect(screen, color, circuit_name_input, 2)
        if circuit_name_input.collidepoint(pos):
            circuit_name(event.type)


        if id.rect.collidepoint(100, 190):
            finish_input_case = True
            input_screen = False
            title_screen = True
        data = [
            ["Case Name", "Ruling", "Case Type", "Civil Case Type", "Criminal Case Type", "Ruling Court", "Circuit Name"],
            [case_name_text, case_ruling_text, criminal_or_civil_text, civil_case_type_text, criminal_case_type_text, ruling_court_text,  circuit_name_text]
        ]
        for row in data:
            sheet.append(row)
        workbook.save(sheet.xlsx)
        spreadsheet_created = True
        display_case_spreadsheet = (sheet.xlsx, True, (255, 255, 255))

    if event.type == pygame.QUIT:  # If user clicked close
        run = False

    screen.fill((100, 100, 100))
    if not input_screen:
        screen.fill((100, 100, 100))
        screen.blit(i.image, i.rect)
        screen.blit(v.image, v.rect)

    if input_screen == True:
        screen.fill((0, 0, 0))

        # Blitting Input 1
        screen.blit(case_input, (0, 10))
        screen.blit(screen, case_input_box)

        # Blitting Input 2
        screen.blit(ruling_input, (0, 30))
        screen.blit(screen, case_ruling_input)

        # Blitting Input 3
        screen.blit(case_type, (0, 50))
        screen.blit(screen, criminal_or_civil_input)

        # Blitting Input 4
        screen.blit(ruling_court_instruction, (0, 70))
        screen.blit(screen, ruling_court_input)

        # Blitting Input 5
        screen.blit(circuit_name_instruction, (0, 90))
        screen.blit(screen, circuit_name_input)

        #Blitting Input 6
        # screen.blit(specify_case_type, (0, 110))
        # screen.blit()
    if name_text_input != " " and ruling_text_surface != " " and criminal_or_civil != " " and ruling_court_rect != " " and circuit_name != " " and specify_case_type != " ":
        screen.blit()
    if not end_title_click:
        screen.blit(title_screen, (35, 75))
        screen.blit(s.image, s.rect)


    # if end_title_click and spreadsheet_created and :
    #     screen.blit(display_case_spreadsheet)
    # if finish_input_case:
        #Give an option to play a "game"
        # Give an option to view the spreadsheet
        # Give an option to add another case
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

