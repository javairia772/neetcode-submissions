class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        window = {}
        left = 0
        have = 0
        need = len(t_count)

        result = ""
        result_length = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need: #current window contains every char
                # removing characters from left to make window smaller
                if (right - left + 1) < result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1

                left_char = s[left]
                window[left_char] -= 1

                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1

                left += 1

        return result