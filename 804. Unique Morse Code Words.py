class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha= ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
        for ind in range(len(words)):
            el= list(words[ind])
            trans= ''
            for letter in el:
                trans+= morse[alpha.index(letter)]
            words[ind]=trans
        return len(set(words))
