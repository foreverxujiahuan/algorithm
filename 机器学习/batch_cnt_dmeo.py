from math import ceil

request_data = [i for i in range(64)]
batch_size = 2

batch_cnt = ceil(len(request_data) / batch_size)
output_data = []
for i in range(batch_cnt):
    cur_request_data = request_data[i * batch_size: (i+1) * batch_size]
    output_data.append(cur_request_data)

for t in output_data:
    print(t)