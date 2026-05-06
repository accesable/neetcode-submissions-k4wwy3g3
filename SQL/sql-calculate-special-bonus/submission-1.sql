-- Write your query below
SELECT e.employee_id, 
    CASE 
        WHEN not e.name like 'M%' and employee_id % 2 != 0 THEN (e.salary * 1)
        ELSE (e.salary * 0)
    END AS bonus
FROM employees as e
ORDER BY e.employee_id; 