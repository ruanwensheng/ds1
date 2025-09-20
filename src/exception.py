import sys
import logging
from src.logger import logging



def error_message(error, error_detail: sys):
    _,_,exc_traceback = error_detail.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = 'error occurred in script name [{0}] line number [{1}] error message[{2}]'.format(
        file_name, exc_traceback.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error, error_detail:sys):
        super().__init__(error)
        self.error_message = error_message(error, error_detail)
    def __str__(self):
        return self.error_message
    

if __name__=='__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info("bat dau log")
        raise CustomException(e, sys)    

