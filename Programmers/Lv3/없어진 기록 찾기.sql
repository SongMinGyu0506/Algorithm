select ANIMAL_OUTS.animal_id, ANIMAL_OUTS.name
from ANIMAL_OUTS
left outer join ANIMAL_INS
on ANIMAL_OUTS.animal_id = ANIMAL_INS.animal_id
where ANIMAL_INS.animal_id is NULL
order by ANIMAL_OUTS.animal_id