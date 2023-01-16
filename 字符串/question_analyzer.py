import pandas as pd

path = "/home/log/dev/siren_nlu_8857.log"
output_data = []

with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "的疑问程度为" in line:
            line = line.split("INFO - ")[1]
            if line.count(":") == 2:
                t1, t2, score = line.split(":")
                score = score.replace('"', "").replace("\n", "")
                text = t2.replace("的疑问程度为", "")
                output_data.append([text, score])
            else:
                print(line)

output_df = pd.DataFrame(output_data)

output_df.to_csv("/nas/home/xujiahuan/data/udq/udq_question.csv", index=False, encoding='utf_8_sig')

