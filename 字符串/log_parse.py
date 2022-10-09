import pandas as pd
path = "/Users/zzulixjh/Desktop/pingsheng.txt"

with open(path, 'r') as f:
    lines = f.readlines()
    text = lines[0]


_, info = text.split("udq 信息: ")
info = eval(info)
print(info.keys())
udq_data = info['udq_data']
print(udq_data)
print()
output_data = []
for d in udq_data:
    cur_id = d['id']
    cur_name = d['desc']
    cur_examples = d['examples']
    for example in cur_examples:
        t = [cur_id, cur_name, example['question']]
        output_data.append(t)

output_df = pd.DataFrame(output_data)
output_df.columns = ['id', 'name', 'example']
output_df.to_csv("/Users/zzulixjh/Desktop/品胜udq配置.csv", index=False, encoding='utf_8_sig')
