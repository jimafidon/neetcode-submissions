public class Solution {
    public boolean isAnagram(String s, String t) {
        //if the lengths do not match it is not an anagram
        if (s.length() != t.length()) {
            return false;
        }

        //create two hashmaps to store how many times the letter
        //appears in each string
        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();
        //loop through both lengths (they are the same length)
        for (int i = 0; i < s.length(); i++) {
            //s/t.charAt(i) gets the character value at index i
            //getorDefault(s/t.charAt(i, 0) + 1) gets the current
            //count of the character from the ma
            //if the character isnt in the map yet it returns 0 
            //adds 1 to the count and stores it pack using .put (at the beginning)
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return countS.equals(countT);
    }
}