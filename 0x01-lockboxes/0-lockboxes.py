#!/usr/bin/python3
"""
Module presents solution to
unlock a number of locked boxes.
"""


def canUnlockAll(boxes):
    """
    Method determines if n number of
    locked boxes can be opened.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
