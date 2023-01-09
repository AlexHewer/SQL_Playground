
USE CarDealership
GO

create table Models(
	modID int identity,
	Name varchar(100),
	ManID int,
	Seats int,
	Style varchar(30)
)
GO

Create table Manufacturers(
	manID INT identity,
	Name varchar(100),
	Established datetime,
	City varchar(80),
	Country varchar(80)
)

GO

create table Dealerships(
	dealID int identity,
	Name varchar(150),
	Address1 varchar(100),
	Address2 varchar(100),
	Pcode varchar(15),
	TelNo varchar(15),
	email varchar(100),
	www varchar(150)
)
