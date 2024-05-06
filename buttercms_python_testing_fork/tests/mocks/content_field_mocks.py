def list_content_fields_without_filtering():
    return {}

def list_filtered_content_fields(key1, key2):
    return {
        'data': {
            key1: [
                {
                    'meta': {
                        'id': 1,
                    }
                },
                {
                    'meta': {
                        'id': 2,
                    }
                }
            ],
            key2: [
                {
                    'meta': {
                        'id': 3,
                    }
                }
            ]
        }
    }

def list_non_existent_content_field(key):
    return {
        'detail': 'Content key %s not found' % key
    }

def get_content_field_without_filtering(field):
    return {
        'data': {
            field: [
                {
                    'meta': {
                        'id': 1,
                    }
                },
                {
                    'meta': {
                        'id': 2,
                    }
                }
            ]
        }
    }

def get_filtered_content_field(field, key):
    return {
        'data': {
            field: [
                {
                    'meta': {
                        'id': 1,
                    },
                    key: "example"
                }
            ]
        }
    }

def get_non_existent_content_field():
    return {
        'detail': 'Not found'
    }