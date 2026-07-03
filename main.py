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

font_name = pygame.font.SysFont("terminus", 28)
font_text = pygame.font.SysFont("terminus", 32)
font_title = pygame.font.SysFont("arial", 56, bold=True)
font_subtitle = pygame.font.SysFont("arial", 36)
font_hint = pygame.font.SysFont("arial", 24)

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
#     "type":"..."
#     "speaker": "...",
#     "text": "...",
#     "background":"..."
# }

scene_intro = [

    {
        "type": "title",
        "title": "Chapter 1",
        "subtitle": "The Newcomer"
    },

    {
        "type":"dialogue",
        "speaker":"Narrator",
        "text":"It is the summer of July, 2025."
    },

    {
        "type":"dialogue",
        "speaker":"Narrator",
        "text":"Ice, an incoming college student, went on to his hometown after years of high school in the city."

    },

    {
        "type":"dialogue",
        "speaker":"Narrator",
        "text":"Lorem ipsum (lmao)"
    },


    {
        "type":"dialogue",
        "speaker":"Isaac",
        "text":"TODO: First line."
    },

    {
        "type":"dialogue",
        "speaker":"Isaac",
        "text":"TODO: First line"
    },

]

scene_practical = [

    {
        "type":"title",
        "title":"Chapter 2",
        "subtitle":"First Interaction"
    },
    {
        "type":"dialogue",
        "speaker":"Cynthia",
        "text":"hello!"
    }
]

SCENES = [
    scene_intro,
    scene_practical
]

# =========================================================
# GAME STATE
# =========================================================

current_scene_index = 0
current_scene = SCENES[current_scene_index]

dialogue_index = 0

running = True


# =========================================================
# HELPER FUNCTIONS
# =========================================================

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

def draw_title_card(current):
    """
    Draw a simple chapter title card.
    """

    # Fill the screen with black
    screen.fill(BLACK)

    # Get title information
    title = current["title"]
    subtitle = current["subtitle"]

    # Render text
    title_surface = font_title.render(title, True, WHITE)
    subtitle_surface = font_subtitle.render(subtitle, True, WHITE)
    hint_surface = font_hint.render("Press SPACE to continue", True, (180, 180, 180))

    # Center the text
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    subtitle_rect = subtitle_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    hint_rect = hint_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    # Draw everything
    screen.blit(title_surface, title_rect)
    screen.blit(subtitle_surface, subtitle_rect)
    screen.blit(hint_surface, hint_rect)

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
    global current_scene
    global current_scene_index

    if dialogue_index < len(current_scene)-1:

        dialogue_index += 1

    else:

        current_scene_index += 1
        current_scene = SCENES[current_scene_index]
        dialogue_index = 0


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

    screen.blit(background, (0,0) )

    current = current_scene[dialogue_index]

    if current["type"] == "title":
        draw_title_card(current)

    elif current["type"] == "dialogue":
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
