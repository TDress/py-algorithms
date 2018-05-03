from lib.assertion import equals

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans, carry = '', 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0:
            next_1 = 0 if i < 0 else int(num1[i])
            next_2 = 0 if j < 0 else int(num2[j])

            sum_col = next_1 + next_2 + carry
            carry, ans = sum_col // 10, str(sum_col % 10) + ans

            i -= 1
            j -= 1

        return str(carry) + ans if carry > 0 else ans



def main():
    func = Solution().addStrings

    l1 = "99"
    l2 = "9"

    equals("108", func(l1, l2))

if __name__ == '__main__':
    main()
