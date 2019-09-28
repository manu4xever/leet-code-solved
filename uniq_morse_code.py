International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        #print (words)
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        #morse_a = []
        arr=[]
        brr=[]
        l=[]
        for j in words:
            morse_a=[]
            for i in j:
                morse_add=morse[ord(i)-ord('a')]
                morse_a.append((morse_add))
            arr.append(''.join(morse_a))
            if arr not in brr:
                brr.append(''.join(morse_a))
        return(len(set(brr)))
#         for mor in brr:
#             if mor not in l:
#                 l.append(mor)
#         return (len(l))
                
        