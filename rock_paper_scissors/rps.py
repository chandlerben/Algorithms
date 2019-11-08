#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    final_outcomes = []
    options_in_a_play = ['rock', 'paper', 'scissors']

    def building_one_of_the_lists(rounds_left, play_result):
        if rounds_left == 0:
            final_outcomes.append(play_result)
            return

        for option in options_in_a_play:
            new_play_result = play_result+[option]
            building_one_of_the_lists(rounds_left-1, new_play_result)

    building_one_of_the_lists(n, [])
    return final_outcomes


rock_paper_scissors(2)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
