#!/bin/env python3

"""
Implement a method of getting a choice from a user using a simpe menu.
"""

def clear():
    """Clear the screen."""

    print('\n'*60)
#    print("\033[2J")
#    print('\033[50;0H')

def bright(msg):
    """Print some text in 'bright'."""

#    print("\033[1;37;40m%s\033[0;37;40m" % msg)
    print(msg)

def find_prefix_match(prefix, choices, start_index = 0):
    """Return index of element in 'choices' that starts with 'prefix'.

    prefix       the prefix string to search for
    choices      list of choces strings
    start_index  the index to start searching 'choices' at

    Returns an index into 'choices' of unique find.  Returns None if no match found.
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
    """

    # make sure we have all-lowercase choice strings
    new_choices = [c.lower() for c in choices]

    # present menu
    error = None
    while True:
        # present the menu
        clear()
        if error:
            print(error + '\n')
            error = None
        bright(header)
        print()
        for (i, c) in enumerate(choices):
            print('%2d. %s' % (i + 1, c))
        print()
        ans = input(prompt)

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
    choice = get_choice(['Alpha', 'beta', 'gamma', 'Delta', 'epsilon', 'alphABET', 'dog', 'grouse'],
                        'A longer header string', 'Enter choice: ')
    print('choice=%s' % choice)
