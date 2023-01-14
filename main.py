import os.path

import pygame
import json
from timer_py import Timer
from sys import argv


def init_pygame():
    """pygame initialisation"""
    global screen, display, clock, window_size
    pygame.init()
    window_size = (1280, 720)
    pygame.display.set_caption('Animation')
    screen = pygame.display.set_mode(window_size, 0, 32)
    clock = pygame.time.Clock()


def init_time():
    """synchronisation timer between audio and video initialisation"""
    global timer
    timer = Timer('Main Timer').start()


def init_audio():
    """audio initialisation"""
    pygame.mixer.music.load(audio_path)
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


def get_emotes():
    """searching for optional tags in transcription"""
    transcript_and_emotes_t = []
    with open(transcript_path, 'r') as f:
        transcript_and_emotes_raw = str(f.read()).split()
        try:
            real_j = 0
            for i in range(0, len(transcript_and_emotes_raw)):
                if '<' in transcript_and_emotes_raw[i]:
                    real_j -= 1
                    for j in range(i, len(transcript_and_emotes_raw)):
                        if '<' in transcript_and_emotes_raw[j]:
                            pass
                        else:
                            pos = j + real_j
                            break
                    transcript_and_emotes_t.append([pos, transcript_and_emotes_raw[i]])

        except IndexError:
            pass
    return transcript_and_emotes_t


# ================= pygame screen/event functions


def quit_button():
    """quit button for pygame"""
    global cycle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cycle = False


def clear_screen():
    """pygame function what makes screen violet(be default) to paint out previous frame"""
    screen.fill((200, 200, 255))


def refresh_screen():
    """pygame function"""
    pygame.display.flip()
    clock.tick(60)


def display_fps():
    """pygame service function, not used in release"""
    render(
        fonts[0],
        text='FPS:',
        color="black",
        where=(0, 0),
        centered=False)
    render(
        fonts[0],
        text=str(int(clock.get_fps())),
        color="black",
        where=(50, 0),
        centered=False)


def get_background(background_path_t, window_size_t):
    """pygame service function, used to initialise background"""
    background_png_t = pygame.image.load(background_path_t)
    return pygame.transform.scale(background_png_t, window_size_t)


def display_background():
    """pygame service function, used to show current background"""
    screen.blit(background, (0, 0))


def display_clock():
    """pygame service function, not used in release"""
    elapsed = timer.elapsed(print=False)
    point_pos = str(elapsed).find('.')
    render(
        fonts[0],
        text='TIME:',
        color="black",
        where=(0, 20),
        centered=False)
    render(
        fonts[0],
        text=str(elapsed)[:point_pos + 3],
        color="black",
        where=(60, 20),
        centered=False)


def display_texts():
    """pygame service function, used to show current word"""
    global current_phone, current_word
    time_now = timer.elapsed(print=False)
    if current_time_start <= time_now <= current_time_end:
        try:
            render(
                fonts[2],
                text=str(current_word['word']),
                color="black",
                where=(window_size[0], window_size[1] * 0.2),
                centered=True)
            render(
                fonts[2],
                text=str(current_phone['phone']),
                color="black",
                where=(window_size[0] * 0.3, window_size[1] * 0.4),
                centered=True)
        except NameError:
            pass


def display_body():
    """pygame function that decides which body posture it must show"""
    current_body_png = down_hands_png
    current_body_position = (window_size[0] * 0.70, window_size[1] * 0.15)
    if emote_hands == emotes_hands[0]:
        current_body_png = down_hands_png
        current_body_position = (window_size[0] * 0.70, window_size[1] * 0.15)
    elif emote_hands == emotes_hands[1]:
        current_body_png = up_hands_png
        current_body_position = (window_size[0] * 0.6925, window_size[1] * 0.15)
    elif emote_hands == emotes_hands[2]:
        current_body_png = pointing_hands_png
        current_body_position = (window_size[0] * 0.5925, window_size[1] * 0.15)
    elif emote_hands == emotes_hands[3]:
        current_body_png = thinking_hands_png
        current_body_position = (window_size[0] * 0.6985, window_size[1] * 0.15)
    elif emote_hands == emotes_hands[4]:
        current_body_png = crossed_hands_png
        current_body_position = (window_size[0] * 0.687, window_size[1] * 0.15)
    screen.blit(current_body_png, (current_body_position[0], current_body_position[1]))


def display_brows_and_eyes(x, y):
    """pygame function that decides which eyes and brows it must show"""
    current_brows_png = normal_brows_png
    current_eyes_png = normal_eyes_png
    if emote_face == emotes_face[0]:
        current_brows_png = normal_brows_png
        current_eyes_png = normal_eyes_png
    elif emote_face == emotes_face[1]:
        current_brows_png = angry_brows_png
        current_eyes_png = angry_eyes_png
    elif emote_face == emotes_face[2]:
        current_brows_png = clueless_brows_png
        current_eyes_png = clueless_eyes_png
    screen.blit(current_eyes_png, (x + 10, y + 10))
    screen.blit(current_brows_png, (x, y))


