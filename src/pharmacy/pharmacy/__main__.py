__version__ = '0.3.4'

import requests

# This function written by ChatGPT3 on 2023-02-19   DRL
def check_ndc_in_database(ndc):
    """Check if NDC is present in the FDA NDC database"""
    ndc_url = f'https://api.fda.gov/drug/ndc.json?search=product_ndc:"{ndc}"&limit=1'
    response = requests.get(ndc_url)
    if response.status_code == 200:
        ndc_data = response.json()
        if ndc_data.get('results') and ndc_data['results'][0]['product_ndc'] == ndc:
            return True
    return False

def check_ndc_data(ndc):
    # DRL: per documentation, NDC has to have a hyphen in it.
    # Also, only the first 5-4 sequence is accepted.
    # Reference: https://open.fda.gov/apis/drug/ndc/searchable-fields/
    """Check if NDC is present in the FDA NDC database"""
    ndc_url = f'https://api.fda.gov/drug/ndc.json?search=product_ndc:"{ndc}"&limit=1'
    response = requests.get(ndc_url)
    if response.status_code == 200:
        ndc_data = response.json()

        if ndc_data.get('results') and ndc_data['results'][0]['product_ndc'] == ndc:
            return True
    else:
        print(response)
    return False


if __name__ == "__main__":

    check_ndc_data('81964-221-14')

    prozac = '00777-3105-02'
    prozac2 = '00777310502'
    check_ndc_data(prozac)