#!/usr/bin/python3

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    # Track whether each box is unlocked
    unlocked[0] = True
    # The first box is already unlocked

    stack = [0]
    # Start with the first box
    while stack:
        current_box = stack.pop()
        # Get the current box from the stack
        for key in boxes[current_box]:
            # Check keys in the current box
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                # Mark the box as unlocked
                stack.append(key)
                # Add box to stack for further exploration

    return all(unlocked)
    # Return True if all boxes are unlocked, False otherwise
