import requests

# Set up mock requests using mocky.io - here the request returns an empty message
def fallback_response():
    print("Error during the payment, please try again.")


def good_mobile_to_user_api():
    r = requests.get('http://www.mocky.io/v2/5e1b2e2931000065004f3286')
    status_code = r.status_code

    if status_code == 200 :
        print(r.text)
    else:
        fallback_response()

good_mobile_to_user_api()


