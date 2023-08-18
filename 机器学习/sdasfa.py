import pandas as pd
input_path = "/Users/zzulixjh/Desktop/最最新降噪后20总故障总数据集.xlsx"
df = pd.read_excel(input_path)
output_data = []
cur = []
for _, row in df.iterrows():
    cur.append(row)
    if len(cur) == 10:
        output_data.append(cur)
        cur = []
if cur:
    output_data.append(cur)
from random import shuffle

shuffle(output_data)
final_output_data = []
for t in output_data:
    final_output_data.extend(t)
output_df.to_excel("/Users/zzulixjh/Desktop/按十个随机打乱.xlsx", index=False, encoding='utf_8_sig')