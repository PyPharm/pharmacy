__version__ = '0.2.1'

import pandas as pd
import warnings


# main location for pypharm objects

import re

# American NDC 1.02
# https://regexr.com/6083d
ndc_regex = '/(?<labeler_code>\d{1,6})(?:[-]*)(?<product_code>\d{1,4})(?:[-])(?<package_code>\d{1,2})|(?<labeler>\d{5})(?<product>\d{4})(?<package>\d{2})/gi'
#ndc_re_pattern = re.compile(ndc_regex)

def main():

    a = NDC('1231-3020-20')
    b = NDC('1231-3020-20')
    print(a == b)
    print(int(a))

    # todo: move these into unit unit_tests
    good_ndcs = [
        '12345-1234-01',    # 5-4-2
        '1234-1234-01',     # 4-4-2
        '12345-123-01',     # 5-3-2
        '12345-1234-1',     # 5-4-1
        '123456-123-01',    # 6-3-2
        '123456-1234-0',    # 6-4-1
        '12345123401',      # 11 digit string
        92345123401,        # 11 digit integer
        #2345123401,         # 10 digit integer        #todo: think hard about this.  Should it be assumed that an overly
                                                    #short NDC where 0s are cut out is actually correct?
        {'mfg': 12345,
         'product': 1234,
         'pkg': 10
         },                 # dictionary of integers with correct labels
        {'mfg': '12345',
         'product': '1234',
         'pkg': '10'
         }                  # dictionary of strings with correct labels
    ]

    #todo: move these into unit unit_tests
    ugly_ndcs = [
        12345678901,
        123,
        'asdsf-fsdf-sf',
        'aasdfasdfas',
        'asdf',
        '123-456-78',
        '0123a-0456-78',
        '01234-5678-90',
        '0123-45678-90',
        '0123-4567-890'
    ]

    for good_ndc in good_ndcs:
        n = NDC(good_ndc)
        print(f'Original NDC: {n._ndc_input} \tTransformed: {n.ndc_simple}')

    for ugly_ndc in ugly_ndcs:
        print(NDC(ugly_ndc).ndc_simple)



class NDC:
    """
    1..
    :description: Intakes an individual NDC as a string then cleans it and makes various functions and properties available.
    """
    def __init__(self, ndc):
        self._ndc_input = ndc
        # ndcd = ndc dictionary
        self.ndcd = self.clean_ndc(ndc)
        assert type(self.ndcd) == dict
        self.ndc_simple = self.ndcd['mfg'] + self.ndcd['product'] + self.ndcd['pkg']

    def __repr__(self):
        return self.ndc_simple

    def __str__(self):
        return self.ndc_simple

    def __int__(self):
        return int(self.ndc_simple)

    def __eq__(self, other):
        return self.ndc_simple == other.ndc_simple           # todo: test this.

    def __len__(self):
        return len(self.ndc_simple)

    def __contains__(self, item):
        return item in self.ndc_simple

    # ------------------------------------------------------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------------------------------------------------------
    # synonyms of "manufacturer"
    @property
    def mfg(self):
        return self.ndcd['mfg']
    @property
    def manufacturer(self):
        return self.ndcd['mfg']
    @property
    def labeler(self):
        return self.ndcd['mfg']

    @property
    def product(self):
        return self.ndcd['product']

    # synonyms of "package"
    @property
    def pkg(self):
        return self.ndcd['pkg']
    @property
    def package(self):
        return self.ndcd['pkg']

    @property
    def dashed(self):
        return self.ndcd['mfg'] + '-' + self.ndcd['product'] + '-' + self.ndcd['pkg']

    # ------------------------------------------------------------------------------------------------------------------
    # Methods
    # ------------------------------------------------------------------------------------------------------------------

    def clean_ndc(self, ndc):
        """

        :param ndc:
        :return: dictionary of values: mfg, product, pkg and simple
        *simple* is the 11-digit string
        """

        """
        Each path will depend on the type entered.
        the sub-parts will return dictionaries of mfg, product and pkg
        As a last step, *simple* is created. 
        
        """

        if type(ndc) == str:
            # Test characters to ensure they are numerals
            if not ndc.replace('-','').isnumeric():
                raise TypeError(f'NDC {ndc} is a string but contains non-numeric characters.')

            # first deal with dashed ndcs
            if ndc.count('-') == 2:
                return self.clean_dashed_ndc(ndc)

            else:
                return self._11string_to_ndc_dict(ndc)
        elif type(ndc) == int:
            # todo: flag to allow shorter-than-11-digit NDCS
            if len(str(ndc)) == 11:
                return self._11string_to_ndc_dict(str(ndc))

        else:
            raise TypeError(f'NDC {ndc} is not recognized as a compatible NDC format.  It is type: {type(ndc)}')


    def clean_dashed_ndc(self, ndc:str):
        #only 2 dashes has already been confirmed
        ndc_list = ndc.split('-')
        ndc_dict = {'mfg':ndc_list[0],
                    'product':ndc_list[1],
                    'pkg':ndc_list[2]}

        #TODO: check lengths of each part

        # 5-4-2
        if len(ndc_dict['mfg']) == 5 and len(ndc_dict['product']) == 4 and len(ndc_dict['pkg']) == 2:
            return ndc_dict
        # 5-3-2
        elif len(ndc_dict['mfg']) == 5 and len(ndc_dict['product']) == 3 and len(ndc_dict['pkg']) == 2:
            ndc_dict['product'] = ndc_dict['product'].zfill(4)
            return ndc_dict
        # 5-4-1
        elif len(ndc_dict['mfg']) == 5 and len(ndc_dict['product']) == 4 and len(ndc_dict['pkg']) == 1:
            ndc_dict['pkg'] = ndc_dict['pkg'].zfill(2)
            return ndc_dict
        # 4-4-2
        elif len(ndc_dict['mfg']) == 4 and len(ndc_dict['product']) == 4 and len(ndc_dict['pkg']) == 2:
            ndc_dict['mfg'] = ndc_dict['mfg'].zfill(5)
            return ndc_dict
        # 6-3-2
        elif len(ndc_dict['mfg']) == 6 and len(ndc_dict['product']) == 3 and len(ndc_dict['pkg']) == 2:
            # hopefully this is ok.  Not sure if a transition to 5-4-2 is somehow needed.
            return ndc_dict
        # 6-4-1
        elif len(ndc_dict['mfg']) == 6 and len(ndc_dict['product']) == 4 and len(ndc_dict['pkg']) == 1:
            # hopefully this is ok.  Not sure if a transition to 5-4-2 is somehow needed.
            return ndc_dict
        else:
            raise TypeError(f'The lengths of segments in {ndc} is not compatible with NDC format.')

    def _11string_to_ndc_dict(self, ndc):
        # Test length
        if len(ndc) == 11:
            ndc_dict = {'mfg': ndc[0:5],
                        'product': ndc[5:9],
                        'pkg': ndc[9:]
                        }
            return ndc_dict
        else:
            raise TypeError(f'NDC {ndc} length of {len(ndc)} is insufficient.')

        return ndc_dict





        # 11 digit string
        # 11 digit .. ?



        raise FutureWarning(f'Program This.  Clean dashed NDC {ndc}.')



if __name__ == "__main__":
    main()