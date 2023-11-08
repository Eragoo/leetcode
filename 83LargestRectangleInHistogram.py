from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [[0, heights[0]]]
        h = heights[0]
        for i in range(1, len(heights)):
            idx, el = st.pop()

            cur = heights[i]
            if cur < el:
                j = 0
                while cur < el:
                    j = idx
                    c_h = (i - idx) * el
                    if c_h > h:
                        h = c_h
                    if len(st) > 0:
                        idx, el = st.pop()
                    else:
                        break
                if cur >= el:
                    st.append([idx, el])

                st.append([j, cur])
            else:
                st.append([idx, el])
                st.append([i, cur])

        for i in range(0, len(st)):
            i, el = st.pop()
            c_h = (len(heights) - i) * el
            if c_h > h:
                h = c_h

        return h



if __name__ == '__main__':
    # should be 20
    print(Solution().largestRectangleArea([4,3,5,5,9,2,8,4,7,2,3,8,3,5,4,7,9]))
