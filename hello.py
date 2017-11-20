def app(environ, start_response):

    string = environ["QUERY_STRING"].split('&')
    data = ""
    for i in string:
        data = data + i + "\n"    
     
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [bytes(data, 'ascii')]
