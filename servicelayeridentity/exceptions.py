class TokenRequestError(Exception):
    def __init__(self, error_message, status_code):
        self.message = "Error requesting token %s with code %s" \
              % (error_message, status_code)
        super(TokenRequestError, self).__init__(self.message)
