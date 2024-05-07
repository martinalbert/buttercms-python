def list_categories():
    return {
        'data': [
            {
                'name': 'Category 1',
                'slug': 'category-1'
            },
            {
                'name': 'Category 2',
                'slug': 'category-2'
            }
        ]
    }

def list_categories_with_posts():
    return {
        'data': [
            {
                'name': 'Category 1',
                'slug': 'category-1',
                'recent_posts': [
                    {'title': 'Post 1', 'slug': 'post-1'},
                    {'title': 'Post 2', 'slug': 'post-2'}
                ]
            },
            {
                'name': 'Category 2',
                'slug': 'category-2',
                'recent_posts': [
                    {'title': 'Post 3', 'slug': 'post-3'},
                    {'title': 'Post 4', 'slug': 'post-4'}
                ]
            }
        ]
    }

def get_category():
    return {
        'data': {
            'name': 'Category 1',
            'slug': 'category-1'
        }
    }

def get_category_with_posts():
    return {
        'data': {
            'name': 'Category 1',
            'slug': 'category-1',
            'recent_posts': [
                {'title': 'Post 1', 'slug': 'post-1'},
                {'title': 'Post 2', 'slug': 'post-2'}
            ]
        }
    }