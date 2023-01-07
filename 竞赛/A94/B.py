from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback_set = set(positive_feedback)
        negative_feedback_set = set(negative_feedback)
        scores = []
        for s, r in zip(student_id, report):
            words = r.split()
            score = 0
            for word in words:
                if word in positive_feedback_set:
                    score += 3
                if word in negative_feedback_set:
                    score -= 1
            scores.append((score, s))
        scores.sort(key= lambda d:(-d[0], d[1]))
        ans = []
        for i in range(k):
            ans.append(scores[i][1])
        return ans

if __name__ == '__main__':
    solution = Solution()
    positive_feedback = ["smart", "brilliant", "studious"]
    negative_feedback = ["not"]
    report = ["this student is studious","the student is smart"]
    student_id = [1,2]
    # positive_feedback = ["smart", "brilliant", "studious"]
    # negative_feedback = ["not"]
    # report = ["this student is not studious","the student is smart"]
    # student_id = [1,2]
    # k = 2

    k = 2
    res = solution.topStudents(positive_feedback, negative_feedback,report, student_id, k)
    print(res)