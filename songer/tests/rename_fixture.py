# Harness imports
import unittest

# Module-under-test imports
import songer

class RenameFixture():
    """
    Fixture for testing file renames.
    """
    
    # XXX: This class should provider helpers for creating and cleaning up files, and verifying
    #      file names (the files can be empty, since we're just renaming them right now. Later on,
    #      when we modify mp3 meta data, we'll have to make real mp3s). The module tests won't need
    #      any hard-coded files, but the harness itself will to verify that its file operations
    #      are working correctly.