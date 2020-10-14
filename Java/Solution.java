package Java;

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    private static Solution instance = new Solution();

    private Solution() {
    }

    public static Solution getInstance() {
        return instance;
    }
    public static String compress(String s){
            String result = "";
            int length = s.length();
            System.out.println("length: "+length);
            int count  = 0;
            // 获取重复字符串
            for (int i= 1;i<=length;i++){
                String[] strings1 = s.split(s.substring(0,i));
                if (strings1.length==0){
                    count = i;
                    break;
                }

            }
            result = length/count + s.substring(0,count);
            return result;
        }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = null;
        if (scan.hasNext()) {
             s = scan.next();
        }
        // String s="aaaa";
        Solution solution = Solution.getInstance();
        System.out.println(solution.compress(s));
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