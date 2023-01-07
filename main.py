import pygame
import json
from timer_py import Timer


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
        current_phone, current_word, transcript_ended, \
        transcript_and_emotes, emote_face_tag, emote_hands_tag, emote_face, emote_hands
    if not transcript_ended:
        time_now = timer.elapsed(print=False)  # timer present value
        if current_time_end <= time_now:
            word_ended = False
            if current_word_pos >= len(json_align['words']) - 1:  # check whether we should continue
                transcript_ended = True
                print('ended!')
            if not transcript_ended:
                if emote_face_tag in transcript_and_emotes[current_word_pos]:
                    emote_tag = transcript_and_emotes.pop(current_word_pos)
                    emote_face = emote_tag[6:-1]
                if emote_hands_tag in transcript_and_emotes[current_word_pos]:
                    emote_tag = transcript_and_emotes.pop(current_word_pos)
                    emote_hands = emote_tag[7:-1]
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
    screen.fill((200, 200, 255))


def refresh_screen():
    pygame.display.flip()
    clock.tick(60)


def display_fps():
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


def display_clock():
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
        text=str(elapsed)[:point_pos+3],
        color="black",
        where=(60, 20),
        centered=False)


def display_texts():
    global current_phone, current_word
    time_now = timer.elapsed(print=False)
    if current_time_start <= time_now <= current_time_end:
        try:
            render(
                fonts[2],
                text=str(current_word['alignedWord']),
                color="black",
                where=(window_size[0]*0.3, window_size[1]*0.3),
                centered=True)
            render(
                fonts[2],
                text=str(current_phone['phone']),
                color="black",
                where=(window_size[0]*0.3, window_size[1]*0.4),
                centered=True)
            render(
                fonts[2],
                text=str(current_phone['phone']),
                color="black",
                where=(window_size[0]*0.82, window_size[1]*0.29),
                centered=True)    
            render(
                fonts[2],
                text=str(emote_face),
                color="black",
                where=(window_size[0]*0.3, window_size[1]*0.5),
                centered=True)
            render(
                fonts[2],
                text=str(emote_hands),
                color="black",
                where=(window_size[0]*0.3, window_size[1]*0.6),
                centered=True)
        except NameError:
            pass


def display_key_points():
    
    pygame.draw.circle(screen, WHITE, eyes_position, 5)
    pygame.draw.circle(screen, WHITE, mouth_position, 5)


def display_body():
    current_body_png = down_hands_png
    current_body_position = (window_size[0]*0.70, window_size[1]*0.15)
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
    screen.blit(current_eyes_png, (x+10, y+10))
    screen.blit(current_brows_png, (x, y))


def update_screen():
    """where everything happens"""
    quit_button()
    clear_screen()
    display_fps()
    display_texts()
    display_clock()
    display_key_points()
    display_body()
    display_brows_and_eyes(eyes_position[0], eyes_position[1])
    refresh_screen()
    #todo delete ->
    x3, y3 = pygame.mouse.get_pos()
    print(x3, y3)

# =================
# =================
# =================


dir_name = 'test_custom_types'
init_pygame()
init_time()
init_audio()
fonts = init_fonts([25, 30, 60])
WHITE = (255, 255, 255)
eyes_position = (window_size[0]*0.747, window_size[1]*0.25)
head_position = (window_size[0]*0.70, window_size[1]*0.15)
head_position_up = (window_size[0]*0.68, window_size[1]*0.15)
mouth_position = (window_size[0] * 0.76, window_size[1] * 0.31)
emote_face_tag = '<face:'
emote_hands_tag = '<hands:'

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


with open(f'test_directory/{dir_name}/transcript.txt', 'r') as f:
    transcript_and_emotes = str(f.read()).split()


if emote_face_tag in transcript_and_emotes[current_word_pos]:
    emote_tag = transcript_and_emotes.pop(current_word_pos)
    emote_face = emote_tag[6:-1]
if emote_hands_tag in transcript_and_emotes[current_word_pos]:
    emote_tag = transcript_and_emotes.pop(current_word_pos)
    emote_hands = emote_tag[7:-1]


cycle = True
while cycle:
    what_should_i_show()
    update_screen()
pygame.quit()
