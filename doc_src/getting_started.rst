
Getting Started
===============


Define the API class
====================

Subclass the :class:`BaseAPI` and define a ``model`` attribute. This model is the equivalent of a blog post and is what gets edited.

.. code-block:: python

	class MyWebEdit(BaseAPI):
	    model=Post

By default any API call that references a blog ignores the blog value. If, however, your model has a "parent" relationship (like blog post has to blog), you can define it as well:

.. code-block:: python

	class MyWebEdit(BaseAPI):
	    model=Post
	    parent=Blog


Map the model attributes
========================

The API has several ways to get the information it needs from your model.

Attribute names
***************

If your model has an attribute with the correct name, it will use it.

Field maps
**********

You can specify the attribute name to use for an API field.

.. code-block:: python

	class MyWebEdit(BaseAPI):
	    model=Post
	    field_map = {
	        'title': 'headline',
	        'description': 'content'
	    }

Method Overrides
****************

Each attribute uses a ``get_FIELDNAME`` method to get its value. You can override this to return a calulated value.

.. code-block:: python

	class MyWebEdit(BaseAPI):
	    model=Post
	    
	    field_map = {
	        'title': 'headline',
	        'description': 'content'
	    }
	    
	    def get_excerpt(self, obj):
	        return "%s..." % obj.content[:300]




uses generic functions to get the data and then return in in the format for the call (wp, mt, mwb)
