def list_posts():
    return {
        'data': [
            {
                'title': 'Title',
                'slug': 'title',
                'body': '<p>body</p>',
                'summary': 'body',
                'url': 'https://deployment/blog/title',
                'author': {
                    'slug': 'author',
                    'email': '',
                    'last_name': 'Test',
                    'first_name': 'Author',
                },
                'tags': [],
                'categories': []
            },
            {
                'title': 'Title 2',
                'slug': 'title-2',
                'body': '<p>body 2</p>',
                'summary': 'body 2',
                'url': 'https://deployment/blog/title-2',
                'author': {
                    'slug': 'author',
                    'email': '',
                    'last_name': 'Test',
                    'first_name': 'Author',
                },
                'tags': [],
                'categories': []
            }
        ]
    }

def list_posts_without_body():
    return {
        'data': [
            {
                'title': 'Title',
                'slug': 'title',
                'summary': 'body',
                'url': 'https://deployment/blog/title',
                'author': {
                    'slug': 'author',
                    'email': '',
                    'last_name': 'Test',
                    'first_name': 'Author',
                },
                'tags': [],
                'categories': []
            },
            {
                'title': 'Title 2',
                'slug': 'title-2',
                'summary': 'body 2',
                'url': 'https://deployment/blog/title-2',
                'author': {
                    'slug': 'author',
                    'email': '',
                    'last_name': 'Test',
                    'first_name': 'Author',
                },
                'tags': [],
                'categories': []
            }
        ]
    }

def get_post():
    return {
        'data': {
            'title': 'Title',
            'slug': 'title',
            'body': '<p>body</p>',
            'summary': 'body',
            'url': 'https://deployment/blog/title',
            'author': {
                'slug': 'author',
                'email': '',
                'last_name': 'Test',
                'first_name': 'Author',
            },
            'tags': [],
            'categories': []
        }
    }

def get_non_existent_post():
    return {
        'detail': 'Not found'
    }

def search_posts(query):
    return {
        'data': [
            {
                'title': 'Title',
                'slug': 'title',
                'body': '<p>body</p>',
                'summary': 'body',
                'body': 'body...%s' % query,
                'url': 'https://deployment/blog/title',
                'author': {
                    'slug': 'author',
                    'email': '',
                    'last_name': 'Test',
                    'first_name': 'Author',
                },
                'tags': [],
                'categories': []
            }
        ]
    }