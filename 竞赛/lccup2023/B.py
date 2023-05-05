from typing import List


class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
        init_expeditions = set(expeditions[0].split("->"))
        ans = -1
        mx = 0
        for i, expedition in enumerate(expeditions):
            cur_expeditions = set(expedition.split("->"))
            cur_expeditions = {t for t in cur_expeditions if t}
            if len(cur_expeditions) - len(init_expeditions.intersection(cur_expeditions)) > mx:
                ans = i
                mx = len(cur_expeditions) - len(init_expeditions.intersection(cur_expeditions))
            init_expeditions = init_expeditions | cur_expeditions
        return ans


if __name__ == '__main__':
    solution = Solution()
    expeditions = ["xO->xO->xO","xO->BKbWDH","xO->BKbWDH","BKbWDH->mWXW","LSAYWW->LSAYWW","oAibBvPdJ","LSAYWW->u","LSAYWW->LSAYWW"]
    res = solution.adventureCamp(expeditions)
    print(res)