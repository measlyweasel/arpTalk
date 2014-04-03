import gzip
from StringIO import StringIO 

def textReplace(body):
	return body.replace(" is ", " YOLO SWAG ")

def proxy_mangle_response(response):
	contentType = response.getHeader('Content-Type')
	
	if contentType and 'text/html' in contentType[0]:
		contentEncoding = response.getHeader('Content-Encoding')
		
		if contentEncoding and contentEncoding[0] == 'gzip':
			response.body = gzip.GzipFile(fileobj=StringIO(response.body)).read()
			del response.headers['Content-Encoding']
						
			contentLength = response.getHeader('Content-Length')
			if contentLength:
				response.setHeader('Content-Length', len(response.serialize()))

		if 'charset=UTF-8' in contentType:
			response.body = unicode(response.body)

		response.body = textReplace(response.body)	
		
	return response
