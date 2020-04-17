// PokerHands.rs

// 获取花色
// Spades:3 Hearts:2 Diamonds:1 Clubs:0
fn getsuit(num: u32) -> usize{
    if num>=1 && num<=13 {
        return 0
    }else if num>=14 && num<=26{
        return 1
    }else if num>=27 && num<=39{
        return 2
    }else{
        return 3
    }
}

//获取值
fn getval(num: u32) -> u32{
    if num%13==0{ 
        13
    }else{
        num%13
    }
}

// 是否炸弹(连续四张)
fn is_bomb(hand: Vec<u32>)-> bool{
    for i in 0..=1{
        if getval(hand[i+1])==getval(hand[i]) && getval(hand[i+2])==getval(hand[i]) && getval(hand[i+3])== getval(hand[i]) {
            return true
        }
    }
    return false
}

// 是否三张连续
fn is_three(hand: Vec<u32>,i:usize) ->bool{
    if getval(hand[i+1])==getval(hand[i]) && getval(hand[i+2])==getval(hand[i]) {
        return true
    }
    return false
}

// 是否成对
fn is_pair(hand: Vec<u32>,i:usize) -> bool{
    if getval(hand[i+1])==getval(hand[i])  {
        return true
    }
    return false
}

// 是否全部连续
fn is_straight(hand: Vec<u32>) -> bool{
    for i in hand.clone(){
        println!("{:?}",getval(i));
    }
    if getval(hand[4])==1 && getval(hand[3])==13 && getval(hand[2])==12 && getval(hand[1])==11 && getval(hand[0])==10 {
        return true
    }

    if getval(hand[4])==1 && getval(hand[3])==5 && getval(hand[2])==4 && getval(hand[1])==3 && getval(hand[0])==2 {
        return true
    }

    for i in 1..hand.len(){
        if hand[i]!=hand[i-1]+1{
            return false
        }
    }
    return true
}

// 是否相同花色
fn is_flush(hand: Vec<u32>)-> bool{
    for i in 1..hand.len(){
        if getsuit(hand[i]) != getsuit(hand[i-1]){
            return false
        }
    }
    return true
}

// 获取等级
fn getlevel(hand: Vec<u32>,tag:&mut Vec<u32>,color:&mut usize ) -> u32{
    let mut level:u32=9;
    let (mut t1,mut t2,mut t3)=(0 as usize,0 as usize,0 as usize);
    let mut i:usize = 0; // 第三层比较
    // let mut tag:Vec<u32>=vec![0,0,0,0,0]; // 记录最大值 
    // 同花顺 -> 9
    if is_straight(hand.clone()) && is_flush(hand.clone()) {

        if getval(hand[4]) == 1{
            tag[0]=14;
        }else{
            tag[0]=getval(hand[4]);
        }
        *color = getsuit(hand[4]);
        return level;
    }
    // 炸弹 -> 8
    level-=1;
    if is_bomb(hand.clone()) {
        tag[0]=getval(hand[1]);
        return level;
    }
    // 3+2 ->7
    level-=1;
    if (is_three(hand.clone(),0) && is_pair(hand.clone(),3)) || (is_pair(hand.clone(),0) && is_three(hand.clone(),2)){
        tag[0]=getval(hand[2]);
        return level;
    }
    // 同花色 -> 6 
    level-=1;
    if is_flush(hand.clone()){
        for i in 0..5 {
            tag[i]=getval(hand[4-i]);
        }
        *color = getsuit(hand[4]);
        return level;
    }
    // 五张连续 -> 5
    level-=1;
    if is_straight(hand.clone()){
        tag[0]=getval(hand[4]);
    }
    // 三张相同 -> 4
    level-=1;
    if is_three(hand.clone(),0) || is_three(hand.clone(),1) || is_three(hand.clone(),2){
        tag[0]=getval(hand[2]);
        return level;
    }
    // 两幅对 -> 3
    level-=1;
    i=0;
    if is_pair(hand.clone(),1) && is_pair(hand.clone(),3) {
        tag[0]=getval(hand[3]);    
        tag[1]=getval(hand[1]);
        tag[2]=getval(hand[i]);
        return level;
    }
    i=2;
    if is_pair(hand.clone(),0) && is_pair(hand.clone(),3) {
        tag[0]=getval(hand[3]);    
        tag[1]=getval(hand[1]);
        tag[2]=getval(hand[i]);
        return level;
    }
    i=4;
    if is_pair(hand.clone(),0) && is_pair(hand.clone(),2) {
        tag[0]=getval(hand[3]);    
        tag[1]=getval(hand[1]);
        tag[2]=getval(hand[i]);
        return level;
    }
    // 一副对 -> 2
    level-=1;
    i=0;t1=4;t2=3;t3=2;
    if is_pair(hand.clone(),0){
        tag[0]=getval(hand[i]);
        tag[1]=getval(hand[t1]);
        tag[2]=getval(hand[t2]);
        tag[3]=getval(hand[t3]);
        return level;
    }
    i=1;t1=4;t2=3;t3=0;
    if is_pair(hand.clone(),1){
        tag[0]=getval(hand[i]);
        tag[1]=getval(hand[t1]);
        tag[2]=getval(hand[t2]);
        tag[3]=getval(hand[t3]);
        return level;
    }
    i=2;t1=4;t2=1;t3=0;
    if is_pair(hand.clone(),2){
        tag[0]=getval(hand[i]);
        tag[1]=getval(hand[t1]);
        tag[2]=getval(hand[t2]);
        tag[3]=getval(hand[t3]);
        return level;
    }
    i=3;t1=2;t2=1;t3=0;
    if is_pair(hand.clone(),3){
        tag[0]=getval(hand[i]);
        tag[1]=getval(hand[t1]);
        tag[2]=getval(hand[t2]);
        tag[3]=getval(hand[t3]);
        return level;
    }

    // 完全杂牌 -> 1
    level-=1;
    for i in 0..5 {
        tag[i] = getval(hand[4-i]);
    }
    return level;
}

