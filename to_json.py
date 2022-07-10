import json
from create_dataset import dataset, json_archive


# This is where you create a json file
with open(json_archive, 'w') as archive:
    archive.write("[")
    for index, data in enumerate(dataset):
        archive.write(json.dumps(data, indent=4))
        if not index == len(dataset) - 1:
            archive.write(",\n")
    archive.write("]")
