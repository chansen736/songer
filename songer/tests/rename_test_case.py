# Harness imports
import unittest

from rename_fixture import RenameFixture
from songer_fixture import SongerFixture

# Module-under-test imports
import songer

class RenameTestCase(unittest.TestCase, SongerFixture, RenameFixture):
    """
    Test case for renaming files.
    """
    
    def test_IMPLEMENT_ME(self):
        # XXX: This is a stub for when i start writing actual tests for this module
        r = self.doMain("abc")
        self.assertEqual( self.ERROR, r.getReturnCode() )

    
    