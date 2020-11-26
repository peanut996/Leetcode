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

// // 建表
// CREATE TABLE `person` (
// `name` int(11) NOT NULL,
// `age` int(11) NOT NULL,
// `birthday` varchar(255) NOT NULL,
// PRIMARY KEY (`name`)
// )

// class Person {
//     private String name;
//     private Integer age;
//     private String birthday;

//     public String getName() {
//         return name;
//     }

//     public void setName(String name) {
//         this.name = name;
//     }

//     public Integer getAge() {
//         return age;
//     }

//     public void setAge(Integer age) {
//         this.age = age;
//     }

//     public String getBirthday() {
//         return birthday;
//     }

//     public void setBirthday(String birthday) {
//         this.birthday = birthday;
//     }

//     public static void main(String[] args) {
//         String driverName = "com.mysql.jdbc.Driver";
//         String connectionUrl = "jdbc:mysql://127.0.0.1:3306/test";
//         String username = "root";
//         String password = "000000";
//         String sql = "insert into person values(?,?,?)";

//         Person person = new Person();
//         person.setName("jack");
//         person.setAge(24);
//         person.setBirthday("1995/10/24 00:00:00");
//         try {
//             Class.forName(driverName);
//             Connection conn = DriverManager.getConnection(connectionUrl, username, password);
//             PreparedStatement stmt = conn.prepareStatement(sql);
//             stmt.setString(1, person.getName());
//             stmt.setInt(2, person.getAge());
//             stmt.setString(3, person.getBirthday());
//             stmt.executeUpdate();
//         } catch (ClassNotFoundException e) {
//             // 异常处理
//             e.printStackTrace();
//         } catch (SQLException e) {
//             // 异常处理
//             e.printStackTrace();
//         }

//     }

// }