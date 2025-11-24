CREATE DATABASE GestaoConferencias;
GO

USE GestaoConferencias;
GO

CREATE SCHEMA artigo;
GO

CREATE SCHEMA participante;
GO

CREATE TABLE participante.participante(
	emailPar VARCHAR(70) PRIMARY KEY CHECK(emailPar LIKE '%@%.%'),
	morada VARCHAR(150) NOT NULL,
	nomePar VARCHAR(100) NOT NULL,
	dataInscricao DATE NOT NULL
);

CREATE TABLE artigo.instituicao(
	nomeInst VARCHAR(80) PRIMARY KEY NOT NULL,
	endereço VARCHAR(150) NOT NULL
);

CREATE TABLE participante.estudante(
	certificado VARCHAR(100) NOT NULL,
	emailPar VARCHAR(70) NOT NULL,
	FOREIGN KEY (emailPar) REFERENCES participante.participante(emailPar),
	nomeInst VARCHAR(80) NOT NULL,
	FOREIGN KEY (nomeInst) REFERENCES artigo.instituicao(nomeInst)
);

CREATE TABLE participante.naoEstudante(
	emailPar VARCHAR(70) NOT NULL,
	FOREIGN KEY (emailPar) REFERENCES participante.participante(emailPar),
	nomeInst VARCHAR(80) NOT NULL,
	FOREIGN KEY (nomeInst) REFERENCES artigo.instituicao(nomeInst)
);

CREATE TABLE artigo.autor(
	emailAur VARCHAR(70) PRIMARY KEY CHECK(emailAur LIKE '%@%.%'),
	nomeAut VARCHAR(100) NOT NULL,
	nomeInst  VARCHAR(80) NOT NULL,
	FOREIGN KEY (nomeInst) REFERENCES artigo.instituicao(nomeInst)
);

CREATE TABLE artigo.artigo(
	numRegisto INT PRIMARY KEY CHECK(numRegisto>0),
	titulo VARCHAR(50) NOT NULL,
	emailAur VARCHAR(70) NOT NULL,
	FOREIGN KEY (emailAur) REFERENCES artigo.autor(emailAur)
);
