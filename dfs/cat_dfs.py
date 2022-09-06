from typing import Dict, Tuple

cat2children = {}


def cat_dfs(parent: str, cat2sdq_tuple: Dict[str, Tuple[str, float]]):
    children = cat2children.get(parent, [])
    parent_intent = cat2sdq_tuple.get(parent)
    child_intents = []
    for child in children:
        child_intent = cat_dfs(child, cat2sdq_tuple)
        if child_intent:
            child_intents.append(child_intent)
    if parent_intent is None:
        return child_intents
    intents = []
    for child_intent in child_intents:
        if child_intent[1] - parent_intent >= -1e-3:
            intents.append(child_intent)
    return intents if intents else [parent_intent]


