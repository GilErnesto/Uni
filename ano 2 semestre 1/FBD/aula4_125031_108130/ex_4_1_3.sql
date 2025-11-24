CREATE DATABASE	GestaoEncomendas;
GO

USE GestaoEncomendas;
GO

CREATE SCHEMA fornecedor;
GO
CREATE SCHEMA encomenda;
GO

CREATE TABLE fornecedor.tipoFornecedor(
	codigo INT PRIMARY KEY CHECK(codigo>0),
	designacao VARCHAR(100) NOT NULL
);

CREATE TABLE fornecedor.fornecedor(
	nif INT PRIMARY KEY CHECK(nif BETWEEN 10000000 AND 999999999),
	nomeForn VARCHAR(100) NOT NULL,
	fax	VARCHAR(15) CHECK(fax LIKE '+%' AND LEN(fax)=13), /* +000 123456789000*/
	endereco VARCHAR(150) NOT NULL,
	codigo INT NOT NULL,
	FOREIGN KEY (codigo) REFERENCES fornecedor.tipoFornecedor(codigo)
);


CREATE TABLE encomenda.encomenda(
	numeroEnc INT PRIMARY KEY CHECK(numeroEnc>0),
	dataEnc DATE NOT NULL,
	nif INT NOT NULL,
	FOREIGN KEY (nif) REFERENCES fornecedor.fornecedor(nif)
);

CREATE TABLE encomenda.produto(
	codigoPro INT PRIMARY KEY CHECK(codigoPro>0),
	nomePro VARCHAR(100) NOT NULL,
	Preço DECIMAL(10,2) CHECK (Preço >= 0),
	iva DECIMAL(4,2) CHECK (iva >= 0 AND iva <= 1),
	numeroEnc INT NOT NULL,
	FOREIGN KEY (numeroEnc) REFERENCES encomenda.encomenda(numeroEnc)
);
GO