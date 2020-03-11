class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        lines = 1
        current_width = 0
        for char in S:
            current_char_length = widths[alphabet.index(char)]
            if current_width + current_char_length <= 100:
                current_width += current_char_length
            else:
                lines += 1
                current_width = current_char_length
        return [lines, current_width]