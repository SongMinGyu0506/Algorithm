-- 코드를 입력하세요
SELECT animal_id, name
FROM ANIMAL_INS
where animal_type = 'dog' and name LIKE '%el%'
order by name