def display_mouths(x, y):
    """pygame function that decides which viseme it should show"""
    # print(current_phone['phone'].split('_')[0])
    wrong_vowel = False
    if current_phone['phone'].split('_')[0] in types_mouth[0]:
        current_mouth_png = open_vowel_mouth_png
    elif current_phone['phone'].split('_')[0] in types_mouth[1]:
        current_mouth_png = closed_vowel_mouth_png
    elif current_phone['phone'].split('_')[0] in types_mouth[2]:
        current_mouth_png = thin_vowel_mouth_png
    elif current_phone['phone'].split('_')[0] in types_mouth[3]:
        current_mouth_png = consonants_open_mouth_png
    elif current_phone['phone'].split('_')[0] in types_mouth[4]:
        current_mouth_png = consonants_hissing_mouth_png
    elif current_phone['phone'].split('_')[0] in types_mouth[5]:
        current_mouth_png = consonants_crunch_mouth_png
    elif current_phone['phone'].split('_')[0] in types_mouth[6]:
        current_mouth_png = consonants_crunch_thud_mouth_png
    elif current_phone['phone'].split('_')[0] in types_mouth[7]:
        current_mouth_png = consonants_closed_mouth_png
    else:
        current_mouth_png = error_png
        wrong_vowel = True
    if current_word['end'] < time_now or time_now < current_word['start']:
        if wrong_vowel:
            current_mouth_png = error_png
        else:
            current_mouth_png = closed_mouth_png
    screen.blit(current_mouth_png, (x, y))


def update_screen():
    """function what does all pygame drawing scripts in order"""
    if use_background:
        display_background()
    else:
        clear_screen()
    display_texts()
    display_body()
    display_brows_and_eyes(eyes_position[0], eyes_position[1])
    display_mouths(mouth_position[0], mouth_position[1])
    refresh_screen()


# =================


if len(argv) == 1:  # taking arguments from cmd/os.system('main.py True')
    gentle_path = os.path.abspath('../gentle-animation-maker')
    script, audio_path, transcript_path, json_path = \
    [f'{gentle_path}/main.py',
     f'{gentle_path}/test_directory/test_reading_skills/a.wav',
     f'{gentle_path}/test_directory/test_reading_skills/transcript.txt',
     f'{gentle_path}/current_test/a.json']
elif len(argv) == 5:  # taking arguments from cmd/os.system('main.py False *.mp3 *.txt *.json')
    script, key, audio_path, transcript_path, json_path = argv
    background_path = ''
elif len(argv) == 6:  # taking arguments from cmd/os.system('main.py False *.mp3 *.txt *.json *.png')
    script, key, audio_path, transcript_path, json_path, background_path = argv
else:  # handling wrong amount of input
    print(f'Error: Expected 1/5/6 arguments, got {len(argv)-1}')
    raise SystemExit


transcript_and_emotes = get_emotes()  # getting emotes to show in animation

json_align = get_json(json_path)  # gathering phoneme data from json
# todo make backgrounds


emote_face_tag = '<face:'  # tag body used in transcription
emote_hands_tag = '<hands:'  # tag body used in transcription

normal_brows_png = pygame.image.load('vector/brows/brows (2).png')
normal_brows_png = pygame.transform.scale(normal_brows_png, (70, 8.4))
angry_brows_png = pygame.image.load('vector/brows/brows (1).png')
angry_brows_png = pygame.transform.scale(angry_brows_png, (70, 11.9))
clueless_brows_png = pygame.image.load('vector/brows/brows (3).png')
clueless_brows_png = pygame.transform.scale(clueless_brows_png, (70, 16.8))

normal_eyes_png = pygame.image.load('vector/eye/eye (1).png')
normal_eyes_png = pygame.transform.scale(normal_eyes_png, (49, 19.3))
angry_eyes_png = pygame.image.load('vector/eye/eye (2).png')
angry_eyes_png = pygame.transform.scale(angry_eyes_png, (49, 19.3))
clueless_eyes_png = pygame.image.load('vector/eye/eye (3).png')
clueless_eyes_png = pygame.transform.scale(clueless_eyes_png, (49, 19.3))
emotes_face = ['normal', 'angry', 'clueless']
emote_face = emotes_face[0]


down_hands_png = pygame.image.load('vector/body/body (4).png')
down_hands_png = pygame.transform.scale(down_hands_png, (190, 600))
up_hands_png = pygame.image.load('vector/body/body (2).png')
up_hands_png = pygame.transform.scale(up_hands_png, (211, 600))
pointing_hands_png = pygame.image.load('vector/body/body (1).png')
pointing_hands_png = pygame.transform.scale(pointing_hands_png, (328, 600))
thinking_hands_png = pygame.image.load('vector/body/body (5).png')
thinking_hands_png = pygame.transform.scale(thinking_hands_png, (193, 600))
crossed_hands_png = pygame.image.load('vector/body/body (3).png')
crossed_hands_png = pygame.transform.scale(crossed_hands_png, (224, 600))
emotes_hands = ['down', 'up', 'pointing', 'thinking', 'crossed']
emote_hands = emotes_hands[0]


