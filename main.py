import pygame
import openpyxl
from start_searching_button import StartSearchingButton
from input_box import TextInputBox
from input_box_button import InputBoxButton
from view_case_button import ViewCaseButton
from input_done import InputDone
from finish_viewing import FinishViewing

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (255, 100, 100)

# Set up the display window
size = (500, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AP CSP Pygame!")

# Set up fonts
my_font = pygame.font.SysFont('Arial', 15)
title_font = pygame.font.SysFont('Arial', 35)

# Set up the clock
clock = pygame.time.Clock()

# Create a new Excel workbook and select the default sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Headers for Excel sheet
if sheet.max_row == 1:
    headers = ["Case Name", "Ruling", "Case Type", "Civil Case Type", "Criminal Case Type", "Ruling Court", "Circuit Name"]
    sheet.append(headers)

# Set up custom objects
id_button = InputDone(300, 300)
start_button = StartSearchingButton(135, 200)
input_button = InputBoxButton(135, 200)
view_button = ViewCaseButton(135, 280)
finish_viewing_button = FinishViewing(250, 200)

case_input_box = TextInputBox(0, 30, 300, 30, my_font)
case_ruling_input = TextInputBox(0, 90, 300, 30, my_font)
criminal_or_civil_input = TextInputBox(0, 150, 300, 30, my_font)
specify_case_type_input = TextInputBox(0, 210, 300, 30, my_font)
ruling_court_input = TextInputBox(0, 270, 300, 30, my_font)
circuit_name_input = TextInputBox(0, 340, 300, 30, my_font)

# Set up variables for the display
end_title_click = False
second_screen = False
input_screen = False
run = True
view_cases = False

# Setting up statements to be blit later
case_input = my_font.render("What was the name of this case?", True, WHITE)
ruling_input = my_font.render("What was the ruling in this case?", True, WHITE)
case_type = my_font.render("What type of sector of law was this case: Criminal or Civil?", True, WHITE)
specify_case_type = my_font.render("What type of criminal or civil case is this case?", True, WHITE)
ruling_court_instruction = my_font.render("What was the ruling court in this case?", True, WHITE)
circuit_name_instruction = my_font.render("What circuit did this case take place in?", True, WHITE)

def handle_mouse_button_down(pos):
    global end_title_click, second_screen, input_screen, view_cases
    if not end_title_click:
        if start_button.rect.collidepoint(pos):
            end_title_click = True
            second_screen = True
    elif second_screen:
        if input_button.rect.collidepoint(pos):
            input_screen = True
            second_screen = False
        elif view_button.rect.collidepoint(pos):
            second_screen = False
            view_cases = True
    elif input_screen:
        if id_button.rect.collidepoint(pos):
            save_case_data()

def save_case_data():
    data = [
        [case_input_box.get_text(), case_ruling_input.get_text(), criminal_or_civil_input.get_text(), specify_case_type_input.get_text(),
        ruling_court_input.get_text(), circuit_name_input.get_text()]
    ]
    for row in data:
        sheet.append(row)
    workbook.save('case_data.xlsx')
    global input_screen, second_screen
    input_screen = False
    second_screen = True

# Main program loop
while run:
    clock.tick(60)

    # Main event loop
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_button_down(pos)

        # Handle input box events only when in input screen
        if input_screen:
            case_input_box.handle_event(event)
            case_ruling_input.handle_event(event)
            criminal_or_civil_input.handle_event(event)
            specify_case_type_input.handle_event(event)
            ruling_court_input.handle_event(event)
            circuit_name_input.handle_event(event)

    # Clear the screen
    screen.fill(LIGHT_RED)

    if not end_title_click:
        screen.blit(start_button.image, start_button.rect)
        screen.blit(title_font.render("JSTOR Law Database", True, WHITE), (35, 75))

    if second_screen:
        screen.blit(input_button.image, input_button.rect)
        screen.blit(view_button.image, view_button.rect)

    if input_screen:
        screen.fill(RED)

        # Blitting input texts and boxes
        screen.blit(case_input, (10, 10))
        case_input_box.update()
        case_input_box.draw(screen)

        screen.blit(ruling_input, (10, 70))
        case_ruling_input.update()
        case_ruling_input.draw(screen)

        screen.blit(case_type, (10, 130))
        criminal_or_civil_input.update()
        criminal_or_civil_input.draw(screen)

        screen.blit(specify_case_type, (10, 190))
        specify_case_type_input.update()
        specify_case_type_input.draw(screen)

        screen.blit(ruling_court_instruction, (10, 240))
        ruling_court_input.update()
        ruling_court_input.draw(screen)

        screen.blit(circuit_name_instruction, (10, 300))
        circuit_name_input.update()
        circuit_name_input.draw(screen)

        if case_input_box.get_text() and case_ruling_input.get_text() and criminal_or_civil_input.get_text() and specify_case_type_input.get_text() and ruling_court_input.get_text() and circuit_name_input.get_text():
            screen.blit(id_button.image, id_button.rect)

    pygame.display.update()

pygame.quit()

