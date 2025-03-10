import java.util.Arrays;

public class checkPermutation {
    public static void main(String[] args) {
        String s1 = "abced";
        String s2 = "acebb";

        System.out.println(sort(s1).equals(sort(s2)));
    }

    public static String sort(String s){
        char[] chars = s.toCharArray();

        Arrays.sort(chars);

        return new String(chars);
    }
}