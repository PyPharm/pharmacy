<!--  

https://www.markdownguide.org/cheat-sheet/   
-->
# Pharmacy Python Examples
Here is a selection of code snippets useful in analyzing data from hospital, community and other pharmacy settings.

Most of the examples utilize Pandas.


## Intro
If you have not already installed the `pandas` library, go to the **terminal** and type `pip install pandas`.  
More detailed instructions for installing pandas can be found [here in the official pandas documentation](https://pandas.pydata.org/getting_started.html).
The examples here will teach pandas to a certain degree but if you are new to the pandas library, I strongly 
recommend that you work through the examples in [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#min).

## Cleaning data
  
```
>>> import pandas as pd
>>> df = pd.DataFrame(
...     [('10000-1000-10','Acetaminophen 325mg','7'),
...     ('20000-2000-30','Lisinopril 10mg','7'),
...     ('30000-3000-30','Tylenol #3','c5'),
...      ], columns = ['ndc','description','schedule'])

```




