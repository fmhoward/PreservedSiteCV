import preservedsite.crossfolds as cv
import pandas as pd

data = pd.read_csv("example.csv", dtype=str)
data = cv.generate(data, "feature", ["A", "B"], crossfolds=3, patient_column='patient', site_column='site')