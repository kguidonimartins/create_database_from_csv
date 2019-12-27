import numpy as np
import pandas as pd

for i in range(0, 3):
    df = pd.DataFrame(
        np.random.randint(0, 1000, size=(1000, 4)), 
        columns=list('ABCD')
        )
    df.to_csv('data/input/small_csv_0' + str(i) + '.csv')

huge_csv = pd.DataFrame(
    np.random.randint(0, 100000, size=(100000, 4)), 
    columns=list('ABCD')
    )

huge_csv.to_csv('data/input/huge_csv.csv')
