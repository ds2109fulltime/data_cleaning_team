def download_csv(url):
    '''This Functions takes a URL with a CSV file and downloads it in the same folder the function is being run.
    The only required parameter is the URL itself'''
    import requests
    req = requests.get(url)
    url_content = req.content