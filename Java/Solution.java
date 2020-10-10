package Java;

import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    public String minNumber(int[] nums) {
        return IntStream.of(nums).mapToObj(String::valueOf).sorted((o1,o2) -> (o1+o2).compareTo(o2+o1)).collect(Collectors.joining());
    }
}
/*
*/