import pygame
import json


def init_global():
    global screen, display, clock
    pygame.init()
    window_size = (600, 400)
    pygame.display.set_caption('Animation')
    screen = pygame.display.set_mode(window_size, 0, 32)
    clock = pygame.time.Clock()


def create_fonts(font_sizes):
    fonts = []
    for size in font_sizes:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts


def render(font, text, color, where):
    text_to_show = font.render(text, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def get_json(name):
    file = open(name)
    aligned_json = json.load(file)
    for word_block in aligned_json['words']:
        if word_block['case'] != 'success':
            aligned_json['words'].remove(word_block)
    return aligned_json


# =================
def quit_button():
    global cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cycle = False


def clear_screen():
    screen.fill((0, 0, 0))


def refresh_screen():
    pygame.display.flip()
    clock.tick(60)


def display_fps():
    render(
        fonts[0],
        text=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))


def update_screen():
    """where everything happens"""
    quit_button()
    clear_screen()
    display_fps()
    refresh_screen()


init_global()
fonts = create_fonts([32])
json_align = get_json('4288fe51/align.json')
cycle = True
while cycle:
    update_screen()
pygame.quit()
