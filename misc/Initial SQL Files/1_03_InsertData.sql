USE CarDealership
GO

Insert Dealerships(Name, Address1, Address2, Pcode, TelNo, www, email)
values('Clarke Kent Autos','67 High Street','Smallville','CK15 5SM','555-124569','www.clarkekentautos.com','clarke@clarkekentautos.com'),
('Peter Parker Secondhand car sales','','','PP33 1AM','555-234582','www.ppscs.com','spidey@ppscs.com'),
('Bruce Wayne Budget Limousines','Barn 47','Wayne Manor Industrial Estate','BM01 1BM','555-987243','www.wayne-limo.com','b@wayne-limo.com')
GO

Insert Manufacturers (Name, Established, City, Country)
values('Ford','16-Jun-1903','Detroit','USA'),
('Mercedes','01-Jun-1926','Stuttgart','Germany'),
('Volkswagen','28-May-1937','Berlin','Germany'),
('MG','01-May-1924','Oxford','England'),
('Porsche','01-jun-1931','Stuttgart','Germany'),
('Bugatti','01-jAN-1909','Molsheim','France')
GO
insert Models (Name, Seats,Style, ManID )
values('GT40','2','LeMans',1),
('Fiesta','4','Hatchback',1),
('Granada','5','Saloon',1),
('Escort','4','Estate',1),
('Focus','4','Hatchback',1),
('CLA-Class','4','Saloon',2),
('B Class','4','Saloon',2),
('300 SEL','5','Saloon',2),
('CLK','4','Cabriolet',2),
('GOlf','4','Cabriolet',3),
('Polo','4','Saloon',3),
('Passat','4','Estate',3),
('Up!','2','Compact',3),
('Midget','2','Cabriolet',4),
('BGT','2','Convertible',4)
GO

 -- need a dealerships <> manufacturers table to allow many<>many relationship
 -- 

 