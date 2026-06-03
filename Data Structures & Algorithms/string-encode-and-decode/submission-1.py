class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            # Add the length, then '#', then the string itself
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the '#' delimiter
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            # Extract the count (everything before '#')
            length = int(s[i:j])
            
            # Move past the '#'
            j += 1
            
            # Extract exactly 'length' characters after '#'
            string = s[j:j + length]
            decoded.append(string)
            
            # Move index to next count
            i = j + length
        
        return decoded

