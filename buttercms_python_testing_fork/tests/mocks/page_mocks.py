def list_pages(page_type):
    return {
        'data': [
            {
                'slug': 'example',
                'name': 'Example Page',
                'page_type': page_type,
                'fields': [
                    {
                        'type': 'text',
                        'key': 'key1',
                    }
                ]
            },
            {
                'slug': 'example2',
                'name': 'Example Page 2',
                'page_type': page_type,
                'fields': [
                    {
                        'type': 'text',
                        'key': 'key2',
                    }
                ]
            }
        ]
    }

def list_pages_without_page_type():
    return {
        'data': [
            {
                'slug': 'example',
                'name': 'Example Page',
                'page_type': None,
                'fields': [
                    {
                        'type': 'text',
                        'key': 'key1',
                    }
                ]
            }
        ]
    }

def get_page(page_type, slug):
    return {
        'data': {
            'slug': slug,
            'name': 'Example Page',
            'page_type': page_type,
            'fields': [
                {
                    'type': 'text',
                    'key': 'key1',
                }
            ]
        }
    }

def get_non_existent_page():
    return {
        'detail': 'Not found'
    }

def search_pages(query):
    return {
        'data': [
            {
                'slug': 'example',
                'name': 'Example Page',
                'page_type': 'page_type',
                'fields': [
                    {
                        'type': 'text',
                        'key': query,
                    }
                ]
            }
        ]
    }