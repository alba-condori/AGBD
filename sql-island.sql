SELECT * FROM INHABITANT | Muestra toda la lista de todos con su información

SELECT * FROM INHABITANT WHERE job = 'butcher' | Muestra a todos los habitantes que trabajan como carniceros

SELECT * FROM INHABITANT WHERE state = 'friendly' AND job = 'weaponsmith' | Muestra a los habitantes que son amigables y que además trabajan como fabricantes de armas

SELECT * FROM INHABITANT WHERE state = 'friendly' and job LIKE '%smith' | Muestra a los habitantes amigables y que además, su trabajo termina en “smith” //--El %, en este caso, sirve para indicar que la palabra termina en smith

SELECT personid FROM INHABITANT WHERE name LIKE "stranger" | Busca el numero de id de la persona que se llama “stranger”

SELECT gold FROM INHABITANT WHERE name LIKE 'stranger' | Muestra cuánto oro tiene el personaje con nombre “stranger”

SELECT * FROM ITEM WHERE owner IS NULL | Muestra los objetos que no tienen dueño

UPDATE item SET owner = 20 WHERE owner IS NULL | Designa como dueño, con el id 20, de todos los objetos que no tenían dueño

SELECT * FROM ITEM where owner = "20" | Muestra todos los objetos de la persona con id 20

SELECT * FROM INHABITANT where state = "friendly" AND job = "dealer" OR job = "merchant" | Muestra a los habitantes que son amigables y dealers o merchants

UPDATE item SET owner = "15" where item = 'ring' or item = 'teapot' | Cambia el dueño a la persona con el id 15 de los objetos ring y teapot

UPDATE inhabitant SET name = "Liam" WHERE personid = 20 | Cambia el nombre de la persona con el id 20 a Liam

SELECT * FROM INHABITANT WHERE job = "baker" ORDER BY gold DESC | Muestra a los panaderos ordenados de quien tiene mas oro y y quien tiene menos oro

SELECT * FROM INHABITANT WHERE job = "pilot" | Muestra a todos los habitantes que trabajan como pilotos

SELECT name FROM INHABITANT WHERE personid = "13" | Muestra el nombre de la persona con id 13

SELECT COUNT(*) FROM inhabitant, village WHERE village.villageid = inhabitant.villageid AND village.name = 'Onionville' AND inhabitant.gender = 'f' | Cuenta cuántas mujeres viven en el pueblo Onionville

SELECT name FROM inhabitant WHERE gender = 'f' AND villageid = '3' | Muestra los nombres de las mujeres que viven en el pueblo con id 3

SELECT SUM(gold) FROM inhabitant WHERE job like 'baker' OR job like 'dealer' OR job like 'merchant' | Suma todo el oro de los habitantes que trabajan como bakers, dealers o merchants

SELECT state, AVG(inhabitant.gold) FROM inhabitant GROUP BY state ORDER BY AVG (inhabitant.gold) | → Muestra el promedio de oro según el estado de los habitantes, ordenado de menor a mayor

DELETE FROM inhabitant WHERE name = "Dirty Diane" | Elimina de la base de datos al habitante llamado “Dirty Diane” (La mata)

UPDATE inhabitant SET state = "friendly" WHERE state = "kidnapped" | Cambia el estado de todos los secuestrados a friendly, en este caso del piloto

