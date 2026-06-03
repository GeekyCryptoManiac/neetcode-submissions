class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""   
            # Loop through each string
        for s in strs:
            # Add the length, then the string itself
            encoded += str(len(s)) + s
        
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            # Find where the number ends
            # We need to read the count (which could be multi-digit like "10" or "123")
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            
            # Extract the count
            length = int(s[i:j])
            
            # Extract the string of that length
            string = s[j:j + length]
            decoded.append(string)
            
            # Move index to next count
            i = j + length
        return decoded

