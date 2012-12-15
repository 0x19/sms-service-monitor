sms-service-monitor
===================

Monitor your service ( server/s &amp;&amp; their respective ports ) and send SMS message to destination/s once they are down.

This package is more simple helper than anything else. There is no one method to do it all. The best thing to do is to look into:

[Sms Service Monitor Examples](https://github.com/0x19/sms-service-monitor/tree/master/examples)

#### Requirements

- You need to have [TelAPI account](http://telapi.com)
- You must install package ( Python 2.6+ )

#### By GitHub clone

```shell
$ cd ~
$ git clone https://github.com/0x19/sms-service-monitor.git
$ cd sms-service-monitor
$ python setup.py install
```

#### By PIP

```shell
$ pip install smsservicemonitor
```

### Step by step installation

**1.) Run the package installation**

You can choose one of the approaches defined above.  

**2.) navigate yourself to examples**

You can find them at [Sms Service Monitor Examples](https://github.com/0x19/sms-service-monitor/tree/master/examples)

**3.) Open `check_and_send.py` example and modify following code**

```python
services = Service(
    telapi_account_sid  = '{account_sid}',
    telapi_auth_token   = '{auth_token}',
    from_address        = '{source_phone_number}',      # This should be a TelAPI phone number
    to_address          = '{destination_phone_number}',
)
```

- `telapi_account_sid` : Can be found at [TelAPI Dashboard](https://telapi.com/dashboard)
- `telapi_auth_token`  : Can be found at [TelAPI Dashboard](https://telapi.com/dashboard)
- `from_address`       : You need to own [TelAPI Number](https://www.telapi.com/numbers/)
- `to_address`         : Your mobile phone number in E.164 format e.g. +1 555 555 5555

** Next step is to modify service key '{some_logical_service_key}' and set service host '{some_domain_name}' **

Service host must be or IP address or FQDN ( Fully qualified domain name ). 

By default, port is set to be 80 so in case you want to check if website is alive or not you can skip port setup.

```python
service_key = '{some_logical_service_key}'

# Add new service into internal Service storage. Default service port is 80 so it optional
# ServiceID and host are on the other hand, required!
services.add( service_key, host = '{some_domain_name}', port = 80 )
```

**4.) Save the example `check_and_send.py` and run it**

It's pretty easy to run the file now. Just do:

```shell
python check_and_send.py
```

**And that's it :) For more details about usage please wait for me or contact me by:**

### Need more info?
Create new [Github ticket](https://github.com/0x19/sms-service-monitor/issues) and I'll make sure it gets solved ASAP!

### Contact
You can always reach me at few places :)

**E-mail:**   nevio.vesic@gmail.com - 
**Facebook:** https://www.facebook.com/noxten - 
**Linkedin:** http://www.linkedin.com/in/neviovesic - 
**Twitter:**  https://twitter.com/vesicnevio