fn deal(perm:[u32;10])->[&str;5]{
    let perm:Vec<u32> = perm.to_vec();
    let mut hand1:Vec<u32>= Vec::new();
    let mut hand2:Vec<u32>= Vec::new();
    for i in 0..perm.len(){
        if i&1 == 1 {
            hand1.push(perm[i] as u32)
        } 
    }

    for i in 0..perm.len(){
        if i&1 == 0 {
            hand2.push(perm[i] as u32)
        } 
    }
    hand1.sort_by_key(|s| if s%13 ==0 { 13 } else if s%13==1 {14} else { s%13 });
    hand2.sort_by_key(|s| if s%13 ==0 { 13 } else if s%13==1 {14} else { s%13 });
    let mut res:[&str;5]=["","","","",""];
    let mut tag1:Vec<u32>=vec![0,0,0,0,0];
    let mut tag2:Vec<u32>=vec![0,0,0,0,0];
    let (mut color1,mut color2)=(4,4);
    let (mut level1,mut level2) = (getlevel(hand1.clone(),&mut tag1,&mut color1),getlevel(hand2.clone(),&mut tag2,&mut color2));

    if level1 == level2{
        let mut i =0;
        while i < 5{
            if tag1[i] > tag2[i]{
                level1+=1;
                break;
            }
            if tag1[i] < tag2[i]{
                level2+=1;
                break;
            }
            i+=1;
        }
        if i==5 {
            if color1>color2{
                level1+=1;
            } else if color2 > color1{
                level2+=1;
            }else{
                level1+=1;
            }
        }
    }
    if level1 > level2{
        if getval(hand1[4])==1 && getval(hand1[3])==5 && getval(hand1[2])==4 && getval(hand1[1])==3 && getval(hand1[0])==2 {
            let temp=hand1.pop().unwrap();
            let mut new:Vec<u32> =vec![temp,hand1[0],hand1[1],hand1[2],hand1[3]];
            hand1=new;
        }
        for i in 0..5 {
            let mut temp=getval(hand1[i]).to_string();
            match getsuit(hand1[i]){
                0=>temp=temp+'C'.to_string().as_str(),
                1=>temp=temp+'D'.to_string().as_str(),
                2=>temp=temp+'H'.to_string().as_str(),
                3=>temp=temp+'S'.to_string().as_str(),
                _=>()
            } 
            // let b = Box::new(temp);
            // res[i]=Box::leak(b);
        }
    }
    if level1 < level2 {
        if getval(hand2[4])==1 && getval(hand2[3])==5 && getval(hand2[2])==4 && getval(hand2[1])==3 && getval(hand2[0])==2 {
            let temp=hand2.pop().unwrap();
            let mut new:Vec<u32> =vec![temp,hand2[0],hand2[1],hand2[2],hand2[3]];
            hand2=new;
        }
        for i in 0..5 {
            let mut temp=getval(hand2[i]).to_string().as_str();
            match getsuit(hand2[i]){
                0=>temp=temp+'C'.to_string().as_str(),
                1=>temp=temp+'D'.to_string().as_str(),
                2=>temp=temp+'H'.to_string().as_str(),
                3=>temp=temp+'S'.to_string().as_str(),
                _=>()
            } 
            // let b = Box::new(temp);
            // res[i]=Box::leak(b);
            // let ptr = Box::into_raw(b);
            // unsafe { Box::from_raw(ptr);}
        }
    }
    // println!("{:?}",res);
    // res.sort();
    return res;
}