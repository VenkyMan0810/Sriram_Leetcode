# Write your MySQL query statement below
(
    SELECT a.name AS results
FROM Users AS a
JOIN MovieRating AS b
ON a.user_id = b.user_id
GROUP BY b.user_id
ORDER BY  COUNT(b.movie_id) DESC, a.name ASC
LIMIT 1
)
UNION ALL
(
SELECT a.title AS results
FROM Movies a
JOIN MovieRating b
ON a.movie_id = b.movie_id
WHERE b.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY b.movie_id
ORDER BY AVG(b.rating) DESC, a.title ASC
LIMIT 1
);