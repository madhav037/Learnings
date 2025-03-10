public class URLify {
    public static void main(String[] args) {
        String s = "Mr john Smith    ";
        char[] ch = s.toCharArray();
        System.out.println(url(ch, 13));
    }

    private static String url(char[] ch, int trueLength) {
        int totalSpaces = 0;
        for (int i = 0; i < trueLength; i++) {
            if (ch[i] == ' ') {
                totalSpaces++;
            }
        }
        int index = trueLength + totalSpaces * 2;
        for (int i = trueLength - 1; i >= 0; i--) {
            if (ch[i] == ' ') {
                ch[index - 1] = '0';
                ch[index - 2] = '2';
                ch[index - 3] = '%';
                index -= 3;
            } else {
                ch[index - 1] = ch[i];
                index--;
            }
        }
        return new String(ch);
    }
}