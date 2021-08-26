use leetcode_rust::*;

fn main(){
    let people = vec![3,2,2,1];
    let limit = 3;
    println!("{}", Solution::num_rescue_boats(people, limit));
}