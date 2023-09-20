CREATE DATABASE colaboradores;
USE colaboradores;
CREATE TABLE colaboradores(
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Nome VARCHAR(20),
	Idade INT,
	Salário INT,
	Salário_Ajustado INT
);