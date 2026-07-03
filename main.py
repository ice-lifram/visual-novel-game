"""
===========================================================
Summer Circuits
-----------------------------------------------------------
A short visual novel created with Python + Pygame.

Version:
    v0.1 Skeleton

Author:
    Ice Lifram

Description:
    This file contains the entire game for Version 1.0.

Development Philosophy:
    - Single Python file
    - Functions over classes
    - Simple and readable
    - Story first, visuals second
===========================================================
"""

# =========================================================
# IMPORTS
# =========================================================

import pygame
import sys
from pathlib import Path

# TODO:
# Import anything else ONLY when needed.


# =========================================================
# INITIALIZATION
# =========================================================

pygame.init()

# TODO:
# Initialize the mixer later when music is added.


# =========================================================
# GAME SETTINGS
# =========================================================

WIDTH = 1280
HEIGHT = 720

FPS = 60

TITLE = "Summer Circuits"


# =========================================================
# COLORS
# =========================================================

WHITE = (255,255,255)
BLACK = (0,0,0)

GRAY = (40,40,40)

DIALOGUE_BOX = (20,20,20)


# =========================================================
# WINDOW
# =========================================================

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


# =========================================================
# ASSET PATHS
# =========================================================

ASSETS = Path("assets")

BACKGROUND_FOLDER = ASSETS / "backgrounds"

PORTRAIT_FOLDER = ASSETS / "portraits"

MUSIC_FOLDER = ASSETS / "music"

PHOTO_FOLDER = ASSETS / "photos"


# =========================================================
# FONTS
# =========================================================

# TODO:
# Replace with custom font later.

font_name = pygame.font.SysFont("arial", 28)

font_text = pygame.font.SysFont("arial", 32)


# =========================================================
# PLACEHOLDER BACKGROUND
# =========================================================

# TODO:
# Load images later.

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((60,70,90))


# =========================================================
# DIALOGUE DATA
# =========================================================

# Every dialogue entry should follow this format:
#
# {
#     "speaker": "...",
#     "text": "...",
# }

scene_intro = [

    {
        "speaker":"Narrator",
        "text":"TODO: Opening narration."
    },

    {
        "speaker":"Isaac",
        "text":"TODO: First line."
    },

]


# =========================================================
# GAME STATE
# =========================================================

current_scene = scene_intro

dialogue_index = 0

running = True


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def draw_background():
    """
    Draw current background.
    """

    screen.blit(background, (0,0))


def draw_dialogue_box():
    """
    Draw bottom dialogue box.
    """

    pygame.draw.rect(
        screen,
        DIALOGUE_BOX,
        (20,500,1240,190),
        border_radius=12
    )


def draw_dialogue():
    """
    Draw current dialogue.
    """

    line = current_scene[dialogue_index]

    speaker = line["speaker"]

    text = line["text"]

    speaker_surface = font_name.render(
        speaker,
        True,
        WHITE
    )

    text_surface = font_text.render(
        text,
        True,
        WHITE
    )

    screen.blit(speaker_surface, (50,520))
    screen.blit(text_surface, (50,570))


def next_dialogue():
    """
    Advance dialogue.
    """

    global dialogue_index

    if dialogue_index < len(current_scene)-1:

        dialogue_index += 1

    else:

        print("TODO: Next scene")


# =========================================================
# EVENT HANDLER
# =========================================================

def handle_events():

    global running

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                next_dialogue()


# =========================================================
# DRAW
# =========================================================

def draw():

    draw_background()

    draw_dialogue_box()

    draw_dialogue()

    pygame.display.flip()


# =========================================================
# MAIN LOOP
# =========================================================

while running:

    handle_events()

    draw()

    clock.tick(FPS)


# =========================================================
# CLEANUP
# =========================================================

pygame.quit()

sys.exit()
