import pandas as pd

with open("/nas/data/siren/siren-corpus/tags/20230112V2/udq_config_data/20230112.csv", 'r') as f:
    lines = f.readlines()
    output_data = []
    for i, line in enumerate(lines):
        if i == 0:
            continue
        t1, t2, t3, t4 = line.split("\t")
        output_data.append([t1,t2,t3,t4[:-1]])
    output_df = pd.DataFrame(output_data)
    output_df.columns = ['user_id', 'udq_id', 'udq_name', 'sample']
    output_df.to_csv("/nas/tmp/udq_20230112.csv", index=False, encoding='utf_8_sig', sep='\t')


df = pd.read_csv("/nas/tmp/udq_20230112.csv", delimiter='\t')


with open("/nas/tmp/udq_20230112.csv", 'r') as f:
    lines = f.readlines()
    output_data = []
    for i, line in enumerate(lines):
        if line.count("\t") != 3:
            print(i, line)