"""This module acts as a controller for the system.

Contains:

    * :func:`main`
    * :func:`update_status`
"""

import PySimpleGUI as psg


# set theme
psg.theme('DarkBrown1')


MAINL_IN        = [[psg.Frame('Section Management', [
                      [psg.Button('New Section', s=(30))],
                      [psg.Button('Edit Sections', s=(30))],
                      [psg.Button('Edit Profile', s=(30))]
                  ])]]
"""GUI elements for section file management."""
MAINL_OUT       = [[psg.Frame('Make A Cover Letter', [
                      [psg.Button('Assembler', s=(30))],
                      [psg.Button('Quick Assembler', s=(30))]
                  ])]]
"""GUI elements for starting generation of a pdf."""
MAINL_STATUS    = [[psg.Text(s=(30))],[psg.Pane([psg.Column([
                      [psg.Text('', k='-templates', s=(31))],
                      [psg.Text('', k='-letters', s=(31))],
                      [psg.StatusBar('github.com/gavboi', justification='c', s=(31))]
                  ])])]]
"""GUI elements for showing the status of files."""


def update_status():
    """Sets the output element in the GUI to reflect latest values.
    """

    # count templates
    # count pdfs

    raise NotImplementedError()


def new_section_menu():
    """Pops open a window for creating a new section.
    """

    raise NotImplementedError()


def edit_section_menu():
    """Pops open a window for editing an existing section.
    """

    raise NotImplementedError()


def edit_profile_menu():
    """Pops open a window for editing personal information.
    """

    raise NotImplementedError()


def new_pdf_menu():
    """Pops open a window for creating a new cover letter.
    """

    raise NotImplementedError()


def quick_pdf():
    """Randomly creates a cover letter from the available sections,
    while following formatting rules. Pops open a window alerting the
    user that this was done.
    """

    raise NotImplementedError()
    

def main():
    layout = MAINL_IN + MAINL_OUT + MAINL_STATUS
    win = psg.Window('QCL - Main Menu', layout)
    #update_status()
    while True:
        event, values = win.read()
        if event == psg.WIN_CLOSED:
            break
        if event == 'New Section':
            new_section_menu()
        elif event == 'Edit Sections':
            edit_section_menu()
        elif event == 'Edit Profile':
            edit_profile_menu()
        elif event == 'Assembler':
            new_pdf_menu()
        elif event == 'Quick Assembler':
            quick_pdf()
    win.close()

main()
