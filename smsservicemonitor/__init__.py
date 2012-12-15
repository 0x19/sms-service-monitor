import os, logging, socket 

from smsservicemonitor.utils import memoized, filter_e164, validate_e164
from smsservicemonitor       import exceptions, constants

from telapi                  import rest

class Service(object):

    def __init__(self, telapi_account_sid=None, telapi_auth_token=None, from_address=None, to_address=None, *args, **kwargs):
        object.__init__(self)

        self.telapi_account_sid = telapi_account_sid or os.environ.get('TELAPI_ACCOUNT_SID')
        self.telapi_auth_token  = telapi_auth_token  or os.environ.get('TELAPI_AUTH_TOKEN')
        self.from_address       = from_address       or os.environ.get('SMSSERVICEMONITOR_FROM_ADDRESS')
        self.to_address         = to_address         or os.environ.get('SMSSERVICEMONITOR_TO_ADDRESS')

        self.services           = {}

        if not self.telapi_account_sid or not self.telapi_account_sid.startswith("AC"):
            raise exceptions.AccountSidError()

        if not self.telapi_auth_token or len(self.telapi_auth_token) != 32:
            raise exceptions.AuthTokenError()

        if not validate_e164(self.from_address):
            raise exceptions.SourceAddressError()

        self.from_address = filter_e164(self.from_address)

        if not validate_e164(self.to_address):
            raise exceptions.DestinationAddressError()

        self.to_address  = filter_e164(self.to_address)

        self.telapi_client = rest.Client(self.telapi_account_sid, self.telapi_auth_token)


    ''' Add desired service to the internal storage. '''
    def add(self, service_id=None, host=None, port=80, *args, **kwargs):
        
        if type(service_id) != str or len(service_id) < 2:
            raise exceptions.ServiceInvalidIdError()

        if not host or type(host) != str:
            raise exceptions.ServiceHostError()

        if not port or type(port) != int:
            raise exceptions.ServicePortError()

        self.services[service_id.lower()] = [host, port]


    ''' Get details of the service if available. If not available, return none '''
    def get_service(self, service_id):
        try:
            return self.services[service_id.lower()]
        except KeyError:
            return None


    ''' Return back all of the existing service items '''
    def all(self):
        return self.services.items()


    ''' Remove existing serivice from the internal storage '''
    def remove(self, service_id):

        if not service_id.lower() in self.services:
            raise exceptions.ServiceIdError()

        del self.services[service_id.lower()]

        return True


    ''' Check whenever service is available '''
    def is_available(self, service_id):

        if not service_id.lower() in self.services:
            raise exceptions.ServiceIdError()

        service_details = self.services[service_id.lower()]

        service_host    = socket.gethostbyname(service_details[0])
        service_port    = service_details[1]

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(constants.SOCKET_TIMEOUT)
        socket_status = sock.connect_ex((service_host, service_port))
        sock.close()

        if socket_status == 0: return True

        return False


    ''' Send SMS message '''
    def send_sms(self, service_id):
        
        account  = self.telapi_client.accounts[self.telapi_client.account_sid]

        if not service_id.lower() in self.services:
            raise exceptions.ServiceIdError()

        service_details = self.services[service_id.lower()]

        sms_message = account.sms_messages.create(
            from_number = self.from_address,
            to_number   = self.to_address,
            body        = constants.FAILED_SERVICE_SMS % (service_details[0], service_details[1]),
        )

        return True
