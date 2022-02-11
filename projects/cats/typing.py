"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime

import string


def lines_from_file(path):
    """Return a list of strings, one for each line in a file."""
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


punctuation_remover = str.maketrans('', '', string.punctuation)


def remove_punctuation(s):
    """Return a string with the same contents as s, but with punctuation removed.

    >>> remove_punctuation("It's a lovely day, don't you think?")
    'Its a lovely day dont you think'
    """
    return s.strip().translate(punctuation_remover)


def lower(s):
    """Return a lowercased version of s."""
    return s.lower()


def split(s):
    """Return a list of words contained in s, which are sequences of characters
    separated by whitespace (spaces, tabs, etc.).

    >>> split("It's a lovely day, don't you think?")
    ["It's", 'a', 'lovely', 'day,', "don't", 'you', 'think?']
    """
    return s.split()

###########
# Phase 1 #
###########

def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    list = []
    for i in range(0, len(paragraphs)):
        if select(paragraphs[i]):
            list.append(paragraphs[i])
    if k < len(list):
        return list[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    return lambda x: set([lower(i) for i in split(remove_punctuation(x))]) & set(topic) != set()
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0group
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if len(typed_words) == 0:
        return 0.0
    elif len(reference_words) == 0:
        return 0.0
    else:
        accurate_num = 0
        for i in range(0, min(len(typed_words), len(reference_words))):
            if typed_words[i] == reference_words[i]:
                accurate_num += 1
        return accurate_num / len(typed_words) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    letters_count = len(typed)
    if letters_count == 0:
        return 0.0
    else:
        return letters_count / elapsed * 12
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    list_diff = []
    list_words = []
    for i in range(0, len(valid_words)):
        list_diff.append(diff_function(user_word, valid_words[i], limit))
    for k in range(0, len(valid_words)):
        if diff_function(user_word, valid_words[k], limit) == min(tuple(list_diff)):
            list_words.append(valid_words[k])
    if min(tuple(list_diff)) > limit:
        return user_word
    elif user_word in valid_words:
        return user_word
    else:
        return list_words[0]
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    list_start = list(start)
    list_goal = list(goal)
    def count_changes(lst_start, lst_goal, total):
        if lst_start == [] or lst_goal == []:
            return total + abs(len(lst_start) - len(lst_goal))
        else:
            if lst_start[0] != lst_goal[0]:
                total += 1
                if total > limit:
                    return total
                return count_changes(lst_start[1: ], lst_goal[1: ], total)
            else:
                return count_changes(lst_start[1: ], lst_goal[1: ], total)
    return count_changes(list_start, list_goal, 0)
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # BEGIN
    list_start = list(start)
    list_goal = list(goal)
    start_length = len(list_start) + 1
    goal_length = len(list_goal) + 1
    edit_matrix = [[0 for i in range(goal_length)] for j in range(start_length)]
    edit_matrix[0] = [i for i in range(goal_length)]
    for k in range(0, start_length):
        edit_matrix[k][0] = k
    if len(list_start) == 0 or len(list_goal) == 0: # Fill in the condition
        return len(list_start) + len(list_goal)
    else:
        for i in range(1, start_length):
            for j in range(1, goal_length):
                add = edit_matrix[i][j - 1] + 1
                remove = edit_matrix[i - 1][j] + 1
                if list_start[i - 1] == list_goal[j - 1]:
                    substitute = edit_matrix[i - 1][j - 1]
                else:
                    substitute = edit_matrix[i - 1][j - 1] + 1
                edit_matrix[i][j] = min(add, remove, substitute)
        return edit_matrix[start_length-1][goal_length-1]
    # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    list_typed = list(typed)
    list_prompt = list(prompt)
    ratio = 0
    accurate_num = 0
    len_typed = len(typed)
    len_prompt = len(prompt)
    list_k = []
    if len_typed == 0:
        ratio = 0.0
    else:
        def accurate_typed(list_typed):
            for k in range(0, len_typed):
                if list_typed[k] != list_prompt[k]:
                    return k
            return len_typed
        accurate_num = accurate_typed(list_typed)
        ratio = accurate_num / len_prompt
    dic_progress = {'ID': id, 'Progress': ratio}
    print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['ratio'])
    print_progress({'id': id, 'ratio': ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    player_nums = len(word_times)
    words_nums = len(word_times[0])
    new_word_times = [[[None, 0] for j in range(0, words_nums)] for i in range(0, player_nums)]
    for i in range(0, player_nums):
        for j in range(0, words_nums):
            new_word_times[i][j][0] = word(word_times[i][j])
    for i in range(0, player_nums):
        for j in range(1, words_nums):
            new_word_times[i][j][1] = elapsed_time(word_times[i][j]) - elapsed_time(word_times[i][j - 1])
    for i in range(0, player_nums):
        new_word_times[i] = new_word_times[i][1: ]
    word_output = [[] for i in range(0, player_nums)]
    for j in range(0, words_nums - 1):
        list_wordtime = []
        for i in range(0, player_nums):
            list_wordtime.append(new_word_times[i][j][1])
        min_time = min(list_wordtime)
        for i in range(0, player_nums):
            if abs(new_word_times[i][j][1] - min_time) < margin:
                word_output[i].append(new_word_times[i][j][0])
    return word_output
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)