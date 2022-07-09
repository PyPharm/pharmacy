
import pandas as pd
import random

"""

impact of social determinants of health on medication adherence:
https://pubmed.ncbi.nlm.nih.gov/33515188/
    food insecurity  (aOR = 0.56; 95% CI 0.42-0.7)
    housing instability (aOR = 0.64; 95% CI 0.44-0.93)
    social determinants overall (aOR = 0.75; 95% CI 0.65-0.88) 
    
Social Risk Factors for Medication Nonadherence: Findings from the CARDIA Study
https://pubmed.ncbi.nlm.nih.gov/32019655/
    income <$25,000 (OR = 2.37 [95% CI 1.12-4.98], p < .05)
    high chronic stress (OR = 2.07 [95% CI 1.09-3.94], p < .05) 
    Individuals with ≥3 social risk factors had >3 times higher odds of nonadherence than 
        counterparts with no social risk factors (OR = 3.26 [95% CI 1.72-6.19], p < .001)

"""
# factor dictionaries from CARDIA
# in each subcategory, the % is the "% of (adherent or nonadherent) people who were in this bucket"
FACTORS = {
    'education':
        {
            'adherent': {'high school':.223,'some college':.273,'college graduate':.505}
            ,'nonadherent': {'high school':.310,'some college':.310,'college graduate':.381}
        }
    ,'income':
        {
            'adherent': {'<25000':.144, '25000-49999':.184, '50000-74999':.187, '>75000':.485}
            ,'nonadherent': {'<25000':.283, '25000-49999':.248, '50000-74999':.212, '>75000':.257}
        }
    ,'financial strain':
        {

            'adherent':{'no hardship':.849, 'hardship':.151}
            ,'nonadherent':{'no hardship':.779, 'hardship':.221}
        }
    ,'chronic stress':
        {
            'adherent':{'q1':.258, 'q2':.261, 'q3':.248, 'q4':.233}
            ,'nonadherent': {'q1': .168, 'q2': .186, 'q3': .186, 'q4': .460}
        }
    ,'social support':
        {
            'adherent':{'q1':.202, 'q2':.258, 'q3':.210, 'q4':.330}
            ,'nonadherent':{'q1':.416, 'q2':.186, 'q3':.133, 'q4':.265}
        }
    ,'social strain':
        {
            'adherent':{'q1':.247, 'q2':.232, 'q3':.252, 'q4':.269}
            ,'nonadherent':{'q1':.195, 'q2':.204, 'q3':.195, 'q4':.407}
        }
}

LASTNAMES_FILE = 'fake_lastnames.txt'
with open(LASTNAMES_FILE, 'r') as f:
    LASTNAMES = f.read().splitlines()
LASTNAMES = set(LASTNAMES)

print(LASTNAMES)

print(FACTORS['social strain']['adherent'])

print(__file__)