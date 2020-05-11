--
-- @lc app=leetcode.cn id=197 lang=mysql
--
-- [197] 上升的温度
--
-- https://leetcode-cn.com/problems/rising-temperature/description/
--
-- database
-- Easy (50.80%)
-- Likes:    121
-- Dislikes: 0
-- Total Accepted:    35.8K
-- Total Submissions: 70.5K
-- Testcase Example:  '{"headers": {"Weather": ["Id", "RecordDate", "Temperature"]}, "rows": {"Weather": [[1, "2015-01-01", 10], [2, "2015-01-02", 25], [3, "2015-01-03", 20], [4, "2015-01-04", 30]]}}'
--
-- 给定一个 Weather 表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 Id。
-- 
-- +---------+------------------+------------------+
-- | Id(INT) | RecordDate(DATE) | Temperature(INT) |
-- +---------+------------------+------------------+
-- |       1 |       2015-01-01 |               10 |
-- |       2 |       2015-01-02 |               25 |
-- |       3 |       2015-01-03 |               20 |
-- |       4 |       2015-01-04 |               30 |
-- +---------+------------------+------------------+
-- 
-- 例如，根据上述给定的 Weather 表格，返回如下 Id:
-- 
-- +----+
-- | Id |
-- +----+
-- |  2 |
-- |  4 |
-- +----+
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT w2.Id FROM Weather w1,Weather w2
WHERE DATEDIFF(w2.RecordDate,w1.RecordDate) = 1
AND w1.temperature < w2.temperature
-- @lc code=end

