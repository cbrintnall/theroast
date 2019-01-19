class RoastError(Exception):
    def __init__(self, message, status_code=500, *args, **kwargs):
        self.status_code = status_code
        super(RoastError, self).__init__(message, *args, **kwargs)