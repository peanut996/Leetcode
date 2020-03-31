package Java;
/*20. Valid Parentheses
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。
*/
// class Solution{
//     public boolean isValid(String s) {
//         while(s.contains("{}")||s.contains("()")||s.contains("[]")){
//             if(s.contains("{}")) s.replaceAll("\\{\\}", "");
//             if(s.contains("[]")) s.replaceAll("\\[\\]", "");
//             if(s.contains("()")) s.replaceAll("\\(\\)", "");
//         }
//         return s.equals("");
//     }
// }