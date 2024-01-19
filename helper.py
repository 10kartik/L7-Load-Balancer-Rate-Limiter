from urllib.parse import urlparse

def sanitize_urls(urls):
    sanitized_urls = []
    for url in urls:
        try:
            url = urlparse(url)
            if url.scheme not in ['http', 'https']:
                raise ValueError('Invalid URL scheme')
            if not url.netloc:
                raise ValueError('Invalid URL')
            sanitized_urls.append(url.geturl())
        except ValueError as e:
            print('Invalid url: {}'.format(url.geturl()))
            raise e
    return sanitized_urls