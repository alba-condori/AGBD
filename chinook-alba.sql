--Nombre y Apellido de todos los empleados, en orden alfabético.--

SELECT FirstName, LastName FROM employees
ORDER BY FirstName, LastName DESC


--Nombre y duración de todas las canciones del álbum "Big Ones" ordenados del más largo al más corto--

SELECT name, Milliseconds FROM tracks
JOIN albums ON tracks.AlbumId = albums.AlbumId
WHERE Title LIKE "Big Ones" ORDER BY Milliseconds DESC


--Nombre y precio total de los 10 discos más baratos--

SELECT Title, SUM(UnitPrice)
FROM tracks JOIN albums 
ON tracks.AlbumId = albums.AlbumId 
GROUP BY tracks.AlbumId
ORDER BY tracks.UnitPrice ASC
LIMIT 10


--Nombre del tema, nombre del género y nombre del disco del los temas que valen $0.99--

SELECT tracks.name, genres.Name, albums.Title, tracks.UnitPrice
FROM tracks JOIN albums 
ON tracks.AlbumId = albums.AlbumId 
JOIN genres
ON tracks.GenreId = genres.GenreId
WHERE tracks.UnitPrice like 0.99


--Nombre del tema, duración, nombre del disco y nombre del artista de los 20 temas más cortos--

SELECT tracks.name, tracks.Milliseconds, albums.Title, artists.Name
FROM tracks JOIN albums 
ON tracks.AlbumId = albums.AlbumId 
JOIN artists
ON artists.ArtistId = albums.ArtistId
ORDER by tracks.Milliseconds ASC
LIMIT 20


--Apellido, puesto, apellido del jefe y cantidad de clientes que atiende de todos los empleados,
--ordenado desde los que atienden más clientes a los que atienden menos.

SELECT Emp.LastName As Apellido_Empleado, Emp.Title As Puesto, Jefe.LastName As Apellido_Jefe, COUNT(SupportRepId) AS Cant_clientes
FROM employees Emp 
LEFT JOIN employees Jefe ON Emp.ReportsTo = Jefe.EmployeeId
LEFT JOIN customers ON Emp.EmployeeId = customers.SupportRepId
GROUP BY Emp.EmployeeId ORDER BY Cant_clientes DESC


--Nombre y apellido del empleado/a y nombre y apellido del cliente/a que 
--atiende cada empleado/a 

SELECT Emp.FirstName As Nombre_Empleado, Emp.LastName As Apellido_Empleado, Clie.FirstName As Nombre_Cliente, Clie.LastName As Apellido_cliente
FROM employees Emp JOIN customers Clie
ON Emp.EmployeeId = Clie.SupportRepId


--Nombre, apellido y direccion del cliente/a y la factura correspondiente a ese cliente.

SELECT Clie.FirstName As Nombre_Cliente, Clie.LastName As Apellido_cliente, Clie.Address As Direccion, Fac.InvoiceId As Factura
FROM customers Clie JOIN invoices Fac
ON Clie.CustomerId = Fac.InvoiceId


--Mostrar el nombre del género y el número total de canciones
--asociadas a cada uno, ordenados de mayor a menor cantidad. 

SELECT genres.name, sum(tracks.GenreId) As Cant_canciones
FROM tracks JOIN genres
ON tracks.GenreId = genres.GenreId
GROUP BY tracks.GenreId
ORDER BY Cant_canciones DESC


-- Mostrar el nombre del cliente y el nombre del artista de las
--canciones que ha comprado, ordenado alfabéticamente por cliente
--para ver qué variedad de artistas consume cada uno.

SELECT customers.FirstName As Nombre_cliente, artists.Name As Artista_escuchado
FROM customers JOIN invoices
ON customers.CustomerId = invoices.InvoiceId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceLineId
JOIN tracks ON tracks.TrackId = invoice_items.TrackId
JOIN albums ON albums.AlbumId = tracks.AlbumId
JOIN artists ON artists.ArtistId = albums.ArtistId
ORDER BY customers.FirstName


--Mostrar el nombre del cliente, la ciudad donde vive, el nombre 
--de la canción que compró y el nombre del género de esa canción.

SELECT customers.FirstName As Nombre_cliente, customers.City, tracks.name As Cancion, genres.Name As Genero
FROM customers JOIN invoices
ON customers.CustomerId = invoices.InvoiceId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceLineId
JOIN tracks ON tracks.TrackId = invoice_items.TrackId
JOIN genres ON genres.GenreId = tracks.TrackId


--Se puede realizar una sentencia que una todas las tablas? En caso de que sea un sí,
--realizar la sentencia, en caso de que sea no, justificar la respuesta.

--Si es posible unir todas las tablas, ya que todas tienen al menos una relacion entre ellas.

SELECT * FROM employees JOIN customers
ON employees.EmployeeId = customers.SupportRepId
JOIN invoices ON customers.CustomerId = invoices.InvoiceId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceLineId
JOIN tracks ON tracks.TrackId = invoice_items.TrackId
JOIN albums ON albums.AlbumId = tracks.AlbumId
JOIN artists ON artists.ArtistId = albums.ArtistId
JOIN genres ON genres.GenreId = tracks.TrackId
JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
JOIN playlist_track ON playlist_track.TrackId = tracks.TrackId
JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
