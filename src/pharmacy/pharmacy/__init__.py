__version__ = '0.1.0'

import pandas as pd


# main location for pypharm objects

import re

# American NDC 1.02
# https://regexr.com/6083d
ndc_regex = '/(?<labeler_code>\d{1,6})(?:[-]*)(?<product_code>\d{1,4})(?:[-])(?<package_code>\d{1,2})|(?<labeler>\d{5})(?<product>\d{4})(?<package>\d{2})/gi'
#ndc_re_pattern = re.compile(ndc_regex)

def main():
    a = NDC('12345-1234-01')

    print(a)
    print(a.labeler)

class NDC:
    """
    1..

    :description: Intakes an individual NDC as a string then cleans it and makes various functions and properties available.

    """
    def __init__(self, ndc):
        self.ndc = str(ndc)
        self.ndc = self.ndc.replace('-','')

    def __repr__(self):
        return self.ndc

    def __str__(self):
        return self.ndc

    def __eq__(self, other):
        if self.ndc == other.ndc:
            return True
        else:
            return False

    @property
    def labeler(self):
        return self.ndc[0:5]


if __name__ == "__main__":
    main()