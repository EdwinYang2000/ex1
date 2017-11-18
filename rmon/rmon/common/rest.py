"""rmon.common.rest"""

class RestException(Exception):
    """exception  class"""

    def __init__(self,code,message):
        """ init exception

        Aargs:
            code(int):http status code
            message (str): error info
        """
        self.code = code
        self.message = message
        super(RestException, self).__init__()


