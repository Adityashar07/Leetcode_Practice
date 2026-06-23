class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m
        up = [0]* m
        down = [0]*m
        
        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i

        if n == 2:
            return sum(up) + sum(down)

        for _ in range(3, n + 1):
            new_up = [0]* m
            new_down = [0]*m
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = (pref[i] + down[i]) % MOD

            suff = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suff[i] = (suff[i + 1] + up[i]) % MOD

            for i in range(m):
                new_up[i] = pref[i]
                new_down[i] = suff[i + 1]

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD