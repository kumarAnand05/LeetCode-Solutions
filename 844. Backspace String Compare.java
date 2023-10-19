/*
Question:

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
*/

// Solution:

import java.util.*;

class Solution {
    public boolean backspaceCompare(String s, String t) {
        StringBuilder sb = new StringBuilder();
        StringBuilder tb = new StringBuilder();

        int backCount = 0;
        for(int i=s.length()-1;i>=0;i--)
        {
            String currentChar = s.charAt(i)+"";
            if(currentChar.equals("#"))
            {
                backCount+=1;
            }
            else if(backCount==0)
            {
                sb.insert(0,currentChar);
            }
            else
            {
                backCount-=1;
            }
        }

        backCount=0;
        for(int j=t.length()-1;j>=0;j--)
        {
            String currentChar = t.charAt(j)+"";
            if(currentChar.equals("#"))
            {
                backCount+=1;
            }
            else if(backCount==0)
            {
                tb.insert(0,currentChar);
            }
            else
            {
                backCount-=1;
            }
        }
        return sb.toString().equals(tb.toString());
    }

}
    
