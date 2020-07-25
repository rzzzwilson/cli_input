"""
Implement a method of getting a choice from a user.
"""

import os
import sys


WIN32 = sys.platform == 'win32'


def clear():
    """Clear the screen."""

    if WIN32:
        os.system('cls')
    else:
        os.system('clear')

def find_prefix_match(prefix, choices, start_index=0):
    """Return index of element in 'choices' that starts with 'prefix'.

    prefix       the prefix string to search for
    choices      list of choces strings
    start_index  the index to start searching 'choices' at

    Returns an index into 'choices' of unique find.  Returns None
    if no or more than one match found.
    """

    for (i, c) in enumerate(choices[start_index:]):
        if c.startswith(prefix):
            return i + start_index
    return None

def get_choice(choices, prompt=None):
    """Get a user choice.

    choices  a list of choice strings
    prompt   the prompt string
    """

    # check prompt supplied
    if prompt is None:
        prompt = 'Enter choice: '

    # make sure we have all-lowercase choice strings
    new_choices = [c.lower() for c in choices]

    # create the complete prompt
    prompt = '[%s]  %s' % (', '.join(choices), prompt)

    # present menu
    error = ''      # holds error message (if any)
    while True:
        # present the prompt
        clear()
        if error:
            print(error + '\n')
            error = ''
        ans = input(prompt)
        if not ans:
            continue    # ignore empty inputs

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
            if not 0 < num_ans <= len(new_choices):
                error = "Sorry, numeric response '%s' was out of range." % ans
                continue
            return choices[num_ans - 1]


if __name__ == '__main__':
    choices = ['Alpha', 'beta', 'gamma', 'Delta', 'epsilon', 'beat', 'deal']
    choice = get_choice(choices, 'Pick one: ')
    print('choice=%s' % choice)
