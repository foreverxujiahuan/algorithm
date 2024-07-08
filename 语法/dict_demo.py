

from collections import defaultdict

sdq_pos_config = defaultdict(dict)

sample = "你好"

sdq_pos_config['2'][sample] = {1,2,3}
print(sdq_pos_config)