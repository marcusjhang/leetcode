import java.util.*;

public class groupAnagrams {
    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray); //Strings in java are immutable so have to convert to charArray then sort
            String sortedWord = new String(charArray);

            if (map.containsKey(sortedWord)) {
                map.get(sortedWord).add(str);
            } else {
                map.put(sortedWord, new ArrayList<>()); // note that ArrayList is the concrete implementation of List (which is an interface) you cannot initialise a List
                map.get(sortedWord).add(str);
            }
        }

        return new ArrayList<>(map.values()); //map.values() returns a Collection<List<String>>. Passing it as an argument to the constructor constructs an ArrayList<List<String>>

    }

    public static void main(String[] args) {
        String[] strs = {"eat","tea","tan","ate","nat","bat"};
        System.out.println(groupAnagrams(strs));
    }
}
