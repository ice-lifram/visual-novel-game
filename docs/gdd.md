# Summer Circuits

### *Game Design Document (GDD)*

**Version:** 1.0
**Project Status:** Pre-Production

---

# 1. Overview

## Project Summary

**Summer Circuits** is a short narrative-driven visual novel developed using **Python** and **Pygame**. The game follows **Isaac**, an introverted student who joins a TESDA Electrical Installation and Maintenance training program during summer vacation.

Throughout the training, Isaac gradually becomes closer to his classmates—especially **Cynthia**, whose friendship slowly develops into something deeper.

The story explores themes of friendship, belonging, self-growth, and quiet romance. Rather than focusing on gameplay mechanics, the experience centers on meaningful dialogue, memorable moments, and player immersion.

The entire experience is designed to be completed in approximately **10–20 minutes**.

---

# 2. Vision

## Vision Statement

Create a heartfelt interactive story that feels like reading a short coming-of-age novel.

The player should finish the game feeling that they witnessed two ordinary people naturally become important to each other through everyday experiences.

The game is intended to be emotionally sincere rather than dramatic.

---

## Player Experience Goals

By the end of the game, the player should feel:

* Comfortable
* Nostalgic
* Relaxed
* Emotionally invested
* Happy after reaching the canon ending
* Curious enough to explore the alternate endings

---

# 3. Core Pillars

Every design decision should support at least one of these pillars.

## 1. Story First

The narrative is the primary feature of the game.

Gameplay exists only to support storytelling.

---

## 2. Simplicity

The project intentionally avoids unnecessary systems.

If a feature does not improve the story, it will not be implemented.

---

## 3. Authenticity

Characters should behave like ordinary people.

Dialogue should sound natural.

Conflicts should arise from realistic situations rather than forced drama.

---

## 4. Meaningful Choices

Choices should represent different approaches to life rather than "correct" or "incorrect" answers.

Alternate endings explore different futures rather than punish the player.

---

# 4. Story Summary

Isaac arrives at a TESDA Electrical Installation and Maintenance training program as a newcomer.

Initially quiet and reserved, he unexpectedly becomes class president and gradually forms friendships with his classmates.

Among them is Cynthia, who first approaches Isaac for technical help during laboratory activities.

As the training progresses, the class grows closer through shared experiences, including a trip to the mall where Isaac's photography hobby becomes more prominent.

After the outing, Cynthia messages Isaac to ask for the photographs he took.

Their conversations continue long after training hours, eventually developing into a close friendship.

Following TESDA, Cynthia struggles during college enrollment.

Isaac supports and encourages her until she successfully secures a slot in the BS Electronics Technology program.

Later, Cynthia visits Isaac's home so he can help her review electrical concepts.

During this quiet study session, Cynthia confesses her feelings.

The player's final decision determines how Isaac responds and which ending the story reaches.

---

# 5. Gameplay

Summer Circuits is a narrative-focused visual novel.

The gameplay loop is intentionally simple.

```
Scene

↓

Dialogue

↓

Player Choice (when available)

↓

Scene Transition
```

The objective is not to solve puzzles or complete challenges.

Instead, the player experiences the story through dialogue and occasional decisions.

---

## Gameplay Features

* Dialogue progression
* Scene transitions
* Character portraits
* Background illustrations
* Simple choices
* Multiple endings
* Credits
* Unlockable extras after the canon ending

---

# 6. Ending Structure

The game contains one **Canon Ending** and several **Alternate Endings**.

The story remains linear until the final confession scene.

Only the final decision changes the ending.

---

## Canon Ending

Isaac accepts Cynthia's confession.

The story concludes with hope for their future together.

After the credits, additional content becomes available.

---

## Alternate Endings

Examples include:

* Silence
* Behind the Lens
* Another Spring
* The Lone Circuit

These endings represent alternate futures rather than failures.

---

# 7. Characters

## Main Character

### Isaac

* Playable protagonist
* Introverted
* Observant
* Photography hobbyist
* Technically skilled
* Newly arrived in town
* TESDA Class President

---

## Supporting Characters

* Cynthia
* Jess
* Winston
* Ray
* Joe
* Rena

Each supporting character contributes to Isaac's personal growth throughout the story.

---

# 8. Themes

The story revolves around several recurring themes.

## Friendship

Learning to become part of a new community.

---

## Growth

Developing confidence through meaningful relationships.

---

## Connection

Both electrical circuits and human relationships require trust and understanding.

---

## Photography

Photography symbolizes preserving moments that might otherwise disappear with time.

Rather than expressing emotions directly, Isaac often communicates through the memories he chooses to capture.

---

# 9. Art Direction

The visual style should remain minimalistic.

Preferred style:

* 2D visual novel
* Soft colors
* Calm atmosphere
* Static backgrounds
* Character portraits
* Simple transitions

Animation is intentionally kept to a minimum.

---

# 10. Audio Direction

Audio should enhance the atmosphere without distracting from the dialogue.

Target assets include:

* Calm background music
* Emotional piano themes
* Camera shutter sound
* Phone notification sound
* UI button sounds

Voice acting is outside the project's scope.

---

# 11. Technical Scope

## Engine

Python

Pygame Community Edition (pygame-ce)

---

## Target Platform

Desktop (Windows)

---

## Estimated Playtime

10–20 minutes

---

## Estimated Development Time

Approximately one month.

---

# 12. Out of Scope

The following features are intentionally excluded.

* Save/Load system
* Inventory
* Achievements
* Complex branching narrative
* Mini-games
* Combat
* Character movement
* Animated sprites
* Voice acting
* Settings menu
* Localization
* Multiple chapters

These may be considered for future versions but are not required for Version 1.0.

---

# 13. Development Philosophy

Summer Circuits is designed to be a small but polished experience.

The project values:

* Simplicity over complexity.
* Completion over perfection.
* Emotional impact over technical sophistication.

Every system in the game exists to support the story.

If a feature does not make the narrative more meaningful, it should be removed.

---

# 14. Success Criteria

The project will be considered successful if it achieves the following goals:

* A complete, playable experience from beginning to end.
* Stable and maintainable Python code.
* A clear and emotionally satisfying story.
* A polished presentation suitable as an anniversary gift.
* A well-organized GitHub repository that demonstrates software engineering practices.

---

# 15. Final Statement

Summer Circuits is more than a programming exercise.

It is a short interactive story about ordinary people, quiet moments, and the connections that shape our lives.

Its purpose is not to impress through technical complexity, but to leave the player with a genuine emotional experience that lingers after the credits roll.

