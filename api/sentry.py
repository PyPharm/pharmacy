#  https://www.sentryds.com

from hashlib import md5
import configparser
import urllib

import requests
from requests import Request, Session, HTTPError

#url = 'https://secure.sentryds.com/api/reporter/'
#url = 'https://httpbin.org/post'
url = 'https://secure.sentryds.com/api/reporter/?product=sentrex&report=claim&output=csv&user_id=4435&contract_ids=20577&qty_limit=5&drug_type=all_brands&hash=25c5350cf1bf1a76b4cd11b816170d5a'

def _open_config_file(config_file=None):
    if config_file == None:
        raise ValueError('Must supply valid config file.')
        # note: in future, make a function to create a template config file for user to fill in.
    else:
        config = configparser.ConfigParser()
        config.read(config_file)
    return config


def _make_md5(input: str, verbose = False):
    md5_str = md5(input.encode('utf-8')).hexdigest()
    if verbose:
        print(f'md5_str: {md5_str}')
    return md5_str


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
    #base_request = Request("POST", url=url, params=params).prepare()
    #query_string = base_request.url.split(sep='?')[1]
    print(params)
    query_string = urllib.parse.urlencode(params, safe='$:+')
    print(f'quer_string: {query_string}')
    return query_string


def request_report(config_file, verbose=False):
    config = _open_config_file(config_file)
    user_id = config['DEFAULT']['user']
    api_key = config['DEFAULT']['api_key']

    # Assemble the parameters
    params = dict(

        product='sentrex',
        contract_ids= '20577',
        report='claims',
        output='csv', # csv, psv, xls, json
        qty_limit='5',
        drug_type='all_brands',
        user_id = user_id
        )
    params_user = params.copy()
    params_user['key'] = api_key

    # Create the signature base string
    query_string = _query_string_from_params(params_user)
    hash = _make_md5(query_string, verbose=verbose)

    # Add signature to request
    params_signed = params.copy()
    params_signed['hash'] = hash
    print(f'params going to payload: {str(params_signed)}')
    if verbose:
        query_string_signed = _query_string_from_params(params_signed)
        print(f'Base:   {query_string}')
        print(f'Signed: {query_string_signed}')

    payload_str = urllib.parse.urlencode(params_signed, safe=':+')  #TODO:change
    #todo: remove the override
    payload_override = 'product=sentrex&' \
                       'report=claim&' \
                       'output=csv&' \
                       'user_id=4435&' \
                       'contract_ids=20577&qty_limit=5&drug_type=all_brands&hash=25c5350cf1bf1a76b4cd11b816170d5a'

    print(payload_override)

    #req = requests.post(url, params=payload_override)
    req = requests.post(url)
    print(req.status_code)
    print(req.text)


def _main(config_file):
    request_report(config_file, verbose=True)


if __name__ == "__main__":
    _main(config_file='sentry_config.ini')
