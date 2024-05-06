def list_tags():
    return {
        'data': [
            {
                'name': 'Example Tag',
                'slug': 'example-tag'
            },
            {
                'name': 'Example Tag 2',
                'slug': 'example-tag-2'
            }
        ]
    }

def list_tags_with_recent_posts():
    return {
        'data': [
            {
                'name': 'Example Tag',
                'slug': 'example-tag',
                'recent_posts': [
                    {'title': 'Post 1', 'slug': 'post-1'},
                    {'title': 'Post 2', 'slug': 'post-2'}
                ]
            },
            {
                'name': 'Example Tag 2',
                'slug': 'example-tag-2',
                'recent_posts': [
                    {'title': 'Post 3', 'slug': 'post-3'},
                    {'title': 'Post 4', 'slug': 'post-4'}
                ]
            }
        ]
    }

def get_tag():
    return {
        'data': {
            'name': 'Example Tag',
            'slug': 'example-tag'
        }
    }

def get_tag_with_recent_posts():
    return {
        'data': {
            'name': 'Example Tag',
            'slug': 'example-tag',
            'recent_posts': [
                {'title': 'Post 1', 'slug': 'post-1'},
                {'title': 'Post 2', 'slug': 'post-2'}
            ]
        }
    }

def get_non_existent_tag():
    return {
        'detail': 'Not found'
    }