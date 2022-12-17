

def f(base_arr, test_arr):
    length = len(base_arr)
    err = 0
    for base, test in zip(base_arr, test_arr):
        err += (base - test) / base
    ans = err / length
    return ans


if __name__ == '__main__':
    base_bert = [5.8, 5.71, 0.71, 2.25, 30.37]

    # BERT_VOTE
    test_bert_vote = [5.6, 5.41, 0.67, 2.03, 29.44]
    bert_vote_score = f(base_bert, test_bert_vote)
    print("BERT_VOTE的相对提升为:{:.3}%".format(bert_vote_score * 100))
    # BERT_AVG
    test_bert_avg = [5.68, 5.53, 0.68, 2.03, 30.03]
    bert_avg_score = f(base_bert, test_bert_avg)
    print("BERT_AVG的相对提升为:{:.3}%".format(bert_avg_score * 100))
    # BERT_SE
    test_bert_se = [5.82, 5.59, 0.65, 2.19, 30.48]
    bert_se_score = f(base_bert, test_bert_se)
    print("BERT_SE的相对提升为:{:.3}%".format(bert_se_score * 100))
    # BERT_SDV
    test_bert_sdv = [5.35, 5.38, 0.68, 2.05, 29.88]
    bert_sdv_score = f(base_bert, test_bert_sdv)
    print("BERT_SDV的相对提升为:{:.3}%".format(bert_sdv_score * 100))
    # BERT_SDA
    test_bert_sda = [5.29, 5.29, 0.68, 2.04, 29.88]
    bert_sda_score = f(base_bert, test_bert_sda)
    print("BERT_SDA的相对提升为:{:.3}%".format(bert_sda_score * 100))
