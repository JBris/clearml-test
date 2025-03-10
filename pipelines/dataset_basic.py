# create example dataset
from clearml import StorageManager, Dataset

# Download sample csv file
csv_file = StorageManager.get_local_copy(
    remote_url="https://vincentarelbundock.github.io/Rdatasets/csv/AER/Affairs.csv"
)

# Create a dataset with ClearML`s Dataset class
dataset = Dataset.create(
    dataset_project="DatasetProject", dataset_name="HelloDataset"
)

# add the example csv
dataset.add_files(path=csv_file)

# Upload dataset to ClearML server (customizable)
dataset.upload()

# commit dataset changes
dataset.finalize()