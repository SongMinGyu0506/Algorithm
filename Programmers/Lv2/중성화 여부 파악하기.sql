-- 코드를 입력하세요
SELECT animal_id, name, 
IF(SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%','O','X') as '중성화'
from animal_ins
ORDER BY ANIMAL_ID