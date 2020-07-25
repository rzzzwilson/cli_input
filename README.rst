cli_input - Getting User Input
==============================

Often our code wants to get textual input from a user.  Sure, GUIs are nice, but
they take a lot of work to set up.  Often we just want a simple script that
prompts the user for input.  Maybe even something as simple as selecting an
option from a menu.

The code here is an attempt to make this process less painful for the end-user.

Use Case
--------

Often text systems ask users for input with this sort of prompt::

    Enter the smoothing function (None, Adaptive or Exponential):

It's a pain for the user to type in 'Adaptive', for example, and we usually allow
the user to type the first character with case being ignored.  But what if the
choices are *many* and the first letter isn't enough?  It would be nice if we let
the user enter as many characters **as necessary** to make the selection.  So a
menu prompt might look like this::

    Smoothing

    1. Adaptive smoothing
    2. Butterworth filter
    3. Kalman filter
    4. Kernel smoother
    5. Kolmogorov–Zurbenko filter
    6. Laplacian smoothing
    7. Local regression
    8. Low-pass filter

    Select the smoothing algorithm to use:

Note that a single letter is not enough: 'k' could be one of three choices.  We
want a system that would allow the user to enter a *number* or a string that
indicates the choice made.  If the choice is invalid the code should ask again.

Design
------

To implement something as complicated as the above example, we need to first define
some terminology.

The **header** is the line at the top of the menu ('Smoothing' in the above case).

The **choices** are the 1 to 8 choice strings - 'Adaptive smoothing', for example.
Note that the numeric values are added by the code.

The line asking for the user to enter a choice ('Select the smoothing algorithm
to use:') is called the **prompt**.

So the code that presents a menu like that shown above would look like::

    choice = get_choice(choices=['Adaptive smoothing', 'Butterworth filter',
                                 'Kalman filter', 'Kernel smoother',
                                 'Kolmogorov–Zurbenko filter',
                                 'Laplacian smoothing', 'Local regression',
                                 'Low-pass filter'],
                        header='Smoothing',
                        prompt='Select the smoothing algorithm to use: ')


where **choices** is a list of strings.  The **header** and **prompt** parameters
may be omitted.

When executed, the above code allows the user to enter any digit in the range
*[1, 8]* or a string that uniquely selects one menu item, such as "a", "Ka" or
"low".

Files here
----------

The python files here are all self-contained and can be imported to use the code
or you can execute each file to get a simple demonstration.
