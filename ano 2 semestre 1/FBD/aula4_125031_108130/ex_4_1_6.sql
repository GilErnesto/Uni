CREATE DATABASE	ATL;
GO

USE ATL;
GO

CREATE SCHEMA escola;
GO
CREATE SCHEMA pessoa;
GO

CREATE TABLE pessoa.professor(
	nomePro VARCHAR(100) NOT NULL,
	numFucionario INT CHECK(numFucionario>0),
	PRIMARY KEY (nomePro, numFucionario),
	telemovel VARCHAR(13) CHECK(telemovel LIKE '+%' AND LEN(telemovel)=13), /* +000 123456789*/
	email VARCHAR(50) CHECK(email LIKE '%@%.%'),
	morada VARCHAR(150) NOT NULL,
	nascimento DATE NOT NULL,
	numCCPro CHAR(12) CHECK (LEN(numCCPro) = 12 AND numCCPro NOT LIKE '%[^0-9A-Z]%')
);

CREATE TABLE escola.turma(
	identificadorTur INT PRIMARY KEY CHECK(identificadorTur>0),
	ano	INT CHECK(ano BETWEEN 1 AND 12),
	numMax INT CHECK(numMax>0),
	designacaoTur VARCHAR(5) NOT NULL, /* 12º A*/
	nomePro VARCHAR(100) NOT NULL,
	numFucionario INT NOT NULL,
	FOREIGN KEY (nomePro, numFucionario) REFERENCES pessoa.professor(nomePro, numFucionario)
);

CREATE TABLE escola.atividade(
	identificadorAti INT PRIMARY KEY CHECK(identificadorAti>0),
	custo DECIMAL(10,2) NOT NULL,
	curso VARCHAR(30) NOT NULL,
	designacaoAti VARCHAR(20) NOT NULL,
	identificadorTur INT NOT NULL,
	FOREIGN KEY (identificadorTur) REFERENCES escola.turma(identificadorTur)
);

CREATE TABLE pessoa.aluno(
	nomeAlu VARCHAR(100) PRIMARY KEY NOT NULL,
	morada VARCHAR(150) NOT NULL,
	nascimento DATE NOT NULL,
	numCCAlu CHAR(12) CHECK (LEN(numCCAlu) = 12 AND numCCAlu NOT LIKE '%[^0-9A-Z]%'),
	identificadorTur INT NOT NULL,
	identificadorAti INT NOT NULL,
	FOREIGN KEY (identificadorTur) REFERENCES escola.turma(identificadorTur),
	FOREIGN KEY (identificadorAti) REFERENCES escola.atividade(identificadorAti)
);

CREATE TABLE pessoa.adulto(
	nomePro VARCHAR(100) PRIMARY KEY NOT NULL,
	telemovel VARCHAR(13) CHECK(telemovel LIKE '+%' AND LEN(telemovel)=13), /* +000 123456789*/
	email VARCHAR(50) CHECK(email LIKE '%@%.%'),
	morada VARCHAR(150) NOT NULL,
	nascimento DATE NOT NULL,
	numCCAdul CHAR(12) CHECK (LEN(numCCAdul) = 12 AND numCCAdul NOT LIKE '%[^0-9A-Z]%'),
	relacaoAluno VARCHAR(15) NOT NULL,
	nomeAlu VARCHAR(100) NOT NULL,
	FOREIGN KEY (nomeAlu) REFERENCES pessoa.aluno(nomeAlu)
);