import java.util.HashMap;

public class StringCompression {
    public static void main(String[] args) {
        String s = "aabcccccaaa";
        System.out.println(compressString(s));
    }

    private static String compressString(String str) {
        StringBuilder sb = new StringBuilder();
        int count = 1;
        char prev = str.charAt(0);
        for(int i = 1; i < str.length(); i++){
            if (str.charAt(i) == prev){
                count++;
            }else {
                sb.append(str.charAt(i-1));
                sb.append(count);
                prev = str.charAt(i);
                count = 1;
            }
        }

        return str.length() < sb.length() ? str : new String(sb);
    }
}