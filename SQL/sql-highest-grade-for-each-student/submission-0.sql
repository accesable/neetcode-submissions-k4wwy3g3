-- Write your query below
SELECT
    e.student_id,
    MIN(e.exam_id) AS exam_id,
    e.score
FROM exam_results AS e
WHERE (student_id, score) IN (
    SELECT student_id, MAX(score)
    FROM exam_results
    GROUP BY student_id
)
GROUP BY e.student_id, e.score
ORDER BY student_id