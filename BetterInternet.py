
# In[1]:

from proxpy.core import *


# In[2]:

opts = ProxyState()
opts.listenport = 8080
opts.listenaddr = '0.0.0.0'
opts.plugin = ProxyPlugin('proxyPlugins/replace.py')


# In[*]:

server = ProxyServer(opts)
server.startProxyServer()


# In[ ]:

server.stopProxyServer()


# In[ ]:



