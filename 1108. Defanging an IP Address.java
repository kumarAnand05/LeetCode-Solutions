/*
Question:

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
*/

// Solution:

import java.util.*;
class Solution {
    public String defangIPaddr(String address) {
        String[] arr = address.split("\\.");
        StringBuilder sb=new StringBuilder();
        for(String x : arr){
            sb.append(x+"[.]");
        }
        sb.delete(sb.length()-3, sb.length());;
        return sb.toString();
    }
}
