import pygame
from start_searching_button import Start_Searching_Button
from input_box import TextInputBox
import openpyxl
import pandas as pd
from input_box_button import Input_Box_Button
from view_case_button import View_Case_Button

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
s = Start_Searching_Button(135, 200)
i = Input_Box_Button(135, 200)
v = View_Case_Button(135, 220)
spreadsheet_created = False

# set up variables for the display

size = (400, 300)
screen = pygame.display.set_mode(size)
end_title_click = False
name = "JSTOR Law Database"
number_of_enter = 0

case_name_text = (" ")
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
ruling_court = my_font.render("What was the ruling court in this case? ", True, (255, 255, 255))
circuit_name = my_font.render("What circuit did this case take place in? ", True, (255, 255, 255))

#Functions for the loop

# Rectangle Collisions

# def text_return_to_base():
#     text = ""
#     return text


# def create_spreadsheet():


def case_name(text):
    case_name_text = text
    name_text_surface = my_font.render(case_name_text, True, (255, 255, 255))
    return name_text_surface and case_input_rect


def case_ruling(text):
    case_ruling_text = text
    ruling_text_surface = my_font.render(case_ruling_text, True, (255, 255, 255))
    return ruling_text_surface and case_ruling_text

def criminal_or_civil_type(text):
    criminal_or_civil_text = text
    criminal_or_civil_text_surface = my_font.render(criminal_or_civil_text, True, (255, 255, 255))
    return criminal_or_civil_text_surface and criminal_or_civil_text

def specify_case_type(text, criminal_or_civil_text):
    if criminal_or_civil_text == "Civil":
        civil_case_type_text = text
        civil_case_text_surface = my_font.render(civil_case_type_text, True, (255, 255, 255))
        return civil_case_text_surface and civil_case_type_text
    else: # Could also create different functions within functions and then just important these functions within the parameters
        criminal_case_type = pygame.Rect(100, 200, 10, 130)
        pygame.draw.rect(screen, color, criminal_case_type, 2)
        criminal_case_non_surface = ("Criminal Case Type: ", True, (255, 255, 255))
        criminal_case_type_text = text
        criminal_case_text_surface = my_font.render(criminal_case_type_text, True, (255, 255, 255))
        return criminal_case_non_surface and criminal_case_text_surface


def ruling_court(text):
    ruling_court_text = text
    ruling_court_text_surface = my_font.render(ruling_court_text, True, (255, 255, 255))
    return ruling_court_rect and ruling_court_text_surface and ruling_court_text


def circuit_name(text):
    circuit_name_text = text
    circuit_name_text_surface = my_font.render(circuit_name_text, True, (255, 255, 255))
    return circuit_name_text_surface and circuit_name_text

def create_text(text, rectangle_collided_with, unicode):
    text += unicode
    # add a line of code where the text will be added to the rectangle through this function
    # like in the normal code, it will be if collidepoint add the text into the rectangle you want to add it into

# def go_to_new_rectangle:
    # If you are moving to a new rectangle, keep the text in the old rectangle, and nothing will happen

name_text_input = case_name(text)
ruling_text_surface = case_ruling(text)
criminal_or_civil = criminal_or_civil_type(text)
specify_case_type_text = specify_case_type(text)
ruling_court(text)
circuit_name(text)


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
            if i.rect.collide_point(pos) and end_title_click:
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

        if end_title_click and input_screen:
            # Rectangle 1, case name
            case_input_rect = pygame.Rect(100, 200, 10, 70)
            pygame.draw.rect(screen, color, case_input_rect, 2)
            if case_input_rect.collidepoint(pos):
                name_text_input = case_name(text)

            # Rectangle 2, ruling input
            ruling_input_rect = pygame.Rect(200, 200, 100, 72)
            pygame.draw.rect(screen, color, ruling_input_rect, 2)
            if ruling_input_rect.collidepoint(pos):
                ruling_text_surface = case_ruling(text)

            # Rectangle 3, criminal or civil
            case_type_rect = pygame.Rect(100, 200, 10, 110)
            pygame.draw.rect(screen,color, case_type_rect,2 )
            if case_type_rect.collidepoint(pos):
                criminal_or_civil = case_type(text)

            # Rectangle 4, what was the ruling court?
            ruling_court_rect = pygame.Rect(100, 200, 10, 150)
            pygame.draw.rect(screen, color, ruling_court_rect, 2)
            if ruling_court_rect.collidepoint(pos):
                ruling_court(text)
            # Rectangle 5 - what was the circuit, if applicable
            circuit_name_rect = pygame.Rect(100, 200, 10, 170)
            pygame.draw.rect(screen, color, circuit_name_rect, 2)
            if circuit_name_rect.collidepoint(pos):
                circuit_name(text)

            specify_case_type_rect = pygame.Rect(100, 200, 10, 190)
            pygame.draw.rect(screen, color, specify_case_type_rect, 2)
            if specify_case_type_rect.collidepoint(pos):
                specify_case_type(text, criminal_or_civil_text)

            finish_input_case = True
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
        screen.blit(i.rect, i.image, (200, 200))
        screen.blit(v.rect, v.image(200, 220))

    if input_screen == True:
        screen.fill((0, 0, 0))

        # Blitting Input 1
        screen.blit(case_input, (0, 10))
        screen.blit(name_text_input, case_input_rect)

        # Blitting Input 2
        screen.blit(ruling_input, (0, 30))
        screen.blit(ruling_text_surface, ruling_input_rect)

        # Blitting Input 3
        screen.blit(case_type, (0, 50))
        screen.blit(criminal_or_civil, case_type_rect)

        # Blitting Input 4
        screen.blit(ruling_court, (0, 70))
        screen.blit(ruling_court_rect, (50, 70))

        # Blitting Input 5
        screen.blit(circuit_name, (0, 90))
        screen.blit(circuit_name_rect, (50, 90))

        #Blitting Input 6
        screen.blit(specify_case_type, (0, 110))
        screen.blit()
    if name_text_input != " " and ruling_text_surface != " " and criminal_or_civil != " " and ruling_court_rect != " " and circuit_name != " " and specify_case_type != " ":
        screen.blit()
    if not end_title_click:
        screen.blit(title_screen, (35, 75))
        screen.blit(s.image, s.rect)


    if end_title_click and spreadsheet_created and :
        screen.blit(display_case_spreadsheet)
    # if finish_input_case:
        #Give an option to play a "game"
        # Give an option to view the spreadsheet
        # Give an option to add another case
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

