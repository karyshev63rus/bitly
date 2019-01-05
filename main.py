from dotenv import load_dotenv
load_dotenv()
import requests
import os
import argparse

def create_arg_link():
    """It takes an arg to create a link."""
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    arg = parser.parse_args()
    return arg.link

def request_short_link(link_name):
    """It requests short link."""
    link_data = {
        'long_url': link_name
            }
    response_short_link = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=api_headers,
    json = link_data)
    return response_short_link

def create_short_link(response_short_link):
    """It creates short link."""
    try:
        short_link = response_short_link.json()['link']
        return short_link
    except KeyError:
        return

def request_clicks(link_name):
    """It requests count of clicks."""
    click_data = {
        'unit': 'month',
            }
    count_click_response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.
    format(link_name), headers=api_headers, params = click_data)
    return count_click_response

def summary_clicks(count_click_response):
    """It summarizes clicks."""
    try:
        count_clicks = count_click_response.json()['total_clicks']
        return count_clicks
    except KeyError:
        return

if __name__ == '__main__':
    TOKEN = os.getenv('TOKEN')
    api_headers = {
        'Authorization': 'Bearer ' + str(TOKEN)
            }

    link_name = create_arg_link()
    response_short_link = request_short_link(link_name)
    if response_short_link:
        short_link = create_short_link(response_short_link)
        print(short_link)
    else:
        count_click_response = request_clicks(link_name)
        count_clicks = summary_clicks(count_click_response)
        print(count_clicks)
