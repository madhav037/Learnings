public class OneAway {
    public static void main(String[] args) {
        String s1 = "pale";
        String s2 = "ple";
        System.out.println(checkString(s1, s2));
    }

    private static boolean checkString(String s1, String s2) {
        if (Math.abs(s1.length() - s2.length()) > 1) {
            return false;
        }

        int[] table = new int['z' - 'a' + 1];

        for (char c : s1.toCharArray()) {
            table[c - 'a']++;
        }

        for (char c : s2.toCharArray()) {
            table[c - 'a']--;
        }

        int count = 0;
        for (int diff : table) {
            count += Math.abs(diff);
            if (count > 2) { 
                return false;
            }
        }

        return true;
    }
}
