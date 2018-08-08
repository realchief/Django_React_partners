

def icon_name(name):
    return {
        'google-oauth': 'google',
        'google-oauth2': 'google',
    }.get(name, name)
