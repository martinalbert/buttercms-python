def list_authors():
    return {
        'data': [
            {
                'first_name': 'John', 
                'last_name': 'Doe', 
                'slug': 'john-doe'
            },
            {
                'first_name': 'Jane', 
                'last_name': 'Doe', 
                'slug': 'jane-doe'
            }
        ]
    }

def list_authors_with_posts():
    return {
        'data': [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'slug': 'john-doe',
                'recent_posts': [
                    {'title': 'Post 1', 'slug': 'post-1'},
                    {'title': 'Post 2', 'slug': 'post-2'}
                ]
            },
            {
                'first_name': 'Jane',
                'last_name': 'Doe',
                'slug': 'jane-doe',
                'recent_posts': [
                    {'title': 'Post 3', 'slug': 'post-3'},
                    {'title': 'Post 4', 'slug': 'post-4'}
                ]
            }
        ]
    }

def get_author():
    return {
        'data': {
            'first_name': 'John', 
            'last_name': 'Doe', 
            'slug': 'john-doe'
        }
    }

def get_author_with_posts():
    return {
        'data': {
            'first_name': 'John',
            'last_name': 'Doe',
            'slug': 'john-doe',
            'recent_posts': [
                {'title': 'Post 1', 'slug': 'post-1'},
                {'title': 'Post 2', 'slug': 'post-2'}
            ]
        }
    }