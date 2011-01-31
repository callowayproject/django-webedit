"""
The WordPress xml-rpc api implementation
"""
from django_xmlrpc.decortors import xmlrpc_method

@xmlrpc_method(
    returns='[{boolean isAdmin, string url, string blogid, string blogName, string xmlrpc}]',
    args=[str, str],
    name='wp.getUsersBlogs')
def get_users_blogs(username, password):
    """
    Return the user's blogs
    """
    pass


@xmlrpc_method(
    returns='[{int tag_id, string name, int count, string slug, string html_url, string rss_url}]',
    args=[int, str, str],
    name='wp.getTags')
def get_tags(blog_id, username, password):
    """
    Get list of all tags.
    """
    pass


@xmlrpc_method(
    returns='[{int approved, int awaiting_moderation, int spam, int total_comments}]',
    args=[int, str, str, int],
    name='wp.getCommentCount')
def get_comment_count(blog_id, username, password, post_id):
    """
    Retrieve comment count for a specific post.
    """
    pass

@xmlrpc_method(
    returns='[str, str, ...]',
    args=[int, str, str],
    name='wp.getPostStatusList')
def get_post_status_list(blog_id, username, password):
    """
    Retrieve post statuses
    """
    pass

@xmlrpc_method(
    returns='[str, str, ...]',
    args=[int, str, str],
    name='wp.getPageStatusList')
def get_page_status_list(blog_id, username, password):
    """
    Retrieve all of the WordPress supported page statuses
    """
    pass

@xmlrpc_method(
    returns='[{string name, string description}]',
    args=[int, str, str],
    name='wp.getPageTemplates')
def get_page_templates(blog_id, username, password):
    """
    Retrieve page templates
    """
    pass

@xmlrpc_method(
    returns='[{string option, string value}]',
    args=[int, str, str, [str,]]
    name='wp.getOptions')
def get_options(blog_id, username, password, options):
    """
    Retrieve blog options. 
    If passing in an array, search for options listed within it.
    """
    pass

@xmlrpc_method(
    returns='[{string option, string value}]',
    args=[int, str, str, '[{str, str}',]]
    name='wp.setOptions')
def set_options(blog_id, username, password, options):
    """
    Update blog options. Returns array of structs showing updated values
    """
    pass

@xmlrpc_method(
    returns='boolean status',
    args=[int, str, str, int],
    name='wp.deleteComment')
def delete_comment(blog_id, username, password, comment_id):
    """
    Remove a comment
    """
    pass

@xmlrpc_method(
    returns='boolean status',
    args=[int, str, str, int, '{str, date, str, str, str, str}'],
    name='wp.editComment')
def edit_comment(blog_id, username, password, comment_id, comment):
    """
    Edit a comment
    """
    pass

@xmlrpc_method(
    returns='int comment_id',
    args=[int, str, str, int, '{str, date, str, str, str, str}'],
    name='wp.newComment')
def new_comment(blog_id, username, password, post_id, comment):
    """
    Create a new comment
    """
    pass

@xmlrpc_method(
    returns='{string hold, string approve, string spam}',
    args=[int, str, str],
    name='wp.getCommentStatusList')
def get_comment_status_list(blog_id, username, password):
    """
    Retrieve the names for the hold, approve and spam comment statuses
    """
    pass

@xmlrpc_method(
    returns="""{
        datetime dateCreated (ISO.8601)
        int userid
        int page_id
        str page_status
        str description
        str title
        str link
        str permaLink
        list categories
            str Category Name
            ...
        str excerpt
        str text_more
        int mt_allow_comments
        int mt_allow_pings
        str wp_slug
        str wp_password
        str wp_author
        int wp_page_parent_id
        str wp_page_parent_title
        int wp_page_order
        int wp_author_id
        str wp_author_display_name
        datetime date_created_gmt
        list custom_fields
            {string id, string key, string value}
            ...
        string wp_page_template
    }""",
    args=[int, int, str, str],
    name="wp.getPage")
def get_page(blog_id, page_id, username, password):
    """
    Get the page identified by the page id.
    """
    pass

@xmlrpc_method(
    returns="[same as wp.getPage,]",
    args=[int, str, str],
    name="wp.getPages")
def get_pages(blog_id, username, password):
    """
    Get an array of all the pages on a blog.
    """
    pass

@xmlrpc_method(
    returns="[{int page_id, str page_title, int page_parent_id, datetime dateCreate},]"
    args=[int, str, str],
    name="wp.getPageList")
def get_page_list(blog_id, username, password):
    """
    Get an array of all the pages on a blog. Just the minimum details, lighter than wp.getPages.
    """
    pass

@xmlrpc_method(
    returns="int page_id",
    args=[int, str, str, '{str, str, int, int, int, str, str, str, str, int, int, datetime, [{str, str, str}]}', bool],
    name="wp.newPage")
def new_page(blog_id, username, password):
    """
    Create a new page. Similar to metaWeblog.newPost.
    """
    pass

wp.deletePage
wp.editPage
wp.getAuthors
wp.getCategories
wp.newCategory
wp.deleteCategory
wp.suggestCategories
wp.uploadFile
wp.getComment
wp.getComments
