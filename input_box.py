import pygame
class TextInputBox:
        def __init__(self, x, y, w, h, font):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = pygame.Color('lightskyblue3')
            self.text = ''
            self.font = font
            self.txt_surface = self.font.render(self.text, True, self.color)
            self.active = False

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input box rect.
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)  # You can add any action you want to take on 'Enter' key press.
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    # Re-render the text.
                    self.txt_surface = self.font.render(self.text, True, self.color)

        def update(self):
            # Resize the box if the text is too long.
            width = max(200, self.txt_surface.get_width() + 10)
            self.rect.w = width

        def draw(self, screen):
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
            pygame.draw.rect(screen, self.color, self.rect, 2)

        def get_text(self):
            return self.text
