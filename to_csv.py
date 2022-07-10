import pandas as pd
from create_dataset import dataset, csv_archive


# This is where you create a json file
dataframe = pd.DataFrame.from_dict(dataset)
dataframe.to_csv(csv_archive, index=False, header=True)