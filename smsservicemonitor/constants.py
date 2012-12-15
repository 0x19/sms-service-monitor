''' This file is here to help out with ... '''
import os

### PACKAGE-WIDE CONSTANTS ###

PACKAGE_VERSION = '0.1.0.1'

### SOCKET CONSTANTS ###

# How much seconds to wait before timeout occurs
SOCKET_TIMEOUT = 3

### SMS CONSTANTS ###

# SMS message that will be sent out to the destination/s provided when service fails.
# First %s represent host and second % represent ports. They must be defined here so be careful when
# changing SMS message look.
FAILED_SERVICE_SMS = "Woops! Service connectivity failed for host %s and port %s."