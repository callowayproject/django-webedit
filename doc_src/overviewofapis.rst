
Blogging API Overview
=====================

There are several ways that external clients may interact with blogging software:

* XML-RPC (Wordpress, MetaWeblog, Moveable Type, old Blogger)
	* http://codex.wordpress.org/XML-RPC_Support
	* http://www.xmlrpc.com/metaWeblogApi
	* http://www.sixapart.com/pronet/breese/xmlrpc/movable_type_api/
* Atom (Blogger, TypePad)
	* http://code.blogger.com/
* HTTP (Tumblr)
	* http://www.tumblr.com/docs/en/api
* REST (Posterous)
	* http://apidocs.posterous.com/


We can rule implementing out Atom because its authentication system requires that both sides of the conversation know the unencrypted password. Django doesn't store passwords in a reversible encrypted form, and I whole-heartedly agree with that decision.

Basic Methods
=============

Get Post Information
********************

``mt.getRecentPostTitles(blogid, username, password, numberOfPosts)``

``wp.getPageList(blog_id, page_id, username, password)``

mt return struct::

	{
	    'dateCreated': datetime (ISO.8601), 
	    'userid': str,
	    'postid': str,
	    'title': str,
	}

wp return struct::

	{
	    'page_id': int,
	    'page_title': str,
	    'page_parent_id': int,
	    'dateCreated': datetime (iso8601)YYYYMMDDTHH:mm:SS,
	}

``metaWeblog.getRecentPosts(blogid, username, password, numberOfPosts)``

``wp.getPages(blog_id, username, password)``

``metaWeblog.getPost(postid, username, password)``

``wp.getPage(blog_id, page_id, username, password)``

metaWeblog return struct::

	{
	    'title': str,
	    'description': str,
	    'dateCreated': datetime (iso8601)YYYYMMDDTHH:mm:SS,
	    'enclosure': {'length': int, 'type': str, 'url': str},
	    'source': {'name': str, 'url': str},
	    'author': str,
	    'categories': [str, ...],
	    'link': str,
	}


wp getPage/getPages struct::

	{
	    'userid': int,
	    'page_id': int,
	    'page_status': str,
	    'link': str,
	    'permaLink': str,
	    'categories': [str,],
	    'excerpt': str,
	    'text_more': str,
	    'wp_author': str,
	    'wp_page_parent_title': str,
	    'wp_author_display_name': str,
	    'date_created_gmt': datetime (gmt),
	    'wp_page_template': str,
	    'wp_slug': str,
	    'wp_password': str,
	    'wp_page_parent_id': int,
	    'wp_page_order': int,
	    'wp_author_id': int,
	    'title': str,
	    'description': str,
	    'mt_excerpt': str,
	    'mt_text_more': str,
	    'mt_allow_comments': int,
	    'mt_allow_pings': int,
	    'dateCreated': datetime (iso8601)YYYYMMDDTHH:mm:SS,
	    'custom_fields': [{
	        'id': str,
	        'key': str,
	        'value': str
	    },]
	}


Set Post Information
********************

``metaWeblog.newPost(blogid, username, password, content, publish)``

``metaWeblog.editPost(postid, username, password, content, publish)``

``wp.newPage(blogid, username, password, content, publish)``

``wp.editPage(blogid, username, password, content, publish)``

metaWeblog content struct::

	{
	    'title': str,
	    'description': str,
	    'dateCreated': datetime (iso8601)YYYYMMDDTHH:mm:SS,
	    'enclosure': {'length': int, 'type': str, 'url': str},
	    'source': {'name': str, 'url': str},
	    'author': str,
	    'categories': [str, ...],
	    'link': str,
	}

WordPress content struct::

	{
	    'wp_slug': str,
	    'wp_password': str,
	    'wp_page_parent_id': int,
	    'wp_page_order': int,
	    'wp_author_id': int,
	    'title': str,
	    'description': str,
	    'mt_excerpt': str,
	    'mt_text_more': str,
	    'mt_allow_comments': int,
	    'mt_allow_pings': int,
	    'dateCreated': datetime (iso8601)YYYYMMDDTHH:mm:SS,
	    'custom_fields': [{
	        'id': str,
	        'key': str,
	        'value': str
	    },]
	}

``mt.publishPost(post_id, username, password)``


Get Category Information
************************

``mt.getCategoryList(blog_id, username, password)``

``metaWeblog.getCategories(blog_id, username, password)``

``wp.getCategories(blog_id, username, password)``

mt return struct::

	[{
	    'categoryId': str,
	    'categoryName': str
	},]

metaWeblog return struct::

	[{
		'description': str,
		'htmlUrl': str,
		'rssUrl': str,
	},]

wp return struct::

	[{
	    'categoryId': int,
	    'parentId': int,
	    'description': str,
	    'categoryName': str
	    'htmlUrl': str,
	    'rssUrl': str,
	},]
	
``mt.getPostCategories(postid, username, password)``

mt return struct::

	[{
	    'categoryName': str,
	    'categoryId': str,
	    'isPrimary': bool
	},]


Set Category Information
************************

mt.setPostCategories(postid, username, password, categories)

mt categories struct::

	[{
	    'categoryId': str,
	    'isPrimary': bool
	},]


``wp.newCategory(blog_id, username, password, category)``

wp category struct::

	{
	    'name': str,
	    'slug': str,
	    'parent_id': int,
	    'description': str
	}

``wp.deleteCategory(blog_id, username, password, category_id)``

Media Objects
*************

``metaWeblog.newMediaObject(blogid, username, password, content)``

metaWeblog content struct::

	{
	    'name': str,
	    'type': str (mimetype),
	    'bits': base64-encoded binary content
	}

metaWeblog return struct::

	{
	    'url': str
	}

``wp.uploadFile(blog_id, username, password, data)``

wp data struct::

	{
	    'name': str,
	    'type': str (mimetype),
	    'bits': base64-encoded binary content,
	    'overwrite': bool
	}

wp return struct::

	{
	    'file': str,
	    'url': str,
	    'type': str
	}


Misc
****

``mt.supportedMethods``

``mt.supportedTextFilters``

``mt.getTrackbackPings``

