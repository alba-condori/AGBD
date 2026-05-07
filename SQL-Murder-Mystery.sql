SELECT name 
  FROM sqlite_master
 where type = 'table'

--Muestra los nombres de las tablas donde el tipo sea "table"--



SELECT * FROM crime_scene_report
WHERE type = "murder" AND city = "SQL City" AND date = 20180115

--Muestra todos los datos de crime_scene_report donde el tipo sea "murder", la ciudad sea "SQL City" y la fecha sea "20180115".--



SELECT * FROM person
WHERE address_street_name =  "Northwestern Dr" ORDER BY address_number DESC

--Muestra a todas las personas que viven en "Northwestern Dr" y las ordenada por el número de direccion de mayor al menor--



SELECT * FROM interview
WHERE person_id = 14887

--Muestra la entrevista de la persona con el id 14887 (Es quien vive al fondo del Northwestern Dr)--



SELECT * FROM person JOIN get_fit_now_member 
ON person.id = get_fit_now_member.person_id
JOIN drivers_license
ON person.license_id = drivers_license.id
WHERE get_fit_now_member.id LIKE "48Z%"
AND get_fit_now_member.membership_status = "gold"
AND drivers_license.plate_number LIKE "%H42W%"
        
--Primero une las listas "person", "get_fit_now_member" y "drivers_license", despues indica que elementos se unen con elementos de otras listas (Estos coinciden). Finalmente muestra a la persona que coincida con los datos que nos dieron en la entrevista. Busca a alguien que su "id" de la membresía del gimnasio empiece por "48Z", que su "membership_status" sea "gold" y que su "plate_number" contenga "H42W"--



SELECT * FROM interview
WHERE person_id LIKE 67318

--Muestra la entrevista de la persona que su "person_id" es 67318--



--El asesino es Jeremy Bowers (fue contratado por alguien)--

