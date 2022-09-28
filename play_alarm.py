"""
--- Created by : Netra Prasad Neupane
--- Created on : 9/28/22
"""

import playsound


def play_sound_alarm(path):
    """
    Function to play the sound
    :param path: file path to the mp3/wav alarm file
    :return:
    """
    # play the alarm sound
    playsound.playsound(path)
