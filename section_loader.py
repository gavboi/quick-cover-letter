"""This module deals with managing pre-made sections of text for use in
the cover letter.

Contains:

    * :class:`Section`
    * :func:`make_new_section`
    * :func:`verify_sections`
    * :func:`load_section`
    * :func:`load_all_sections`
"""

from os.path import join, isfile
from os import listdir

SECTION_TYPE = {0: "Intro",
                1: "Body",
                2: "Conclusion"}
"""Dictionary for ID to String section type conversions."""
                
FILE_EXT = '.py'
"""File type of section template files."""
TEMPLATE_CONTENT = {'# Replace values as needed for the section\n'
                    + 'SECTION_ID = 0 # id for location in text that the '
                    + 'section is relevant to\n'
                    + 'STRONG_KEYWORDS = [''] # keywords most relevant '
                    + 'to section content\n'
                    + 'WEAK_KEYWORDS = [''] # keywords somewhat relevant '
                    + 'to section content\n'
                    + 'TEXT_CONTENT = '' # text written to cover letter\n'}
"""Contents of section template file."""


def make_new_section(name):
    """Creates a template file for a user to fill out that can be then
    used as a section in a cover letter.

    If a template file of the same name already exists, it will add a
    counter to the end until it becomes a new file (i.e. if `name`
    is 'proj' and both 'proj' and 'proj2' already exist, 'proj3'
    will be created.

    :param name: the name given as a descriptor of the section's
        content
    :type name: str
    """

    # ensure unique name
    counter = 1
    file_name = name
    while isfile(join('sections', file_name + FILE_EXT)):
        counter += 1
        file_name = name + counter
    # create file
    with open(join('sections', file_name + FILE_EXT),
              'w', encoding='utf-8') as file:
        file.write(TEMPLATE_CONTENT)


def verify_sections(amount=1):
    """Ensures all sections have at least some amount of entries.
    """
    
    # count 0s, 1s, 2s
    # check counts >= amount
    raise NotImplementedError()
        


def load_section(name, warn=True):
    """Checks that a section template file has been filled out
    sufficiently and converts it to an object.

    :param name: the name of the file to load
    :type name: str
    :param warn: if warning messages should be shown
    :type warn: bool
    :return: object containing the section values
    :rtype: Section
    """

    raise NotImplementedError()


def load_all_sections(warn=True):
    """Checks that all section template files have been filled out
    sufficiently and converts them to objects.

    :param warn: if warning messages should be shown
    :type warn: bool
    :return: list of `Section` objects corresponding to all the files
    :rtype: list
    """

    sections = []
    for item in listdir('sections'):
        name = join('sections', item)
        if isfile(name) and name.endswith(FILE_EXT):
            sect = load_section(name, warn=warn)
            if isinstance(sect, Section):
                sections.append(sect)
    return sections


class Section():
    """Used to create runtime copies of the section template files.

    :param name: the name given as a descriptor of the section's
        content
    :type name: str
    """

    def __init__(self, name):
        """The constructor method.
        """

        raise NotImplementedError()
