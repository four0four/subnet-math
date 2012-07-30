#!/usr/bin/python2

import subnetMath

print "Combined:"
test = subnetMath.Subnet("192.168.0.1/16")
print ".toIPaddress(): " + str(test.toIPaddress())
print ".toBroadcast(): " + str(test.toBroadcast())
print ".toNetmask(): " + str(test.toNetmask())
print ".toSubnet(): " + str(test.toSubnet()) 
print ".toSubnetZeroed(): " + str(test.toSubnetZeroed())

print "Split:"
test2 = subnetMath.Subnet("192.168.0.1","255.255.0.0")
print ".ipString(): " + str(test2.ipString())
print ".broadcastString(): " + str(test2.broadcastString())
print ".netmaskString(): " + str(test2.netmaskString())
print ".subnetString(): " + str(test2.subnetString()) 
print ".subnetZeroedString(): " + str(test2.subnetZeroedString())


