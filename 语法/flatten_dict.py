# NER 嵌套实体
"""
The purpose of this function is to flatten a dictionary,
converting nested dictionaries into a flat list of key-value pairs,
excluding the key "features" if it exists.
"""

# 南京市长江大桥


def flat_dict(frame):
    # 返回这个嵌套字典中所有value为非ignored的健值对

    frame.pop("features", None)
    out = []  # [("a", 1)]
    for key, item in frame.items():
        if type(item) is dict:
            tmp = flat_dict(item)  # [("c", 2), ("e", 3)]
            out.extend(tmp)
        else:
            out.append((key, item))
    return out


frame = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "features": "ignored"
        }
    },
    "features": "ignored"
}

if __name__ == '__main__':
    ans = flat_dict(frame)
    print(ans)

