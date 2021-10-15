#  https://www.sentryds.com

from hashlib import md5
import configparser

import requests
from requests import Request, Session, HTTPError

url = 'https://secure.sentryds.com/api/reporter/'


def _open_config_file(config_file=None):
    if config_file == None:
        raise ValueError('Must supply valid config file.')
        # note: in future, make a function to create a template config file for user to fill in.
    else:
        config = configparser.ConfigParser()
        config.read(config_file)
    return config


def _make_md5(input: str):
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


def _query_string_from_params(params):
    base_request = Request("POST", url=url, params=params).prepare()
    query_string = base_request.url.split(sep='?')[1]
    return query_string


def request_report(config_file, verbose=False):
    config = _open_config_file(config_file)
    user_id = config['DEFAULT']['user']
    api_key = config['DEFAULT']['api_key']

    # Assemble the parameters
    params = dict(product='sentrex',
                  report='claims',
                  output='csv', # csv, psv, xls, json
                  qty_limit='5',
                  user_id=user_id)
    params_user = params.copy()
    params_user['key'] = api_key

    # Create the signature base string
    query_string = _query_string_from_params(params_user)
    hash = _make_md5(query_string)

    # Add signature to request
    params_signed = params.copy()
    params_signed['hash'] = hash
    if verbose:
        query_string_signed = _query_string_from_params(params_signed)
        print(f'Base:   {query_string}')
        print(f'Signed: {query_string_signed}')

    req = requests.post(url, params=params_signed)
    print(req.status_code)
    print(req.text)


def _main(config_file):
    request_report(config_file, verbose=True)


if __name__ == "__main__":
    _main(config_file='sentry_config.ini')
