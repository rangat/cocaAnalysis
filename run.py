import loadJSON
import json_csv
import collect_dataset

import time
start = time.time()

loadJSON.run()
json_csv.run()
collect_dataset.run()
json_csv.json_to_csv("edited/coca_data.json")

end = time.time()
print(end - start)
