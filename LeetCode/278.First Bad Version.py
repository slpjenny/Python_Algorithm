# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        answer = n

        while start <= end:
            mid = (start+end)//2

            if isBadVersion(mid) == True:
                end = mid-1
                answer = mid

            else:
                start = mid+1

        # while문 조건을 충족하지 못한다면, 이전에 저장해둔 mid값을 return 해야하므로
        # answer라는 변수를 사용
        return answer
