
# In[ ]:

from thirdParty.proxpy.core import *


# In[ ]:

opts = ProxyState()
opts.listenport = 8080
opts.listenaddr = '0.0.0.0'
opts.plugin = ProxyPlugin('proxyPlugins/passthrough.py')


# In[ ]:

server = ProxyServer(opts)
server.startProxyServer()


# In[ ]:

server.stopProxyServer()


# In[ ]:



