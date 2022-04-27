"""This module acts as the translator between the loader and compiler
modules.

Contains:

    * :func:`dir_setup`
    * :func:`file_setup`
"""

from os.path import join, isdir
from os import mkdir


def dir_setup():
    """Makes folders for files.
    """

    folders = ['sections', join('sections', 'tex'),
            'subjects', join('subjects', 'tex')]
    for folder in folders:
        if not isdir(folder):
            mkdir(folder)


def file_setup(warn=True):
    """Copies filled templates into new files of a different format for
    use in generating a pdf.

    Note that original files must still remain for proper selection of
    generated files for pdf.

    :param warn: if warning messages should be shown
    :type warn: bool
    """

    raise NotImplementedError()
