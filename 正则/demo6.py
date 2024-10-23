import re

def _get_item_url() -> str:
    return "|".join([
        "https?://item.taobao.com/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://item.taobao.com/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://detail.tmall.com/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://detail.tmall.com/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://detail.tmall.hk/hk/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://detail.tmall.hk/hk/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://h5.m.taobao.com/awp/core/detail.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://h5.m.taobao.com/awp/core/detail.html?\\?.*id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
        "https?://main.m.taobao.com/security-h5-detail/home\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*"
    ])


def get_regex() -> str:
    link_pattern = _get_item_url()
    json_pattern = fr'{{"text":"({link_pattern})","jsview":\[{{"value":{{"url":"({link_pattern})","name":"({link_pattern})","safe":"SAFE"}},"type":1}}]}}'
    return json_pattern + "|" + link_pattern


regex = get_regex()

pattern = re.compile(regex)