#!/usr/bin/env python
from snmp_helper import snmp_get_oid,snmp_extract

targets = [['50.242.94.227', 'galileo', 7961], ['50.242.94.227', 'galileo', 8061]]
my_oids = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0']

print

for index, device in enumerate(targets):
    target_device = (device[0], device[1], device[2])
    pretty_name = snmp_extract(snmp_get_oid(target_device, oid=my_oids[0]))
    pretty_desc = snmp_extract(snmp_get_oid(target_device, oid=my_oids[1]))
    print pretty_name
    print pretty_desc
    print

print

