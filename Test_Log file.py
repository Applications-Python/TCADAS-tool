import shutil

import pandas as pd
import os
import re
from pprint import pprint


# def findfiles(path, regex):
#     regObj = re.compile(regex)
#     res = []
#     for root, dirs, fnames in os.walk(path):
#         for fname in fnames:
#             if regObj.match(fname):
#                 res.append(os.path.join(root, fname))
#     return res

# print(findfiles('.', r'beforeprogramwith(.*?)Width=(.*?)(V).*'))

output1 = 'beforeprogramwith0.1Width=0.0656(V)'
directory = r'C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1\Simulation with set width = 0.1 Length = 0.066'

file_pth = f'{output1}.log'

# for file_pth in file_pths:
log_df = pd.read_csv(file_pth, skiprows=20, sep=' ', header=None)
use_cols = [
    "cgate1", "cgate2", "cgate3",
    "fgate1", "fgate2", "fgate3",
    "source1", "source2", "source3",
    "drain1", "drain2", "drain3",
    "substrate1", "substrate2", "substrate3"
]
log_df.columns = ["r1",
                  *use_cols,
                  "r2"]

log_df = log_df[[
    *use_cols
]]

log_df.to_csv(f'./{file_pth[:-4]}.csv', index=False)
results = f'{file_pth[:-4]}.csv'
shutil.copy(results,directory)
# pprint(log_df)
