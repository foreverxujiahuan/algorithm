import pandas as pd

file_path1 = "*"
file_path2 = "*"


component2times = dict()


def process(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "time_cost" in line:
                info = line.split("#component")[-1]
                component, cost_time = info.split("#time_cost:")
                cost_time = float(cost_time)
                component2times.setdefault(component, []).append(cost_time)


process(file_path1)
process(file_path2)
output_data = []
for component, times in component2times.items():
    ave_time = sum(times) / len(times)
    output_data.append([component, ave_time])

output_df = pd.DataFrame(output_data)
output_df.columns = ["component", "平均耗时"]
output_df.to_csv("/home/darcy/component_cost_time.csv", index=False, encoding='utf_8_sig')
