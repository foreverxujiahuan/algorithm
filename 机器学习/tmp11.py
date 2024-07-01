logits_infos = []
batch_cnt = len(logits_pred)
label_cnt = len(logits_pred[0])
for sample_index in range(batch_cnt):
    cur_logits_infos = []
    for label_index in range(label_cnt):
        for logit_info in logits_pred[sample_index][label_index]:
            start, end, logit_value = logit_info
            cur_logits_infos.append((label_index, start, end, logit_value))
    logits_infos.append(cur_logits_infos)