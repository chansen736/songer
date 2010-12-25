# Harness imports
import sys
import unittest

# Module-under-test imports
import songer

class ERROR_CODES:
    """
    Enum for error codes.
    """
    
    OK = 0
    TESTS_FAILED = 1
    SETUP_FAILED = 2
    
    
def main( argv ):
    """
    Run all the tests.
    
    argv: command-line arguments
    
    return: ERROR_CODES.OK if successful, the appropriate error code otherwise
    
    """
    # Load all the tests in the "test" directory
    suite = unittest.TestLoader().discover( "tests", pattern = "*_test_case.py" )
    # Run them. verbosity=2 prints the function names and output, and buffer=True only prints
    # output on test failure.
    result = unittest.TextTestRunner( verbosity = 2 , buffer = True ).run( suite )
    
    if result.wasSuccessful():
        return ERROR_CODES.OK
    return ERROR_CODES.TESTS_FAILED
    
if __name__ == '__main__':
    sys.exit( main( sys.argv ) )