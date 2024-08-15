#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    This function takes a list of lists as an input, where each sublist represents a box and the integers in the sublist represent the keys to other boxes. The function checks if it's possible to open all boxes starting from the first box (box 0).

    Parameters:
    boxes (List[List[int]]): A list of lists where each sublist represents a box and the integers in the sublist represent the keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.

    Example:
    >>> canUnlockAll([[1], [2], [3], []])
    True
    >>> canUnlockAll([[1, 3], [3, 0, 1], [2], [0]])
    False

    Note:
    The function assumes that the keys are zero-indexed and that the first box (box 0) is initially open.
    """

    if not boxes:
        return False

    keys = [0 for i in range(len(boxes))]
    keys[0] = 1
    for i in range(len(boxes)):
        for key in boxes[i]:
            if key < len(boxes) and key != i:
                keys[key] = 1
    if 0 in keys:
        return False
    return True
