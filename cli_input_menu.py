"""
Implement a method of getting a choice from a user using a simple menu.

Uses the entire screen for the menu.  Allows user to enter either a numeric
choice or to provide enough input to identify the desired choice.

Usage:  choice = get_choice(choices, header=None, prompt=None)

where  choices  is a list of choice strings
       header   the top header line for the menu
       prompt   the prompt string that asks for a choice

The returned value is the complete string from 'choices' that the user chose.
"""

import os
import sys


WIN32 = sys.platform == 'win32'


def clear():
    """Clear the screen.

    Should work on multiple operating systems.
    """

    if WIN32:
        os.system('cls')
    else:
        os.system('clear')

def bright(msg):
    """Print some text in 'bright'.

    This is potentially not portable.
    """

    print(f'\033[1m{msg}\033[0m')

def find_prefix_match(prefix, choices, start_index = 0):
    """Return index of element in 'choices' that starts with 'prefix'.

    prefix       the prefix string to search for
    choices      list of choces strings
    start_index  the index to start searching 'choices' at

    Returns an index into 'choices' of unique find.
    Returns 'None' if no match found.
    """

    for (i, c) in enumerate(choices[start_index:]):
        if c.startswith(prefix):
            return i + start_index
    return None

def get_choice(choices, header=None, prompt=None):
    """Get a user choice.

    choices  a list of choice strings
    header   the header string
    prompt   the prompt string

    Returns the complete string from 'choices' that the user chose.
    """

    # check prompt supplied
    if prompt is None:
        prompt = 'Enter choice: '

    # make sure we have all-lowercase choice strings
    new_choices = [c.lower() for c in choices]

    # present menu
    error = ''      # holds error message (if any)
    while True:
        # present the menu
        clear()
        if header:
            bright(header)
        print()
        for (i, c) in enumerate(choices):
            print('%2d. %s' % (i + 1, c))
        print()
        if error:
            print(error)
            print()
            error = ''
        ans = input(prompt)
        if not ans:
            # no input, just represent the menu
            continue

        # check response
        ans_lower = ans.lower()
        try:
            num_ans = int(ans_lower)
        except ValueError:
            # not numeric, look for choice starting with 'ans_lower'
            ndx = find_prefix_match(ans_lower, new_choices)
            if ndx is None:
                # error, NO match
                error = "Sorry, '%s' doesn't match a choice." % ans
                continue
            else:
                if find_prefix_match(ans_lower, new_choices, ndx+1):
                    error = "Sorry, '%s' matches more than one choice." % ans
                    continue
                return choices[ndx]
        else:       # no exception
            # if we get here, 'num_ans' is numeric choice
            if 0 < num_ans <= len(new_choices):
                return choices[num_ans - 1]
            error = "Sorry, numeric response '%s' was out of range." % ans


if __name__ == '__main__':
    choices = ['Alpha', 'beta', 'gamma', 'Delta', 'epsilon', 'alphABET', 'dog', 'grouse']
#    choice = get_choice(choices, 'A longer header string', 'Enter choice: ')
    choice = get_choice(choices)
    print('choice=%s' % choice)
