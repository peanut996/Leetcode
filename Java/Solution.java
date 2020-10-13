package Java;

import java.util.ArrayList;

class Solution {
    public static void main(String[] args) {
        System.out.println(helper(16));
        ArrayList<Integer> arrays = new ArrayList<Integer>();
        System.out.println(arrays);
    }
    public static int m = 3;
    public  static int helper(int n){
        int res = 0;
        for(int i=2;i<n+1;i++){
            res = (res+m)%i;
        }
        return res+1;
    }
}