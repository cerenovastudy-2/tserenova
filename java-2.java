import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        String text = "hello";
        HashMap<Character, Integer> freq = new HashMap<>();

        for (char c : text.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        System.out.println(freq); // {h=1, e=1, l=2, o=1}
    }
}
