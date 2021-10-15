#  https://www.sentryds.com

from hashlib import md5
import configparser
from requests import Request, Session, HTTPError

url = 'https://secure.sentryds.com/api/reporter/'

def _open_config_file(config_file = None):
    if config_file == None:
        raise ValueError('Must supply valid config file.')
        #note: in future, make a function to create a template config file for user to fill in.
    else:
        config = configparser.ConfigParser()
        config.read(config_file)
    return config

def _make_md5(input:str):
    return md5(input.encode('utf-8')).hexdigest()

def _pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def request_report(config_file):

    config = _open_config_file(config_file)
    user_id = config['DEFAULT']['user']
    api_key = config['DEFAULT']['api_key']

    params = {
        'product':'sentrex'
        ,'report':'claims'
        ,'qty_limit':'5'
    }

    params_user = params.copy()
    params_user['user_id'] = user_id

    base_request = Request("POST",url=url, params=params_user).prepare()
    query_string = base_request.url.split(sep='?')[1]
    print(query_string)

def _main(config_file):
    request_report(config_file)


if __name__ == "__main__":
    _main(config_file='sentry_config.ini')