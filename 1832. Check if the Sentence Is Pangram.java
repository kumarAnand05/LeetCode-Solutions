/*
Question:

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
*/

// Solution:

class Solution {
    public boolean checkIfPangram(String sentence) {
        if(sentence.length()<26)
        {
            return false;
        }
        else
        {
            for(int i =97;i<97+26;i++)
            {
                if(sentence.indexOf((char)i)==(-1))
                {
                    return false;
                }
            }
            return true;
        }    
    }
}
