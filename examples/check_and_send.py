from smsservicemonitor import Service

# ALL parameters that are passed in Service are REQUIRED
services = Service(
    telapi_account_sid  = '{account_sid}',
    telapi_auth_token   = '{auth_token}',
    from_address        = '{source_phone_number}',      # This should be a TelAPI phone number
    to_address          = '{destination_phone_number}',
)

service_key = '{some_logical_service_key}'

# Add new service into internal Service storage. Default service port is 80 so it optional
# ServiceID and host are on the other hand, required!
services.add( service_key, host = '{some_domain_name}', port = 80 )

# Loop throu all services and send SMS message if particular service fails
for service_key, service_data in services.all():
	print "Checking if host %s and port %s are available" % (service_data[0], service_data[1])

	if not services.is_available(service_key):
		services.send_sms(service_key)