
class SongerResult:
    """
    A simple struct for holding the result of a process-like command. Has return code, stdout, and
    stderr.
    """
    
    _returnCode = 0
    _stdoutput  = ""
    _stderrput  = ''
    
    def __init__(self, returnCode, stdoutput, stderrput):
        self._returnCode = returnCode
        self._stdoutput  = stdoutput
        self._stderrput  = stderrput
        
        
    def getReturnCode(self):
        return self._returnCode
        
    def getStdoutput(self):
        return self._stdoutput
        
        
    def getStderrput(self):
        return self._stderrput
        
        