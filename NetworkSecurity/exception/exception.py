import sys
class NetworkSecurityException(Exception):
    """Custom exception class for network security related errors."""
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_, exc_tb = error_details.exc_info() # gets the traceback object 
        self.line_number = exc_tb.tb_lineno # gets the line number where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename # gets the file name where the exception occurred

    def __str__(self):
        return f"Error occurred in script: {self.file_name} at line number: {self.line_number} with message: {self.error_message}"    
    

   