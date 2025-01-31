class Solution:
    def compress(self, chars: List[str]) -> int:
        # 투포인터로 다른값이 나올때까지 index를 구한다.
        # 다 만들고나서 덮어씌우기는 하면 안됨
        n = len(chars)
        write = 0  # The position where we write in the original array
        i = 0  # The position for reading through the array
        while i < n:
            char = chars[i]
            count = 0
            while i < n and chars[i] == char:
                count += 1
                i += 1
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
