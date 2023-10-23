/*
Question:

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
*/

// Solution:

class Solution {
    public String toLowerCase(String s) {
        StringBuilder res = new StringBuilder();
        for(int i=0; i<s.length();i++)
        {
            int currentChar = (int)s.charAt(i);
            if(currentChar<91 && currentChar>=65)
            {
                res.append((char)(currentChar+32));
            }
            else
            {
                res.append((char)currentChar);
            }
        }
        return res.toString();
    }
}
