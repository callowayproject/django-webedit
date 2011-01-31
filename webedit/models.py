from django.db import models

"""
Handle Categories
Handle Media
Handle Workspaces/Groups of Collections
Handle mimetypes accepted

<meta name="generator" content="blogger" />
<meta name="generator" content="WordPress.com">
<link rel="service.post" type="application/atom+xml" title="asdfasdfasdf" href="path to blog post service"


Workspace = Admin Site
Collection = Model
"""

class Collection(object):
    """docstring for Collection"""
    
    href = "" # for posting an entry to this collection, the view or name of url
    title = ""
    accept = ()
    author = ""
    update_field = ""
    
    model = 'app.model'
    
    feed_id = "tag:%(domainname)s,%(year)s:%(model)s:feed"
    
    