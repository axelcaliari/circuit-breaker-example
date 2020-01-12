import requests

# Set up mock requests using mocky.io - here the request returns an empty message
def bad_mobile_to_user_api():
    r = requests.get('http://www.mocky.io/v2/5e1b2e2931000065004f3286')

    text = r.text

    # Post request treatment ...
    print(text)
    raise ValueError()


bad_mobile_to_user_api()