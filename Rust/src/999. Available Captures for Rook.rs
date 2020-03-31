/*999. Available Captures for Rook
在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。

车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。

返回车能够在一次移动中捕获到的卒的数量。

*/
impl Solution {
    pub fn num_rook_captures(board: Vec<Vec<char>>) -> i32 {
        fn get_rook(board: &Vec<Vec<char>>)->(usize,usize){
            for (r,row) in board.iter().enumerate(){
                for (c,ch) in row.iter().enumerate(){
                    if *ch == 'R'{
                        return (r,c)
                    }
                }
            }
            unreachable!()
        }
        fn is_pawn<'a>(mut itr: impl Iterator <Item = &'a char>) ->i32{
            while let Some(ch)=itr.next(){
                match *ch{
                    'p'=>return 1,
                    '.'=>continue,
                    _ =>break,
                }
                
            }
            0
        }

        let (r,c) = get_rook(&board);
        
        is_pawn((0..c).rev().map(|x| &board[r][x]))
            +is_pawn((c+1..8).map(|x| &board[r][x]))
            +is_pawn((0..r).rev().map(|x| &board[x][c]))
            +is_pawn((r+1..8).map(|x| &board[x][c]))
    }
    
}