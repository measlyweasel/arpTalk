import gzip
from StringIO import StringIO 
from bs4 import BeautifulSoup
from bs4 import Comment
import upsidedown

askJeevesUrl = 'http://web.archive.org/web/20000511005423/http://askjeeves.com/'

def soupStrainForText(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif isinstance(element, Comment):
		return False
	return True

def improveInternet(body):
	soup = BeautifulSoup.BeautifulSoup(body)
	textSoup = soup.findAll(text=True)
	for element in textSoup:
		element.replace_with(upsidedown.transform(unicode(element)))

	return body

def fixContentLength(response):
	contentLength = response.getHeader('Content-Length')
	if contentLength:
		response.setHeader('Content-Length', len(response.serialize()))

def unzip(response):
	contentEncoding = response.getHeader('Content-Encoding')
	if contentEncoding and contentEncoding[0] == 'gzip':
		response.body = gzip.GzipFile(fileobj=StringIO(response.body)).read()
		del response.headers['Content-Encoding']
					
		fixContentLength(response)

def fixCharset(response):
	if 'charset=UTF-8' in contentType:
		response.body = unicode(response.body)

def proxy_mangle_response(response):
	contentType = response.getHeader('Content-Type')	
	if contentType and 'text/html' in contentType[0]:
		unzip(response)		
		fixCharset(response)		
		if response.url == askJeevesUrl:
			response.url == 'www.google.com/'
		else:
			response.body = textReplace(response.body)	
		
	return response

def proxy_mangle_request(request):
	if request.getHost() == 'google.com' and request.getPath() == '/':
		request.url = askJeevesUrl
