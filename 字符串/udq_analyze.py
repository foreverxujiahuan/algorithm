import pandas as pd

path = "/tmp/udq_data.txt"

output_data = []
enumature()
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        info = line.split("udq 信息: ")[1]
        info = eval(info)
        udq_data = info['udq_data']
        for samples in udq_data:
            for sample in samples['examples']:
                tmp = [info['user_id'], samples['id'], samples['desc'], sample['question']]
                output_data.append(tmp)

output_df = pd.DataFrame(output_data)
output_df.columns = ['user_id', 'udq_id', 'udq_name', 'sample']
output_df.to_csv("/tmp/udq_data.xlsx", index=False, encoding='utf_8_sig')

