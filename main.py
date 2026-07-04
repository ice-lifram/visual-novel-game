"""
===========================================================
Summer Circuits
-----------------------------------------------------------
A short visual novel created with Python + Pygame.

Version:
    v0.2

Author:
    Ice Lifram

Development Philosophy:
    - Single Python file
    - Functions over classes
    - Story first
    - Easy to modify
===========================================================
"""

# =========================================================
# IMPORTS
# =========================================================

import pygame
import sys
from pathlib import Path

import dialogue


# =========================================================
# INITIALIZATION
# =========================================================

pygame.init()

# Uncomment once music is added
# pygame.mixer.init()


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

PATHS = {

    "backgrounds": ASSETS / "backgrounds",

    "portraits": ASSETS / "portraits",

    "music": ASSETS / "music",

    "ui": ASSETS / "ui"

}


# =========================================================
# ASSET CACHE
# =========================================================

background_cache = {}

portrait_cache = {}


# =========================================================
# FONTS
# =========================================================

font_name = pygame.font.SysFont("terminus", 28)

font_text = pygame.font.SysFont("terminus", 32)

font_title = pygame.font.SysFont("arial", 56, bold=True)

font_subtitle = pygame.font.SysFont("arial", 36)

font_hint = pygame.font.SysFont("arial", 24)


# =========================================================
# PLACEHOLDER BACKGROUND
# =========================================================

placeholder_bg = pygame.Surface((WIDTH, HEIGHT))
placeholder_bg.fill((60,70,90))


# =========================================================
# SCENES
# =========================================================

SCENES = [

    dialogue.chapter0,

    dialogue.chapter1

]


# =========================================================
# GAME STATE
# =========================================================

state = {

    "background": placeholder_bg,

    "left_portrait": None,

    "right_portrait": None,

    "music": None

}


# =========================================================
# STORY STATE
# =========================================================

current_scene_index = 0

current_scene = SCENES[current_scene_index]

dialogue_index = 0

running = True


# =========================================================
# PORTRAIT POSITIONS
# =========================================================

LEFT_POS = (40,130)

RIGHT_POS = (900,130)


# =========================================================
# ASSET HELPERS
# =========================================================

def load_background(name):
    """
    Load a background only once.
    """

    if name in background_cache:
        return background_cache[name]

    path = PATHS["backgrounds"] / f"{name}.png"

    try:

        image = pygame.image.load(path).convert()

    except:

        image = placeholder_bg

    background_cache[name] = image

    return image


def load_portrait(name):
    """
    Load a portrait only once.
    """

    if name is None:
        return None

    if name in portrait_cache:
        return portrait_cache[name]

    path = PATHS["portraits"] / f"{name}.png"

    try:

        image = pygame.image.load(path).convert_alpha()

    except:

        image = None

    portrait_cache[name] = image

    return image


def play_music(name):
    """
    Play background music.

    Disabled until music is added.
    """

    if state["music"] == name:
        return

    state["music"] = name

    # pygame.mixer.music.load(
    #     PATHS["music"] / f"{name}.ogg"
    # )
    #
    # pygame.mixer.music.play(-1)


# =========================================================
# SCENE COMMANDS
# =========================================================

def set_background(name):

    state["background"] = load_background(name)


def set_portraits(left=None, right=None):

    state["left_portrait"] = load_portrait(left)

    state["right_portrait"] = load_portrait(right)