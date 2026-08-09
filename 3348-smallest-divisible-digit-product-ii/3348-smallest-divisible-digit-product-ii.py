class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        c2 = c3 = c5 = c7 = 0
        while temp % 2 == 0:
            c2 += 1
            temp //= 2
        while temp % 3 == 0:
            c3 += 1
            temp //= 3
        while temp % 5 == 0:
            c5 += 1
            temp //= 5
        while temp % 7 == 0:
            c7 += 1
            temp //= 7
        
        if temp > 1:
            return "-1"
            
        def get_min_len(r2, r3, r5, r7):
            r2, r3, r5, r7 = max(0, r2), max(0, r3), max(0, r5), max(0, r7)
            cnt = (r3 // 2) + (r2 // 3) + r5 + r7
            rem3, rem2 = r3 % 2, r2 % 3
            if rem3 == 1 and rem2 == 2:
                cnt += 2
            elif rem3 > 0 or rem2 > 0:
                cnt += 1
            return cnt

        FACTOR_MAP = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        n = len(num)
        
        zero_pos = num.find('0')
        if zero_pos == -1:
            cur2, cur3, cur5, cur7 = c2, c3, c5, c7
            for ch in num:
                d2, d3, d5, d7 = FACTOR_MAP[int(ch)]
                cur2 -= d2
                cur3 -= d3
                cur5 -= d5
                cur7 -= d7
            if cur2 <= 0 and cur3 <= 0 and cur5 <= 0 and cur7 <= 0:
                return num

        pref_r2 = [c2] * (n + 1)
        pref_r3 = [c3] * (n + 1)
        pref_r5 = [c5] * (n + 1)
        pref_r7 = [c7] * (n + 1)
        
        valid_prefix_len = n
        for i in range(n):
            if num[i] == '0':
                valid_prefix_len = i
                break
            d2, d3, d5, d7 = FACTOR_MAP[int(num[i])]
            pref_r2[i + 1] = pref_r2[i] - d2
            pref_r3[i + 1] = pref_r3[i] - d3
            pref_r5[i + 1] = pref_r5[i] - d5
            pref_r7[i + 1] = pref_r7[i] - d7

        def build_suffix(rem_len, r2, r3, r5, r7):
            res = []
            for _ in range(rem_len):
                for d in range(1, 10):
                    d2, d3, d5, d7 = FACTOR_MAP[d]
                    nr2, nr3, nr5, nr7 = r2 - d2, r3 - d3, r5 - d5, r7 - d7
                    if get_min_len(nr2, nr3, nr5, nr7) <= rem_len - 1 - len(res):
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)

        for i in range(valid_prefix_len, -1, -1):
            r2, r3, r5, r7 = pref_r2[i], pref_r3[i], pref_r5[i], pref_r7[i]
            rem_len = n - i
            if rem_len == 0:
                continue
            
            start_d = int(num[i]) + 1 if i < n else 1
            for d in range(start_d, 10):
                d2, d3, d5, d7 = FACTOR_MAP[d]
                nr2, nr3, nr5, nr7 = r2 - d2, r3 - d3, r5 - d5, r7 - d7
                if get_min_len(nr2, nr3, nr5, nr7) <= rem_len - 1:
                    prefix = num[:i] + str(d)
                    suffix = build_suffix(rem_len - 1, nr2, nr3, nr5, nr7)
                    return prefix + suffix

        min_len_req = get_min_len(c2, c3, c5, c7)
        target_len = max(n + 1, min_len_req)
        return build_suffix(target_len, c2, c3, c5, c7)