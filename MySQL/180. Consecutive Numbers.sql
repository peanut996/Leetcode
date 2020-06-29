--
-- @lc app=leetcode.cn id=180 lang=mysql
--
-- [180] 连续出现的数字
--
-- https://leetcode-cn.com/problems/consecutive-numbers/description/
--
-- database
-- Medium (48.86%)
-- Likes:    262
-- Dislikes: 0
-- Total Accepted:    35.3K
-- Total Submissions: 72.3K
-- Testcase Example:  '{"headers": {"Logs": ["Id", "Num"]}, "rows": {"Logs": [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}'
--
-- 编写一个 SQL 查询，查找所有至少连续出现三次的数字。
-- 
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- 
-- 
-- 例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。
-- 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
    DISTINCT L1.Num as ConsecutiveNums --防止重复
FROM
    Logs L1,
    Logs L2,
    Logs L3
WHERE
    L1.Id = L2.Id - 1
    AND L2.Id = L3.Id - 1
    AND L1.Num = L2.Num
    AND L2.Num = L3.Num
-- @lc code=end

