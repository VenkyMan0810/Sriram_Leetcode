-- SELECT a.student_id, a.student_name, COUNT(b.subject_name)
-- FROM Students as A
-- LEFT JOIN Examinations as B
-- ON a.student_id = b.student_id
-- GROUP BY b.subject_name, a.student_id;

-- SELECT a.student_id, a.student_name, COUNT(b.subject_name)
-- FROM Students AS a
-- LEFT JOIN Examinations AS b
-- ON a.student_id = b.student_id
-- GROUP BY a.student_id, b.subject_name
-- ORDER BY a.student_id;

-- SELECT a.student_id, a.student_name, b.subject_name, COUNT(c.subject_name)
-- FROM Students AS a 
-- JOIN Subjects AS b 
-- JOIN Examinations as C
-- ON a.student_id = c.student_id
-- GROUP BY c.student_id;

SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
ON s.student_id = e.student_id
AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name;