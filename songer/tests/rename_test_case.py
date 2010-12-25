# Harness imports
import songer_test_case
import unittest

# Module-under-test imports
import songer

class RenameTestCase(songer_test_case.SongerTestCase):
    """
    Test case for renaming files.
    """
    
    """ TEST CASES """
    
    def test_IMPLEMENT_ME(self):
        # XXX: This is a stub for when i start writing actual tests for this module
        self.assertEqual( self.ERROR, self.doMain("abc") )

    
    """ HELPER FUNCTIONS """
    
    # XXX: This class should provider helpers for creating and cleaning up files, and verifying
    #      file names (the files can be empty, since we're just renaming them right now. Later on,
    #      when we modify mp3 meta data, we'll have to make real mp3s). The module tests won't need
    #      any hard-coded files, but the harness itself will to verify that its file operations
    #      are working correctly.