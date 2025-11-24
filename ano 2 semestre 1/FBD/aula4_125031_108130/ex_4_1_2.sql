CREATE DATABASE GestaodeReservasdeVoos;
GO

USE GestaodeReservasdeVoos;
GO

CREATE SCHEMA airplane;
GO

CREATE TABLE airplane.planetype (
	typeName VARCHAR(15) PRIMARY KEY NOT NULL,
	company VARCHAR(25) NOT NULL,
	max_seats INT CHECK(max_seats > 0)
);

CREATE TABLE airplane.plane (
	airplane_id INT PRIMARY KEY NOT NULL,
	total_no_of_seats INT CHECK(total_no_of_seats > 0),
	typeName VARCHAR(15) NOT NULL,
	FOREIGN KEY (typeName) REFERENCES airplane.planetype(typeName)
);
GO

CREATE SCHEMA airport;
GO

CREATE TABLE airport.airport (
	code CHAR(5) PRIMARY KEY NOT NULL,
	city VARCHAR(20) NOT NULL,
	state VARCHAR(20) NOT NULL,
	name VARCHAR(20) NOT NULL
);

CREATE TABLE airport.canLand (
	code CHAR(5) NOT NULL,
	typeName VARCHAR(15) NOT NULL,
	PRIMARY KEY (code, typeName),
	FOREIGN KEY (code) REFERENCES airport.airport(code),
	FOREIGN KEY (typeName) REFERENCES airplane.planetype(typeName)
);
GO

CREATE SCHEMA flight;
GO

CREATE TABLE flight.fly (
	number INT PRIMARY KEY NOT NULL,
	airline VARCHAR(25) NOT NULL,
	weekdays VARCHAR(20)
);

CREATE TABLE flight.leg (
	number INT NOT NULL,
	leg_no INT NOT NULL,
	scheduled_departTime DATETIME NOT NULL,
	scheduled_arriveTime DATETIME NOT NULL,
	departure_airport CHAR(5) NOT NULL,
	arrival_airport CHAR(5) NOT NULL,
	PRIMARY KEY (number, leg_no),
	FOREIGN KEY (number) REFERENCES flight.fly(number),
	FOREIGN KEY (departure_airport) REFERENCES airport.airport(code),
	FOREIGN KEY (arrival_airport) REFERENCES airport.airport(code),
	CHECK (scheduled_arriveTime > scheduled_departTime)
);

CREATE TABLE flight.fare (
	fareCode CHAR(5) PRIMARY KEY NOT NULL,
	number INT NOT NULL,
	amount DECIMAL(10,2) CHECK (amount > 0),
	restrictions VARCHAR(1000),
	FOREIGN KEY (number) REFERENCES flight.fly(number)
);

CREATE TABLE flight.legInstance (
	legData DATE NOT NULL,
	leg_no INT NOT NULL,
	number INT NOT NULL,
	airplane_id INT NOT NULL,
	code CHAR(5) NOT NULL,
	numberAvailableSeats INT CHECK(numberAvailableSeats >= 0),
	arriveTime DATETIME NOT NULL,
	departTime DATETIME NOT NULL,
	PRIMARY KEY (legData, leg_no, number),
	FOREIGN KEY (number, leg_no) REFERENCES flight.leg(number, leg_no),
	FOREIGN KEY (airplane_id) REFERENCES airplane.plane(airplane_id),
	FOREIGN KEY (code) REFERENCES airport.airport(code),
	CHECK (arriveTime > departTime)
);

CREATE TABLE flight.seat (
	seatNumber INT PRIMARY KEY NOT NULL,
	legData DATE NOT NULL,
	number INT NOT NULL,
	leg_no INT NOT NULL,
	customerName VARCHAR(100) NOT NULL,
	telemovel CHAR(9) CHECK(LEN(telemovel) = 9 AND telemovel NOT LIKE '%[^0-9]%'),
	FOREIGN KEY (legData, leg_no, number) REFERENCES flight.legInstance(legData, leg_no, number)
);
GO
