import gzip
from StringIO import StringIO 
from bs4 import BeautifulSoup
from bs4 import Comment
import upsidedown 

def strainSoupForText(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif isinstance(element, Comment):
		return False
	return True

def upsidedownternet(response):
	soup = BeautifulSoup(response.body)
#	textSoup = soup.findAll(text=strainSoupForText)
	for element in soup.findAll('body'):
		#element = element.replace_with(upsidedown.transform(element))
		flipped = "-webkit-transform:scaleX(-1);-ms-transform:scaleX(-1);"
		if 'style' in element.attrs.keys():
			element.attrs['style'] += flipped
		else:
			element.attrs['style']=flipped
	response.body = str(soup)

def makeInternetBetter(response):
	#depending on the header i injected in proxpy/core.py doGet
	origHost = response.getHeader('origHost')
	if not origHost: return
	if 'reddit.com' in origHost[0]:
		upsidedownternet(response)

def fixWaybackToolbar(response):
	if response.getHeader('X-Archive-Orig-contentlocation'):
		toolbarStart = response.body.index('<!-- BEGIN WAYBACK TOOLBAR INSERT -->')
		toolbarEnd = response.body.index('<!-- END WAYBACK TOOLBAR INSERT -->')
		response.body = response.body[:toolbarStart] + response.body[toolbarEnd:-1]

def fixContentLength(response):
	contentLength = response.getHeader('Content-Length')
	if contentLength:
		response.setHeader('Content-Length', len(response.serialize()))

def unzip(response):
	contentEncoding = response.getHeader('Content-Encoding')
	if contentEncoding and contentEncoding[0] == 'gzip':
		response.body = gzip.GzipFile(fileobj=StringIO(response.body)).read()
		del response.headers['Content-Encoding']	

def fixCharset(response,contentType):
	if 'charset=UTF-8' in contentType:
		response.body = unicode(response.body)

def proxy_mangle_response(response):
	contentType = response.getHeader('Content-Type')	
	if contentType and 'text/html' in contentType[0]:		
		unzip(response)		
		fixCharset(response,contentType)
		makeInternetBetter(response)
		fixWaybackToolbar(response)
		fixContentLength(response)
	return response

def proxy_mangle_request(request):
	if request.getHost()[0] == 'www.google.com':
		if request.getPath()=='/':
			request.url = 'http://web.archive.org/web/20000301035559/http://askjeeves.com/'
		else:
			request.url = 'http://web.archive.org' + request.getPath()
		request.setHeader('Host','web.archive.org')
	return request
