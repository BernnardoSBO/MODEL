import fpgrowth_py as fp
import pandas as pd
import pickle
import datetime
import sys
import time
from urllib.error import HTTPError, URLError
import ssl



# file_path = "/app/data/file.txt"

# with open("/app/data/output.txt", "w+") as file:
#     file.write(f"the url is {sys.argv[1]}")


if len(sys.argv) < 2:
    print("ERROR: DATASET URL NOT GIVEN\nusage: $python main.py <DATASET_URL>", file=sys.stderr)
    exit(1)
csv_file_path = sys.argv[1]

ssl._create_default_https_context = ssl._create_unverified_context

try:
    df = pd.read_csv(csv_file_path)
except (HTTPError, URLError) as e:
    print(f"ERROR: {e}", file=sys.stderr)
    exit(1)
except Exception as e:
    print(f"Not treated exception: {e}", file=sys.sterr)
    exit(1)
    

# if len(sys.argv) == 2:
#     print(sys.argv[1])
#     with open("/data/output.txt") as file:
#         file.write(sys.argv[1])
#     time.sleep(1020)
    


# # read csv
# csv_file_path = './data/2023_spotify_ds1.csv'

# df = pd.read_csv(csv_file_path, sep=',', header=0)

# # create transactions
# transactions = []
# for index, row in df.iterrows():
#     transactions.append(row['songs'].split(','))

# # create model
# minSupRatio = 0.01
# minConf = 0.5

# model = fp.fpgrowth(transactions, minSupRatio, minConf)

# # version and model_date
# model.version = 'v1'
# model.model_date = datetime.datetime.now().strftime("%d/%m/%Y")

# # save model
# model_file_path = './model.pkl'

# with open(model_file_path, 'wb') as file:
#     pickle.dump(model, file)
