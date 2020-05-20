import os
import sys


def add_sources_to_pythonpath():
    # Expect the sources to be rooted at the parent
    # of the test directory, which is in turn
    # the directory that must contain this conftest.py
    sources_directory = os.path.abspath(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )
    sys.path.append(sources_directory)


add_sources_to_pythonpath()
