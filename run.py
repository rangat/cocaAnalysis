import loadJSON
import json_csv
import collect_dataset

loadJSON.run()
json_csv.run()
collect_dataset.run()
json_csv.json_to_csv("edited/coca_data.json")