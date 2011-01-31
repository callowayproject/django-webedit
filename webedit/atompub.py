"""
Views for handling the Atom Protocol

e.g. Public URLs
GET /feeds/blogs (list Blog objects) <link rel="alternate" .../>
POST /feeds/blogs (new Blog object) <link rel="service.post" .../>
GET /feeds/blogs/<blog>/entry (entry objects) <link rel="alternate" .../>

e.g. Edit URLs
GET /atom/blogs (full list of Blog objects)
POST /atom/blogs (New Blog object) <link rel="service.post" .../>
PUT /atom/blogs/<blog> (Update Blog object)
DELETE /atom/blogs/<blog> (Delete Blog object)

GET /feeds/blogs/<blog>/entry (full list entry objects) <link rel="alternate" .../>
POST /feeds/blogs/<blog>/entry (new entry object) <link rel="service.post" .../>
PUT /feeds/blogs/<blog>/entry/<entry> (update entry object) <link rel="service" .../>
DELETE /feeds/blogs/<blog>/entry/<entry> (delete entry object) <link rel="service" .../>

"""
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.encoding import iri_to_uri
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

class HttpResponseCreated(HttpResponse):
    status_code = 201

    def __init__(self, item_url):
        HttpResponse.__init__(self)
        self['Location'] = iri_to_uri(item_url)

class HttpResponseAccepted(HttpResponse):
    status_code = 202

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401
    
    def __init__(self):
        super(HttpResponseUnauthorized, self).__init__()
        self['WWW-Authenticate'] = 'Atom realm="some server realm name", qop="atom-auth", algorithm="SHA", nonce="some unique server-specific value"'

class EditFeed(Feed):
    feed_type = Atom1Feed


class AtomPub(object):
    edit_url_pattern = ""
    public_url = ""
    
    def create(self, *args, **kwargs):
        """
        POST entry to public_uri
        """
        pass
    
    def retrieve(self, *args, **kwargs):
        """
        GET feed to public_uri or edit_uri
        """
        pass
    
    def delete(self, *args, **kwargs):
        """
        DELETE request to edit_url
        """
        pass
    
    def update(self, *args, **kwargs):
        """
        PUT to the edit_url
        """
        pass


def feedview(request):
    import pprint
    if request.method == 'GET':
        return render_to_response("get_entries_response.xml", mimetype="application/atom+xml")
        # return render_to_response("response.xml", mimetype="application/atom+xml")
    elif request.method == 'POST':
        pprint.pprint(request.raw_post_data)
        pprint.pprint(request.META)
        # return HttpResponseAccepted()
        return HttpResponseUnauthorized()