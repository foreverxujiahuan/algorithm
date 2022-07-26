

def stable_batch(lengths, batch_size):
    lengths.sort()
    n = len(lengths)
    flags = [0 for _ in range(n)]
    final_batch = []
    cur_length_batch = []
    cur_target = 0
    i = 0
    while sum(flags) != n:
        for j in range(n-1, -1, -1):
            if flags[j] == 1:
                continue
            if cur_target + lengths[j] < batch_size:
                cur_length_batch.append(lengths[j])
                cur_target += lengths[j]
                flags[j] = 1
            elif cur_target + lengths[j] == batch_size:
                cur_length_batch.append(lengths[j])
                flags[j] = 1
                final_batch.append(cur_length_batch)
                cur_target = 0
                cur_length_batch = []
            else:
                while lengths[i] + cur_target <= batch_size and flags[i] != 1:
                    cur_target += lengths[i]
                    cur_length_batch.append(lengths[i])
                    flags[i] = 1
                    i += 1
                if lengths[i] + cur_target > batch_size:
                    cur_length_batch.append(lengths[i])
                    flags[i] = 1
                    final_batch.append(cur_length_batch)
    if cur_length_batch:
        final_batch.append(cur_length_batch)
    return final_batch


if __name__ == '__main__':
    lengths = [1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2]
    final_batch = stable_batch(lengths, batch_size=16)
    print(final_batch)

