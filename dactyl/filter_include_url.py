#!/usr/bin/env python3

# Import the main library
import requests
# import special error handling
from requests.exceptions import HTTPError

# Define source url and transformation vars
url = ''
url_content = ''
url_string = ''


def include_url(filter_url):

    try:
        r = requests.get(
            filter_url, headers={'Accept': 'application/vnd.github.v3.raw'})

        # If the response was successful, no Exception will be raised
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Successful response')
    #url_content = r.content
    url_content = str(r.content, 'UTF-8')
    return(url_content)


print(url_content)

export = {
    "include_url": include_url
}


