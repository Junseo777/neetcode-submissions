class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for sublist in strs:
            
            length = len(sublist)
            encoded_string += "#" + str(length) + "#"
            
            for i in sublist:
                encoded_string += i
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_list = []
        L=0
        R=L+1
        while R < len(s):
            
           
            str_length = ""
                
            while R < len(s) and s[R].isdigit():
                
                str_length += s[R]
                R +=1
                
                
            length = int(str_length)
            string = ""
            for i in range(R+1,R+1+length):
                string += s[i]
            decoded_list.append(string)

            L = R+1+length
            R = L+1
   
        return decoded_list


                

