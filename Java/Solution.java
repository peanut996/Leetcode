package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    /**
     * 面试题 01.03. URL化 URL化。编写一种方法，将字符串中的空格全部替换为%20。
     * 假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。 （注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）
     * 
     * @param S
     * @param length
     * @return
     */
    public String replaceSpaces(String S, int length) {
        char[] s = S.toCharArray();
        char[] res = new char[S.length()];
        int index = 0;
        for (int i = 0; i < length; i++) {
            if (s[i] == ' ') {
                res[index++] = '%';
                res[index++] = '2';
                res[index++] = '0';
            } else {
                res[index++] = s[i];
            }
        }
        return String.valueOf(Arrays.copyOfRange(res, 0, index));
    }

    /**
     * 118.杨辉三角
     * 
     * 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
     * 
     * @param numRows
     * @return
     */
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>(numRows);
        for (int i = 0; i < numRows; i++) {
            List<Integer> tmpList = new ArrayList<Integer>(Collections.nCopies(i, 1));
            List<Integer> last = res.get(i - 1);
            if (i > 0) {
                for (int j = 1; j < i; j++) {
                    tmpList.set(j, last.get(j) + last.get(j - 1));
                }
            }
            res.add(tmpList);
        }
        return res;
    }

    /**
     * 面试题 01.04. 回文排列 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
     * 
     * 回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
     * 
     * 回文串不一定是字典当中的单词。
     * 
     * 示例1：
     * 
     * 输入："tactcoa" 输出：true（排列有"tacocat"、"atcocta"，等等）
     * 
     * 解题思路： 判断字符数量奇数的是否小于等于一
     * 
     * @param s
     * @return
     */
    public static boolean canPermutePalindrome(String s) {
        Set<Character> set = new HashSet<Character>();
        Arrays.stream(s.split("")).forEach(c -> {
            Character ch = Character.valueOf(c.charAt(0));
            if (!set.add(ch)) {
                set.remove(ch);
            }
        });
        return set.size() <= 1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.replaceSpaces("ds sdfs afs sdfa dfssf asdf             ", 27));
    }
}