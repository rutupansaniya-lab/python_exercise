class Solution:
    def findComplement(self, num: int) -> int:
        return int(
            f'{num:b}'
            .replace('0', '.')
            .replace('1', '0')
            .replace('.', '1'),
            2
        )
