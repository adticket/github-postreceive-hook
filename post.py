# -*- coding: utf-8 -*-
"""
    Post-Commit-Hook für github
    Führt ein git pull aus
    
    @author Markus Tacker <m@coderbyheart.de>
"""
from cgi import parse_qs
#import json
import os
import subprocess

def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
        
    if request_body_size == 0:
        status = '412 Precondition Failed'
        output = 'No post data provided'
    else:
        request_body = environ['wsgi.input'].read(request_body_size)
        d = parse_qs(request_body)
        
        if 'payload' in d:
            # payloadJson = ''.join(d.get('payload'))
            # payload = json.loads(payloadJson)
        
            subprocess.call(['/bin/bash', 'postreceive.sh'], cwd=os.path.join(os.path.dirname(environ['SCRIPT_FILENAME']), '..' + os.sep))
        
        status = '200 OK'
        output = "Thank you very much.\n"
        
    response_headers = [('Content-type', 'text/plain; charset=utf-8'),
                                ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