normal_mouth_png = pygame.image.load('vector/mouth/mouth (8).png')
normal_mouth_png = pygame.transform.scale(normal_mouth_png, (37.7, 19.3))
open_vowel_mouth_png = pygame.image.load('vector/mouth/mouth (16).png')
open_vowel_mouth_png = pygame.transform.scale(open_vowel_mouth_png, (37.7, 19.3))
closed_vowel_mouth_png = pygame.image.load('vector/mouth/mouth (9).png')
closed_vowel_mouth_png = pygame.transform.scale(closed_vowel_mouth_png, (37.7, 19.3))
thin_vowel_mouth_png = pygame.image.load('vector/mouth/mouth (17).png')
thin_vowel_mouth_png = pygame.transform.scale(thin_vowel_mouth_png, (37.7, 19.3))
consonants_open_mouth_png = pygame.image.load('vector/mouth/mouth (11).png')
consonants_open_mouth_png = pygame.transform.scale(consonants_open_mouth_png, (37.7, 19.3))
consonants_hissing_mouth_png = pygame.image.load('vector/mouth/mouth (17).png')
consonants_hissing_mouth_png = pygame.transform.scale(consonants_hissing_mouth_png, (37.7, 19.3))
consonants_crunch_mouth_png = pygame.image.load('vector/mouth/mouth (6).png')
consonants_crunch_mouth_png = pygame.transform.scale(consonants_crunch_mouth_png, (37.7, 19.3))
consonants_crunch_thud_mouth_png = pygame.image.load('vector/mouth/mouth (7).png')
consonants_crunch_thud_mouth_png = pygame.transform.scale(consonants_crunch_thud_mouth_png, (37.7, 19.3))
consonants_closed_mouth_png = pygame.image.load('vector/mouth/mouth (8).png')
consonants_closed_mouth_png = pygame.transform.scale(consonants_closed_mouth_png, (37.7, 19.3))
closed_mouth_png = pygame.image.load('vector/mouth/mouth (19).png')
closed_mouth_png = pygame.transform.scale(closed_mouth_png, (34.5, 21.5))
error_png = pygame.image.load('vector/eye/eye (1).png')
error_png = pygame.transform.scale(error_png, (37.7, 19.3))

types_mouth = [['ah', 'eh', 'ae', 'ay', 'ey'], ['uh', 'uw', 'y', 'aw', 'er', 'w', 'hh'],
               ['ih', 'ey', 'iy'], ['g', 'd', 'k', 'n', 'r'], ['s', 'z', 't'], ['ch'],
               ['f', 'v', 'dh', 'jh', 'ng', 'th'], ['m']]

current_word_pos = 0
current_phone_pos = 0
current_word = json_align['words'][current_word_pos]
current_phone = current_word['phones'][current_phone_pos]
current_word_len = len(current_word['phones'])
current_time_start = current_word['start']
current_time_end = current_word['end']
time_now = 0.0
word_ended = False
transcript_ended = False


init_pygame()  # explanations in the body of the function
init_time()  # explanations in the body of the function
init_audio()  # explanations in the body of the function

try:
    if background_path:
        use_background = True
        background = get_background(background_path, window_size)
    else:
        use_background = False
except NameError:
    use_background = False

fonts = init_fonts([25, 30, 60])

eyes_position = (window_size[0] * 0.747, window_size[1] * 0.25)  # default position for eyes
head_position = (window_size[0] * 0.70, window_size[1] * 0.15)  # default position for body
mouth_position = (window_size[0] * 0.76, window_size[1] * 0.305)  # default position for mouth

cycle = True
while cycle:
    if not transcript_ended:
        time_now = timer.elapsed(print=False)  # timer present value
        if current_time_end <= time_now:
            word_ended = False
            if current_word_pos >= len(json_align['words']) - 1:  # check whether we should continue
                transcript_ended = True
            if not transcript_ended:
                for emote in transcript_and_emotes:  # check whether we should change emotes
                    if emote_face_tag in emote[1]:
                        if current_word_pos == emote[0]:
                            emote_face = emote[1][6:-1]
                    if emote_hands_tag in emote[1]:
                        if current_word_pos == emote[0]:
                            emote_hands = emote[1][7:-1]
                current_word_pos += 1  # redefining
                current_phone_pos = 0  # redefining
                current_word = json_align['words'][current_word_pos]  # redefining
                current_word_len = len(current_word['phones'])  # redefining
                current_time_start, current_time_end = current_word['start'], current_word['end']  # redefining
        if not transcript_ended:
            if current_time_start <= time_now and not word_ended:
                current_phone = current_word['phones'][current_phone_pos]
                if (current_phone['duration'] + current_time_start) <= time_now:  # check whether we should change phoneme
                    current_phone_pos += 1
                    if current_phone_pos == current_word_len:
                        word_ended = True
    update_screen()  # explanations in the body of the function
    quit_button()
pygame.quit()  # explanations in the body of the function
