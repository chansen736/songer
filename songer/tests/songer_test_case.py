# Harness imports
import unittest

# Module-under-test imports
import songer

class SongerTestCase(unittest.TestCase):
    """
    Top-level test case for all songer tests.
    """
    
    # Shorthand error codes from the module
    OK = songer.RETURN_OK
    ERROR = songer.RETURN_ERROR
    
    """ TEST CASES """
    
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
        self.assertEqual( self.OK, SongerTestCase.doMain("-h") )
    
    
    """ HELPER FUNCTIONS """
    
    @classmethod
    def doMain(cls, commandline):
        """
        Calls songer's main function with the given commandline
        """
        
        try:
            r = songer.main( commandline.split() )
        except SystemExit, x:
            r = x.code
        
        return r
        
        