# Harness imports
import unittest

from songer_fixture import SongerFixture
from songer_result  import SongerResult

# Module-under-test imports
import songer

class SongerTestCase(unittest.TestCase, SongerFixture):
    """
    Basic songer tests.
    """
    def test_nothing(self):
        self.assertEqual(0, 0, "Trivial, non-module test didn't assert 0==0")

        
    def test_error_codes_are_correct(self):
        # Verify the module error codes are what we expect
        self.assertEqual( 0, songer.RETURN_OK )
        self.assertEqual( 1, songer.RETURN_ERROR )
        
        # Verify the harness shorthand codes are set properly
        self.assertEqual( self.OK, songer.RETURN_OK )
        self.assertEqual( self.ERROR, songer.RETURN_ERROR )
    
    
    def test_help(self):
        r = SongerFixture.doMain("-h")
        self.assertEqual( self.OK, r.getReturnCode() )
    
    
    def test_version(self):
        # XXX000: add a test to verify the string
        correctVersionString = "%s %s.%s"%( songer.PRODUCT_NAME,
                                            songer.VERSION_MAJOR,
                                            songer.VERSION_MINOR )
        r = SongerFixture.doMain("-v")
        self.assertEqual( self.OK, r.getReturnCode() )

        