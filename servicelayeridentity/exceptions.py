class TokenRequestError(Exception):
    def __init__(self, error_message, status_code):
        self.message = "Error (%s) requesting security token: %s" \
              % (status_code, error_message)
        super(TokenRequestError, self).__init__(self.message)
