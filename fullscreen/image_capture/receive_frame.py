#!/usr/bin/env python
'''
Writes out data received from websocketd on stdin as 
png frames.
'''

# modified from: https://gist.github.com/payload/aaf97ba000c789e0a8141d58ded1218b

import time
import base64
import binascii
from sys import stdin, stdout
import StringIO
import os
import numpy as np



# From http://stackoverflow.com/a/9807138
def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)

def main():
    '''
    As each frame is received write it to a .png file
    '''

    #frames = 1600
    count = 0
    
    while True:

        received_val = stdin.readline()
        count = count + 1
        # Right pad filenames so they can be sorted
        filename = "frames/%s.png" % count #str(time.time()).ljust(13, "0") + ".png"
        with open(filename, 'wb') as file_handle:
            try:
                file_handle.write(decode_base64(received_val))
                #frames += 1
                if count % 10 == 0:
                    print("Captured %d frames ..." % count)
                    stdout.flush()
            except binascii.Error:
                # Ignore malformed data urls
                continue
            
if __name__ == '__main__':
    main()
