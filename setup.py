import os
from   setuptools          import setup
from   smsservicemonitor   import constants

setup(
    name                = "smsservicemonitor",
    version             = constants.PACKAGE_VERSION,
    description         = "Monitor your service ( servers and their respective ports ) and send SMS message to your cell phone if they are down.",
    author              = "Nevio Vesic",
    author_email        = "nevio.vesic@gmail.com",
    license             = "MIT",
    url                 = "http://0x19.github.com/sms-service-monitor/",
    keywords            = ["telapi", "sms", "telephony", "python", "services", "monitoring"],
    install_requires    = ["requests", "telapi"],
    packages            = ['smsservicemonitor', 'smsservicemonitor.exceptions'],
    classifiers         = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        "Topic :: Internet",
        "Topic :: System :: Networking",
        "Topic :: Internet :: WWW/HTTP"
    ],
    long_description    = """ Monitor your service ( servers and their respective ports ) and send SMS message to your cell phone if they are down. This package is just helper. It implements all base functionallity you need, rest is up to you! """,
)
