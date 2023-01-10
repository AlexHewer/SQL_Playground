USE master
GO
if exists (SELECT 1 FROM sys.databases WHERE name = 'CarDealership') 
begin
	ALTER DATABASE CarDealership SET  SINGLE_USER WITH ROLLBACK IMMEDIATE
	
	DROP DATABASE CarDealership
end
GO

CREATE DATABASE CarDealership