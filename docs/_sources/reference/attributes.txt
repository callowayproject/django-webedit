==============
API Attributes
==============

**author**
	The author of the item.
	
	*Default:* ``''``
	
	*Aliases:* ``wp_author_display_name``
	
	*Notes:* The author can either be a string or a Django model. If it is a Django model, its :py:func:`__unicode__` representation is used. The model's ``pk`` attribute is also used for the **author_id**.

**author_id**
	The ID of the author of the item
	
	*Default:* ``0``
	
	*Aliases:* ``userid``\ , ``wp_author_id``
	
	*Notes:* If the ``author`` attribute is a Django model, ``author_id`` will be its ``pk`` attribute. Otherwise an integer is required.

**status**
	The publish status of the item, such as 'draft', 'private' or 'publish'.
	
	*Default:* ``publish``

	*Aliases:* ``page_status``\ , ``post_status``

**id**
	The ID of the post
	
	*Default:* ``pk`` attribute of the model
	
	*Aliases:* ``page_id``\ , ``postid``

**permalink**
	The absolute URL to this item
	
	*Default:* Calling ``get_absolute_url()`` on item
	
	*Aliases:* ``link``\ , ``permaLink``

**categories**
	The category(ies) attributed to this item
	
	*Default:* []
	
	*Aliases:* *None*

**excerpt**
	A brief section of the item, typically the first part of the content.
	
	*Default:* ''
	
	*Aliases:* ``mt_excerpt``

**creation_date**
	The date the item was first created.
	
	*Default:* *None*
	
	*Aliases:* ``date_created_gmt``\ , ``dateCreated``

**slug**
	A URL-izeable string that is typically also used in the URL of the item.
	
	*Default:* ''
	
	*Aliases:* ``wp_slug``

**title**
	The title or headline of the item
	
	*Default:* ''
	
	*Aliases:* *None*

**content**
	The content of the item
	
	*Default:* ''
	
	*Aliases:* ``description``

**allow_comments**
	Can people comment on this item. Yes = 1, No = 0
	
	*Default:* ``1``
	
	*Aliases:* ``mt_allow_comments``

**allow_pings**
	Can people ping this item. Yes = 1, No = 0
	
	*Default:* ``1``
	
	*Aliases:* ``mt_allow_pings``

**custom_fields**
	Custom key/values in a ``[{'id': '', 'key': '', 'value': ''}, ]`` format.
	
	*Default:* ``[]``
	
	*Aliases:* *None*