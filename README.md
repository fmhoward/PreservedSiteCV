# Preserved Site Cross Validation
Provides optimal stratification for deep learning on datasets with samples from multiple sites
<br>
<img src="https://github.com/fmhoward/PreservedSiteCV/blob/main/PreservedSitesCV.png?raw=true" width="600">
## Overview
Stratification can be performed by loading data from an annotations file into a DataFrame. Stratification can be performed with the following function:
```python
def generate(data, category, values, crossfolds = 3, target_column = 'CV3', patient_column = 'submitter_id', site_column = 'SITE', timelimit = 100):
    ''' Generates 3 site preserved cross folds with optimal stratification of category
    Input:
        data: dataframe with slides that must be split into crossfolds.
        category: the column in data to stratify by
        values: a list of possible values within category to include for stratification
        crossfolds: number of crossfolds to split data into
        target_column: name for target column to contain the assigned crossfolds for each patient in the output dataframe
        patient_column: column within dataframe indicating unique identifier for patient
        site_column: column within dataframe indicating designated site for a patient
        timelimit: maximum time to spend solving
    Output:
        dataframe with a new column, 'CV3' that contains values 1 - 3, indicating the assigned crossfold
    '''
```

## Example
Please see test.py for example use applied to the accompanying 'example.csv' data file. 
```python
import preservedsite.crossfolds as cv
import pandas as pd

data = pd.read_csv("example.csv", dtype=str)
data = cv.generate(data, "feature", ["A", "B"], crossfolds=3, patient_column='patient', site_column='site')
```

The resulting segregation of sites into crossfolds is printed as follows, with the appropriate assignment of patients to folds for cross validation appended to the dataframe.
```
Crossfold 1: A - 54 B - 250  Sites: ['Site 0', 'Site 4', 'Site 7', 'Site 8', 'Site 13', 'Site 14', 'Site 30', 'Site 33']
Crossfold 2: A - 54 B - 251  Sites: ['Site 1', 'Site 2', 'Site 3', 'Site 5', 'Site 6', 'Site 9', 'Site 15', 'Site 19', 'Site 20', 'Site 21', 'Site 22', 'Site 23', 'Site 25', 'Site 26', 'Site 27', 'Site 28', 'Site 29', 'Site 31', 'Site 32', 'Site 36']
Crossfold 3: A - 54 B - 250  Sites: ['Site 10', 'Site 11', 'Site 12', 'Site 16', 'Site 17', 'Site 18', 'Site 24', 'Site 34', 'Site 35', 'Site 37']
```


