# Preserved Site Cross Validation
Provides optimal stratification for deep learning on datasets with samples from multiple sites
<br>
<img src="https://github.com/fmhoward/PreservedSiteCV/blob/main/PreservedSitesCV.png?raw=true" width="600">
## Overview
Stratification can be performed by loading data from an annotations file into a DataFrame. Required column headers include 'SITE' representing the tissue submitting site for a sample, and 'submitter_id' representing a unique ID for each patient. Stratification can be performed with the following function:
```python
def preservedSite3FCV(data, category, values):
    ''' Generates 3 site preserved cross folds with optimal stratification of category

    Input:
        data: dataframe with slides that must be split into crossfolds.
        Must have a column 'SITE' representing the tissue submitting site
        Must have a column 'submitter_id' which must be unique for each patient

        category: the column in data to stratify by

        values: a list of possible values within category to include for stratification

    Output:
        dataframe with a new column, 'CV3' that contains values 1 - 3, indicating the assigned crossfold
    '''
```
