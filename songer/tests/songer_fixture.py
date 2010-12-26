# Harness imports
import unittest

# Module-under-test imports
import songer

class SongerFixture():
    """
    Top-level fixture for all songer tests.
    """
    
    # Shorthand error codes from the module
    OK = songer.RETURN_OK
    ERROR = songer.RETURN_ERROR
    
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
        
        