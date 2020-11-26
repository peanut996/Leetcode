package Java;

import java.util.Arrays;
/**
 * 面试题 01.03. URL化
 * URL化。编写一种方法，将字符串中的空格全部替换为%20。
 * 假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。
 * （注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）
 */

class Solution {
    public String replaceSpaces(String S, int length) {
        char[] s = S.toCharArray();
        char[] res = new char[S.length()];
        int index = 0;
        for(int i=0;i<length;i++) {
            if(s[i] ==' '){
                res[index++] = '%';
                res[index++] = '2';
                res[index++] = '0';
            }else{
                res[index++] = s[i];
            }
        }
        return String.valueOf(Arrays.copyOfRange(res, 0, index));
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.replaceSpaces("ds sdfs afs sdfa dfssf asdf             ",27));
    }
}