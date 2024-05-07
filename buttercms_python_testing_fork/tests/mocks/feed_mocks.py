feed = '<?xml version=\"1.0\" encoding=\"UTF-8\"?><hello>World</hello>'

def get_sitemap_feed():
    return {
        'data': feed
    }

def get_rss_feed():
    return {
        'data': feed
    }

def get_atom_feed():
    return {
        'data': feed
    }

def get_non_existent_feed():
    return {
        'detail': 'Not found'
    }