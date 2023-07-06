#!/usr/bin/python3
"""A module for working with lockboxes."""


def canUnlockAll(boxes):
    """This function will take a list of boxes and the content
       of a list will unlock other boxes.
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
