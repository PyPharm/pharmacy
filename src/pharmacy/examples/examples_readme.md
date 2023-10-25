<!--  
__version__ = 0.4.5
https://www.markdownguide.org/cheat-sheet/   
Remember that doctest wants a break after code examples or they will fail.
-->
# Pharmacy Python Examples
Here is a selection of code snippets useful in analyzing data from hospital, community and other pharmacy settings.
<br>Most of these examples utilize Pandas.   

## Intro
If you have not already installed the `pandas` library, go to the **terminal** and type `pip install pandas`.  
More detailed instructions for installing pandas can be found [here in the official pandas documentation](https://pandas.pydata.org/getting_started.html).
The examples here will teach pandas to a certain degree but if you are new to the pandas library, I strongly 
recommend that you work through the examples in [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#min).

## Cleaning Data
Pretend that the following table of data was exported from the Settings page of your pharmacy software.
<br>*Note that the 'schedule' column is a string rather than a pure integer number 
because of the 'c5' cell.*

| ndc           | description         | schedule |
|:--------------|:--------------------|----------|
| 10000-1000-10 | Acetaminophen 325mg |          |
| 20000-2000-30 | Lisinopril 10mg     | 7        |
| 30000-3000-30 | Tylenol #3          | c5       |

The code below creates this as a pandas 
[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html):   
```python
>>> import pandas as pd
>>> df = pd.DataFrame(
...     [('10000-1000-10','Acetaminophen 325mg',),
...     ('20000-2000-30','Lisinopril 10mg','7'),
...     ('30000-3000-30','Tylenol #3','c5'),
...      ], columns = ['ndc','description','schedule'])

```
Take a look at how the  DataFrame looks
```python
>>> print(df)
             ndc          description schedule
0  10000-1000-10  Acetaminophen 325mg     None
1  20000-2000-30      Lisinopril 10mg        7
2  30000-3000-30           Tylenol #3       c5

```
Next, let's clean the schedule column by creating a conversion dictionary called *converter*.
```python
>>> converter = {'7':7, '6':6, 'c5':5,'4':4,'c3':3,'c2':2,'n2':2}

```
Set the df.schedule column equal to a new column.  Apply the converter to the schedule column
<br>*Note that the individual 'schedule' column is being referenced as `df.schedule` - if there are no
spaces in the name of a column, it can be referenced using the dot after the DataFrame name.  A safer way
to reference a column is using brackets and putting the column name in quotations: `df['schedule']`*

```python
>>> df.schedule = df.schedule.map(converter)
>>> df
             ndc          description  schedule
0  10000-1000-10  Acetaminophen 325mg       NaN
1  20000-2000-30      Lisinopril 10mg       7.0
2  30000-3000-30           Tylenol #3       5.0

```
Hmm.  We want a clearly-described set of drug schedules but there is a value that says, 
'NaN' ('<u>N</u>ot <u>a</u> <u>N</u>umber', or `NULL` in SQL terms).  However, we know from our database that our
pharmacy software leaves out the drug schedule when items are OTC. 
Use [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html) to fill those.
```python
>>> df.schedule = df.schedule.fillna(7)
>>> df
             ndc          description  schedule
0  10000-1000-10  Acetaminophen 325mg       7.0
1  20000-2000-30      Lisinopril 10mg       7.0
2  30000-3000-30           Tylenol #3       5.0

```
One last nitpick: the `schedule` column is stored as `float` variables, signified by the '7.0' - to make it look
nice and clean let's convert that to a pure `int` (integer) type 
using [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html).
```python
>>> df.schedule = df.schedule.astype(int)
>>> df
             ndc          description  schedule
0  10000-1000-10  Acetaminophen 325mg         7
1  20000-2000-30      Lisinopril 10mg         7
2  30000-3000-30           Tylenol #3         5

```
Now the `schedule` column is pure integers. 
You can confirm with [`dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html).  Notice that
dtypes does _not_ use parenthesis.
```python
>>> df.dtypes
ndc            object
description    object
schedule        int32
dtype: object

```
Alternatively, you could have done this all in one line with method chaining as below.  Either of these two examples 
works:
```python
# Concise
>>> df.schedule = df.schedule.map(converter).fillna(7).astype(int)

```
```python
# Clear to read
>>> df.schedule = (df.schedule
...    .map(converter)
...    .fillna(7)
...    .astype(int))

```

