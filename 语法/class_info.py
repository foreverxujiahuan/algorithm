import importlib
from typing import Any


def load_class_by_name(class_info: str) -> Any:
    """
    :params class_info:  类的信息, 比如'custom.nlu.tokenizers.siren_tokenizer.SirenTokenizer'
    """
    info = class_info.split(".")
    # 类名
    class_name = info.pop()
    # 包名
    class_path = ".".join(info)
    m = importlib.import_module(class_path)
    return getattr(m, class_name)


component_path = "siren.nlu.extractors.order_entity_recognizer.OrderEntityRecognizer"

ans = load_class_by_name(component_path)

print(ans)
