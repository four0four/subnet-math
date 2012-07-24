#!/usr/bin/python2

import subnetMath

#test = subnetMath.Subnet("192.168.0.1","255.255.0.0")
test = subnetMath.Subnet("192.168.0.1/16")
print ".toIPaddress(): " + str(test.toIPaddress())
print ".toBroadcast(): " + str(test.toBroadcast())
print ".toNetmask(): " + str(test.toNetmask())
print ".toSubnet(): " + str(test.toSubnet()) 
print ".toSubnetZeroed(): " + str(test.toSubnetZeroed())

