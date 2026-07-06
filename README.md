# Summer Circuits

*A lightweight Visual Novel engine built with Python and Pygame.*

---

## About

Summer Circuits is a short, story-driven visual novel created as a personal anniversary gift.

Unlike full visual novel engines (Ren'Py, Novelty, etc.), this project is intentionally lightweight and only contains the features needed for a linear 15–30 minute experience.

Development Philosophy:

- Story first
- Simplicity over complexity
- Functions over classes
- One Python file
- Easy to modify
- Beginner friendly

---

# Project Structure

```
SummerCircuits/
│
├── main.py
├── dialogue.py
│
├── assets/
│   ├── backgrounds/
│   ├── portraits/
│   ├── music/
│   └── ui/
│
└── README.md
```

---

# Engine Architecture

The project is separated into two major files.

## main.py

Responsible for:

- Window creation
- Rendering
- Asset loading
- Scene processing
- Music
- Portraits
- Backgrounds
- Dialogue rendering
- Game loop

Think of this as the **engine**.

---

## dialogue.py

Contains the story only.

No rendering code.

No pygame.

Only dictionaries describing the story.

Think of this as the **script**.

---

# Dialogue Format

Every chapter is simply a Python list.

Example:

```python
chapter0 = [

    {
        "type":"background",
        "name":"graduation"
    },

    {
        "type":"portrait",
        "left":"isaac",
        "right":None
    },

    {
        "type":"title",
        "title":"Chapter 0",
        "subtitle":"The Prologue"
    },

    {
        "type":"dialogue",
        "speaker":"Isaac",
        "text":"More than ready..."
    }

]
```

---

# Supported Commands

## Background

Changes the current background.

```python
{
    "type":"background",
    "name":"training_room"
}
```

Looks for

```
assets/backgrounds/training_room.png
```

---

## Portrait

Changes portraits.

```python
{
    "type":"portrait",
    "left":"isaac",
    "right":"cynthia"
}
```

Looks for

```
assets/portraits/isaac.png

assets/portraits/cynthia.png
```

---

## Music

Changes background music.

```python
{
    "type":"music",
    "name":"training"
}
```

Looks for

```
assets/music/training.ogg
```

---

## Title Card

Displays a chapter title.

```python
{
    "type":"title",
    "title":"Chapter 3",
    "subtitle":"Drafts"
}
```

---

## Dialogue

Normal dialogue.

```python
{
    "type":"dialogue",
    "speaker":"Isaac",
    "text":"Hello."
}
```

---

## Thoughts

Thoughts are still dialogue.

Simply add

```python
"thought":True
```

Example

```python
{
    "type":"dialogue",
    "speaker":"Isaac",
    "thought":True,
    "text":"This is awkward..."
}
```

The engine may later render thoughts differently.

---

# Asset Naming

Keep filenames lowercase.

Good

```
isaac.png

training_room.png

mall.ogg
```

Avoid

```
Isaac Portrait FINAL FINAL.png
```

Consistency is more important than style.

---

# Current Scope

Version 1.0 intentionally supports only:

- Linear story
- One portrait per character
- One background per scene
- Background music
- Title cards
- Dialogue
- Thoughts
- Fade transitions

No save/load.

No inventory.

No combat.

No animation system.

---

# Controls

SPACE

Advance dialogue

ENTER

Advance dialogue

ESC

(Reserved)

---

# Future Features

The engine architecture already leaves room for:

- Choices
- Multiple endings
- CG illustrations
- Sound effects
- Screen shake
- Credits
- Save system

These are intentionally postponed until after Version 1.0.

---

# Development Workflow

When writing a new chapter:

1. Create the chapter in `dialogue.py`.

2. Add any required backgrounds.

3. Add portraits if needed.

4. Test the chapter.

5. Repeat.

Avoid modifying `main.py` unless fixing a bug or adding a new engine feature.

---

# Design Philosophy

The engine should remain stable.

The story should continue evolving.

Most future work should happen inside:

- `dialogue.py`
- `assets/`

instead of the engine itself.

---

# Credits

Story

- Ice Lifram

Programming

- Ice Lifram

Story Co-Writer

- ❤️

Built with

- Python
- Pygame

