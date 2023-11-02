from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        day = 0
        while day < len(temperatures):
            curr = temperatures[day]
            if len(st) == 0:
                st.append([curr, day])
            else:
                last, last_day = st.pop()

                if curr > last:
                    end = False
                    while curr > last:
                        res[last_day] = day - last_day

                        if len(st) > 0:
                            last, last_day = st.pop()
                        else:
                            end = True
                            break
                    if not end:
                        st.append([last, last_day])
                else:
                    st.append([last, last_day])
                st.append([curr, day])
            day += 1
        return res


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
