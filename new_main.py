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

# Setting up Main Screen to Set up Start Searching Button


# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
finish_input_case = False

#Functions for the loop

# Rectangle Collisions

# def text_return_to_base():
#     text = ""
#     return text

def case_name_rect_collision:

def create_spreadsheet():


def case_name(text):
    name_text_surface = my_font.render(text, True, (255, 255, 255))
    return name_text_surface and case_input_rect


def input_data_in_spreadsheet():

def case_ruling(text):
    case_ruling_rect = pygame.Rect(100, 200, 10, 90)
    pygame.draw.rect(screen, color, case_ruling_rect, 2)
    ruling_text_surface = my_font.render(text, True, (255, 255, 255))
    return ruling_text_surface and case_ruling_rect

def case_type(text):
    case_type_rect = pygame.Rect(100, 200, 10, 110)
    pygame.draw.rect(screen, color, case_type_rect, 2)
    case_type_text_surface = my_font.render(text, True, (255, 255, 255))
    if case_type_text_surface == "Civil":
        civil_case_type = pygame.Rect(100, 200, 10, 130)
        pygame.draw.rect(screen, color, civil_case_type, 2)
        civil_case_text_surface = my_font.render(text, True, (255, 255, 255))
    else: # Could also create different functions within functions and then just important these functions within the parameters
        criminal_case_type = pygame.Rect(100, 200, 10, 130)
        pygame.draw.rect(screen, color, criminal_case_type, 2)
        criminal_case_text_surface = my_font.render(text, True, (255, 255, 255))
    return case_type_rect and case_type_text_surface and civil_case_text_surface and civil_case_type or criminal_case_text_surface and criminal_case_type

def ruling_court(text):
    ruling_court_text_surface = my_font.render(text, True, (255, 255, 255))
    return ruling_court_rect and ruling_court_text_surface


def circuit_name(text):
    circuit_name_text_surface = my_font.render(text, True, (255, 255, 255))
    return circuit_name_text_surface





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

        if end_title_click and :
            # Rectangle 1
            case_input_rect = pygame.Rect(100, 200, 10, 70)
            pygame.draw.rect(screen, color, case_input_rect, 2)
            if case_input_rect.collidepoint(pos):
                case_name(text)
            # Rectangle 2
            ruling_input_rect = pygame.Rect(200, 200, 100, 72)
            pygame.draw.rect(screen, color, ruling_input_rect, 2)
            if ruling_input_rect.collidepoint(pos):
                case_ruling(text)
            # Rectangle 3
            case_type_rect = pygame.Rect(100, 200, 10, 110)
            pygame.draw.rect(screen ,color, case_type_rect,2 )
            if case_type_rect.collidepoint(pos):
                case_type(text)
            # Rectangle 4
            ruling_court_rect = pygame.Rect(100, 200, 10, 150)
            pygame.draw.rect(screen, color, ruling_court_rect, 2)
            if ruling_court_rect.collidepoint(pos):
                ruling_court(text)
            # Rectangle 5
            circuit_name_rect = pygame.Rect(100, 200, 10, 170)
            pygame.draw.rect(screen, color, circuit_name_rect, 2)
            if circuit_name_rect.collidepoint(pos):
                circuit_name(text)



            if input_ruling_court == "Circuit" or "circuit" or "CIRCUIT":
                circuit_name = input("Which Federal Circuit did this ruling take place?")
                display_circuit_name = my_font.render(circuit_name, True, (255, 255, 255))
            else:
                display_circuit_name = my_font.render("", True, (255, 255, 255))
            finish_input_case = True
            data = [
                ["Case Name", "Ruling", "Case Type", "Civil Case Type", "Ruling Court", "Circuit Name"],
                [case_input_rect, input_ruling, input_case_type, input_ruling_court, circuit_name]
            ]
            for row in data:
                sheet.append(row)
            workbook.save(sheet.xlsx)
            spreadsheet_created = True
            display_case_spreadsheet = (sheet.xlsx, True, (255, 255, 255))
            number_of_enter = 0



        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((100, 100, 100))
    if not input_screen:
        screen.fill((100, 100, 100))
        screen.blit(i.rect, i.image, (200, 200))
        screen.blit(v.rect, v.image(200, 220))
    if input_screen == True:
        screen.fill((0, 0, 0))
        screen.blit(name_text_surface, (200, 220))
        screen.blit(ruling_text_surface, (200, 240))
        screen.blit(case_type_text_surface, (200, 260))
        screen.blit(case_type_rect, (200, 280))
        if
    if not end_title_click:
        screen.blit(title_screen, (35, 75))
        screen.blit(s.image, s.rect)

    if end_title_click:
        screen.fill((0, 0, 0))
        screen.blit(name_text_surface, (200, 220))
        screen.blit(ruling_text_surface, (200, 240))
        screen.blit(case_type_text_surface, (200, 260))
        screen.blit(case_type_rect, (200, 280))
        screen.blit()
        pygame.display.flip()
        screen.blit()
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

