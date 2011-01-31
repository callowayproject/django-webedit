

class BaseApi(object):
    """
    Handles all the methods
    """
    parent_model = None
    model = None
    
    field_map = {
        'author': 'author',
        'author_id': 'author_id',
        'status': 'status',
        'id': 'id',
        'permalink': 'permalink',
        'categories': 'categories',
        'excerpt': 'excerpt',
        'creation_date': 'creation_date',
        'slug': 'slug',
        'title': 'title',
        'content': 'content',
        'allow_comments': 'allow_comments',
        'allow_pings': 'allow_pings',
        'custom_fields': 'custom_fields',
    }
    def __init__(self):
        pass
    
    def get_custom_fields(self, obj):
        """
        Default custom field handler. Return an empty list
        """
        return []
    
    def get_allow_comments(self, obj):
        """
        Default allow comments handler. Return 1
        """
        return 1
    
    def get_allow_pings(self, obj):
        """
        Default allow pings handler. Return 1
        """
        return 1
    
    def get_author(self, obj):
        """
        Default
        """
        return ''
    
    def get_author_id(self, obj):
        """
        Check if the author has an id or pk attribute and return that or else 0
        """
        author = self.get_field('author_id', obj)
        if hasattr(author, 'pk'):
            return author.pk
        elif hasattr(author, 'id'):
            return author.id
        else:
            return 0
    
    def get_status(self, obj):
        return "publish"
    
    def get_id(self, obj):
        if hasattr(obj, 'pk'):
            return obj.pk
        elif hasattr(obj, 'id'):
            return obj.id
        else:
            return 0
    
    def get_permalink(self, obj):
        if hasattr(obj, 'get_absolute_url'):
            return obj.get_absolute_url()
        else:
            return ''
    
    def get_categories(self, obj):
        return []
    
    def get_excerpt(self, obj):
        return ''
    
    def get_creation_date(self, obj):
        return ''
    
    def get_slug(self, obj):
        return ''
    
    def get_title(self, obj):
        return ''
    
    def get_content(self, obj):
        return ''
    
    def get_field(self, field, obj):
        if callable(field):
            return field(obj)
        elif hasattr(obj, field):
            attr = getattr(obj, field)
            if callable(attr):
                return attr(obj)
            else:
                return unicode(attr)
        elif hasattr(self, field):
            attr = getattr(self, field)
            if callable(attr):
                attr(obj)
            else:
                return unicode(attr)
        else:
            func = getattr(self, 'get_%s' % field)
            return func(obj)
    