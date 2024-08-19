from enum import Enum


class MatchType(Enum):
    # 匹配类型，分为匹配/不匹配/无法确定

    MATCHED = "MATCHED"
    UNMATCHED = "UNMATCHED"
    UNCERTAIN = "UNCERTAIN"

    def __eq__(self, other):
        return self.value == other


eq = MatchType.UNMATCHED == "UNMATCHED"
print(eq)
print(MatchType.UNMATCHED)
print(type(MatchType.UNMATCHED))
