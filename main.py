import pygame
import json
from timer_py import Timer


def init_pygame():
    """pygame initialisation"""
    global screen, display, clock
    pygame.init()
    window_size = (600, 400)
    pygame.display.set_caption('Animation')
    screen = pygame.display.set_mode(window_size, 0, 32)
    clock = pygame.time.Clock()


def init_time():
    """synchronisation timer between audio and video initialisation"""
    global timer
    timer = Timer('Main Timer').start()


def init_audio():
    """audio initialisation"""
    global dir_name
    pygame.mixer.music.load(f'test_directory/{dir_name}/a.wav')
    pygame.mixer.music.play()


def init_fonts(font_sizes):
    """simple font initialisation"""
    fonts_to_create = []
    for size in font_sizes:
        fonts_to_create.append(
            pygame.font.SysFont("Arial", size))
    return fonts_to_create


def render(font, text, color, where, centered):
    """simple render function for further usage in other functions"""
    text_to_show = font.render(text, 0, pygame.Color(color))
    if centered:
        where = text_to_show.get_rect(center=(where[0] // 2, where[1]))
    screen.blit(text_to_show, where)


def get_json(name):
    """receiving aligned text for further usage"""
    file = open(name)
    aligned_json = json.load(file)
    for word_block_na in aligned_json['words']:
        if word_block_na['case'] != 'success':
            aligned_json['words'].remove(word_block_na)
    return aligned_json


def what_should_i_show():
    """main function to define which word and phoneme we must show now"""
    global current_time_end, \
        current_word_pos, word_ended, \
        current_time_start, current_word, \
        current_phone_pos, current_word_len, \
        current_phone, current_word, transcript_ended
    if not transcript_ended:
        time_now = timer.elapsed(print=False)  # timer present value
        if current_time_end <= time_now:
            word_ended = False
            if current_word_pos >= len(json_align['words']) - 1:  # check whether we should continue
                transcript_ended = True
                print('ended!')
            if not transcript_ended:
                current_word_pos += 1
                current_phone_pos = 0
                current_word = json_align['words'][current_word_pos]
                current_word_len = len(current_word['phones'])
                current_time_start, current_time_end = \
                    current_word['start'], current_word['end']
        if not transcript_ended:
            if current_time_start <= time_now and not word_ended:
                current_phone = current_word['phones'][current_phone_pos]
                if (current_phone['duration'] + current_time_start) <= time_now:
                    current_phone_pos += 1
                    if current_phone_pos == current_word_len:
                        word_ended = True


# =================
# ================= pygame screen/event functions
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
        text='FPS:',
        color="white",
        where=(0, 0),
        centered=False)
    render(
        fonts[0],
        text=str(int(clock.get_fps())),
        color="white",
        where=(50, 0),
        centered=False)


def display_clock():
    elapsed = timer.elapsed(print=False)
    point_pos = str(elapsed).find('.')
    render(
        fonts[0],
        text='TIME:',
        color="white",
        where=(0, 20),
        centered=False)
    render(
        fonts[0],
        text=str(elapsed)[:point_pos+3],
        color="white",
        where=(60, 20),
        centered=False)


def display_phone_and_word():
    global current_phone, current_word
    time_now = timer.elapsed(print=False)
    if current_time_start <= time_now <= current_time_end:
        try:
            render(
                fonts[2],
                text=str(current_word['alignedWord']),
                color="white",
                where=(600, 300),
                centered=True)
            render(
                fonts[2],
                text=str(current_phone['phone']),
                color="white",
                where=(600, 175),
                centered=True)
        except NameError:
            pass


def update_screen():
    """where everything happens"""
    quit_button()
    clear_screen()
    display_fps()
    display_phone_and_word()
    display_clock()
    refresh_screen()


# =================
# =================
# =================


dir_name = 'test_short'
init_pygame()
init_time()
init_audio()
fonts = init_fonts([25, 30, 60])

json_align = get_json(f'test_directory/{dir_name}/align.json')
current_word_pos = 0
current_phone_pos = 0
current_word = json_align['words'][current_word_pos]
current_phone = current_word['phones'][current_phone_pos]
current_word_len = len(current_word['phones'])
current_time_start = current_word['start']
current_time_end = current_word['end']
word_ended = False
transcript_ended = False
cycle = True
while cycle:
    what_should_i_show()
    update_screen()
pygame.quit()
