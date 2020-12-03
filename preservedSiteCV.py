import pandas as pd
import numpy as np
import cvxpy as cp
import cplex

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

    submitters = data['submitter_id'].unique()
    newData = pd.DataFrame(submitters, columns=['submitter_id'])
    newData2 = data[['submitter_id', category, 'SITE']]
    newData3 = pd.merge(newData, newData2, on='submitter_id', how='left')
    newData3.drop_duplicates(inplace=True)
    uniqueSites = newData2['SITE'].unique()
    n = len(uniqueSites)
    listSet = []
    for v in values:
        listOrder = []
        for s in uniqueSites:
            listOrder += [len(newData3[(newData3.SITE == s) & (newData3[category] == v)].index)]
        listSet += [listOrder]

    g1 = cp.Variable(n, boolean=True)
    g2 = cp.Variable(n, boolean=True)
    g3 = cp.Variable(n, boolean=True)
    A = np.ones(n)
    constraints = [g1 + g2 + g3 == A]
    error = ""
    for v in range(len(values)):
        if v == 0:
            error = cp.square(cp.sum(3*cp.multiply(g1, listSet[0])) - sum(listSet[0])) + cp.square(cp.sum(3*cp.multiply(g2, listSet[0])) - sum(listSet[0])) + cp.square(cp.sum(3*cp.multiply(g3, listSet[0])) - sum(listSet[0]))
        else:
            error += cp.square(cp.sum(3 * cp.multiply(g1, listSet[v])) - sum(listSet[v])) + cp.square(
                cp.sum(3 * cp.multiply(g2, listSet[v])) - sum(listSet[v])) + cp.square(
                cp.sum(3 * cp.multiply(g3, listSet[v])) - sum(listSet[v]))
    prob = cp.Problem(cp.Minimize(error), constraints)


    prob.solve(solver='CPLEX', cplex_params={"timelimit": 100})
    g1gs = []
    g2gs = []
    g3gs = []
    for i in range(n):
        if g1.value[i] == 1:
            g1gs += [uniqueSites[i]]
        if g2.value[i] == 1:
            g2gs += [uniqueSites[i]]
        if g3.value[i] == 1:
            g3gs += [uniqueSites[i]]
    cvs = "CV3"
    bins = pd.DataFrame()
    ds1 = newData3[newData3.SITE.isin(g1gs)]
    ds1[cvs] = str(1)
    ds2 = newData3[newData3.SITE.isin(g2gs)]
    ds2[cvs] = str(2)
    ds3 = newData3[newData3.SITE.isin(g3gs)]
    ds3[cvs] = str(3)
    bins = bins.append(ds1)
    bins = bins.append(ds2)
    bins = bins.append(ds3)
    return pd.merge(data, bins[['submitter_id', cvs]], on='submitter_id', how='left')
