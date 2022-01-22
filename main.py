import pygame
import json


def init_global():
    global screen, display, clock
    pygame.init()
    window_size = (600, 400)
    pygame.display.set_caption('Animation')
    screen = pygame.display.set_mode(window_size, 0, 32)
    clock = pygame.time.Clock()


def init_time_machine():
    global miliseconds, counter_miliseconds
    miliseconds = 0
    counter_miliseconds = 0


def refresh_time():
    global miliseconds, counter_miliseconds
    miliseconds += 16
    counter_miliseconds += 1
    if counter_miliseconds == 3:
        miliseconds += 2
        counter_miliseconds = 0
    if miliseconds == 5000:
        miliseconds = 0


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
    for word_block_na in aligned_json['words']:
        if word_block_na['case'] != 'success':
            aligned_json['words'].remove(word_block_na)
    return aligned_json


def what_should_i_show():
    global transcript_ended, current_time_end, \
        current_word_pos, word_ended, \
        current_time_start, current_word, \
        current_phone_pos, current_word_len, \
        current_phone, current_word, \
        miliseconds

    if not transcript_ended:
        if (current_time_end * 1000) <= miliseconds:
            word_ended = False
            if current_word_pos >= json_len - 1:
                transcript_ended = True
                print('ended!')
            if not transcript_ended:
                current_word_pos += 1
                current_phone_pos = 0
                current_word = json_align['words'][current_word_pos]
                current_word_len = len(current_word['phones'])
                current_time_start = current_word['start']
                current_time_end = current_word['end']
        if not transcript_ended:
            if (current_time_start * 1000) <= miliseconds and not word_ended:
                current_phone = current_word['phones'][current_phone_pos]
                if ((current_phone['duration'] + current_time_start) * 1000) <= miliseconds:
                    current_phone_pos += 1
                    if current_phone_pos == current_word_len:
                        word_ended = True


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


def display_phone():
    global current_phone, current_word
    try:
        render(
            fonts[0],
            text=str(current_phone['phone']),
            color="white",
            where=(200, 200))
        render(
            fonts[0],
            text=str(current_word['alignedWord']),
            color="white",
            where=(200, 150))
    except NameError:
        pass


def update_screen():
    """where everything happens"""
    quit_button()
    clear_screen()
    display_fps()
    display_phone()
    refresh_screen()


init_global()
init_time_machine()
fonts = create_fonts([32])
json_align = get_json('3447c646/align.json')
pygame.mixer.music.load('3447c646/a.wav')
pygame.mixer.music.play()
cycle = True
current_word_pos = 0
current_phone_pos = 0
json_len = len(json_align['words'])
current_word = json_align['words'][current_word_pos]
current_word_len = len(current_word['phones'])
current_time_start = current_word['start']
current_time_end = current_word['end']
word_ended = False
transcript_ended = False
while cycle:
    refresh_time()
    what_should_i_show()  # todo не работает на большой дистанции
    update_screen()
pygame.quit()
