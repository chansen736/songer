# Harness imports
import sys
import unittest

from songer_result import SongerResult
from StringIO      import StringIO

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
        Calls songer's main function with the given commandline.
        
        commandline: string representing the commandline with which you'd call the songer module.
                     For example, doMain("-h") is equivalent to "songer.py -h".
        return: songer_result.SongerResult containing the output of the command.
        """
        
        _stdout = sys.stdout
        _stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        
        try:
            rCode = songer.main( commandline.split() )
        except SystemExit, x:
            rCode = x.code
        
        result = SongerResult( returnCode = rCode,
                               stdoutput = sys.stdout.getvalue(),
                               stderrput = sys.stderr.getvalue() )
        sys.stdout.close()
        sys.stderr.close()
        
        sys.stdout = _stdout
        sys.stderr = _stderr
        
        return result
        
        