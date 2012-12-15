''' Package Exceptions '''

class AccountSidError(Exception):
    message = "Please pass account_sid when instantiating the REST API Client or set the environment variable `TELAPI_ACCOUNT_SID`.\
        An account SID is a 34 character string that starts with the letters 'AC'."

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code
        

class AuthTokenError(Exception):
    message = "Please pass auth_token when instantiating the REST API Client or set the environment variable `TELAPI_AUTH_TOKEN`.\
        An auth token is 32 characters long."

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class SourceAddressError(Exception):
    message = "Please pass from_address when instantiating SMS Service Service or set the environment variable `SMSSERVICEMONITOR_FROM_ADDRESS`.\
        An from_address should be TelAPI number in E.164 format."

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class DestinationAddressError(Exception):
    message = "Please pass to_address when instantiating SMS Service Monitor or set the environment variable `SMSSERVICEMONITOR_TO_ADDRESS`.\
        An from_address should be destination number in E.164 format that is capable to receive SMS messages.\
        Usually, your mobile phone number!"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class ServiceInvalidIdError(Exception):
    message = "Invalid Service ID provided. Please make sure that service ID contains ONLY strings and that it is more than 1 character long"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class ServiceIdError(Exception):
    message = "Invalid Service ID provided. Please make sure that service you added and service you tried to reach have same ID"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class ServiceHostError(Exception):
    message = "Invalid Service host provided. Please make sure that service host argument is set as string!"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code


class ServicePortError(Exception):
    message = "Invalid Service port provided. Please make sure that service port argument is set as integer!"

    def __init__(self, error_code=None, http_code=None):
        Exception.__init__(self, self.message)
        self.message    = self.message
        self.error_code = error_code
        self.http_code  = http_code