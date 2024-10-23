import re

def _get_item_url() -> str:
    return "|".join([
        "\"?https?://item.taobao.com/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://item.taobao.com/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://detail.tmall.com/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://detail.tmall.com/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://detail.tmall.hk/hk/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://detail.tmall.hk/hk/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://h5.m.taobao.com/awp/core/detail.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://h5.m.taobao.com/awp/core/detail.html?\\?.*id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?",
        "\"?https?://main.m.taobao.com/security-h5-detail/home\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*\"?"
    ])


def get_regex() -> str:
    item_url_regex = _get_item_url()
    json_url_regex = '\\{\"text\":\\{item_url_regex\\},\"jsview\":\\[\\{\"value\":\\{\"url\":\\{item_url_regex\\},\"name\":\\{item_url_regex\\},\"safe\":\"SAFE\"\\},\"type\":1\\}\\]\\}'
    json_url_regex = json_url_regex.replace("item_url_regex", item_url_regex)
    return _get_item_url() + "|" + json_url_regex


regex = get_regex()
print(regex)

url_text = '"https://item.taobao.com/item.htm?id=742782571740"'
url_regex = _get_item_url()

#
json_text = '{"text":"https://item.taobao.com/item.htm?id=742782571740","jsview":[{"value":{"url":"https://item.taobao.com/item.htm?id=742782571740","name":"https://item.taobao.com/item.htm?id=742782571740","safe":"SAFE"},"type":1}]}'

pattern = re.compile(regex)
ans = pattern.match(json_text)
print(len(json_text))
print(ans)
