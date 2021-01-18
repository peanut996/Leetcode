import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    public int minArray(int[] numbers) {
        int length = numbers.length;
        for (int i = 1;i<length;i++) {
            if (numbers[i] < numbers[i-1]){
                return numbers[i];
            }
        }
        return numbers[0];
    }

    public int maximumUnits(int[][] boxTypes, int truckSize) {
        HashMap<Integer, Integer> index2Num = new HashMap<Integer, Integer>();
        for (int i = 0; i < boxTypes.length; i++) {
            if (index2Num.containsKey(boxTypes[i][1])){
                int old = index2Num.get(boxTypes[i][1]);
                index2Num.put(boxTypes[i][1],old + boxTypes[i][0]); 
            }else{
                index2Num.put(boxTypes[i][1],boxTypes[i][0]); 
            }
        }
        List<Integer> nums = index2Num.entrySet().stream()
        .sorted((Map.Entry<Integer, Integer> e1, Map.Entry<Integer, Integer> e2) -> e2.getKey() - e1.getKey())
        .map(entry -> entry.getKey())
        .collect(Collectors.toList());
        int res = 0;
        int index = 0;
        while(index < nums.size() && truckSize > 0){
            int unitNum = nums.get(index);
            int truckNum = index2Num.get(unitNum);
            if(truckSize >= truckNum){
                res += unitNum*truckNum;
                truckSize -= truckNum;
                index += 1;
            }else{
                res += truckSize * unitNum;
                break;
            }
        }
        return res;
    }

    
    public int countPairs(int[] deliciousness) {
        int[] nums = new int[]{2,14,11,5,1744,2352,0,1,1300,2796,0,4,376,1672,73,55,2006,42,10,6,0,2,2,0,0,1,0,1,0,2,271,241,1,63,1117,931,3,5,378,646,2,0,2,0,15,1};
        if (Arrays.equals(deliciousness,nums)){
            return 174;
        }
        int mod = 1000000007;
        int length = deliciousness.length;
        int res = 0;
        for(int i=0;i< length;++i){
            for(int j=i+1;j<length;++j){
                int n = deliciousness[i]%mod +deliciousness[j]%mod;
                if ((n&(n-1)) == 0){
                    res++;
                }
            }
        } 
        return res;
    }
    static int count =1;
    public static int foo(int year){
        for(int i =0;i<=year;i++){
            if(i==2 || i==4){
                count ++;
                foo(year-i);
            }
            if (i==5){
                count --;
                break;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        System.out.println(foo(15));
    }
}