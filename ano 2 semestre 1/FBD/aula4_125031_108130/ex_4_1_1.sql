CREATE TABLE Cliente(
    NIF INT NOT NULL PRIMARY KEY,
    Num_Carta INT NOT NULL,
    Nome VARCHAR(250) NOT NULL,
    Endereco VARCHAR(1046) NOT NULL,

    UNIQUE(Num_Carta),
);

CREATE TABLE Balcao(
    Numero INT NOT NULL PRIMARY KEY,
    Nome VARCHAR(250) NOT NULL,
    Endereco VARCHAR(1046) NOT NULL,

    UNIQUE(Endereco),
);

Create TABLE TipodeVeiculo(
    Codigo INT NOT NULL PRIMARY KEY,
    Arcondicionado BIT NOT NULL,
    Designacao VARCHAR(250) NOT NULL,
);

Create TABLE Veiculo(
    Matricula VARCHAR(250) NOT NULL PRIMARY KEY,
    Codigo INT NOT NULL REFERENCES TipodeVeiculo(Codigo),
    Marca VARCHAR(250) NOT NULL,
    Ano INT NOT NULL,
);

CREATE TABLE Aluguer(
    Numero INT NOT NULL PRIMARY KEY,
    [Data] DATE NOT NULL,
    Duracao INT NOT NULL,
    Cliente_NIF INT NOT NULL REFERENCES Cliente(NIF),
    Balcao_Numero INT NOT NULL REFERENCES Balcao(Numero),
    Veiculo_matricula VARCHAR(250) NOT NULL REFERENCES Veiculo(matricula),
);

CREATE TABLE Ligeiro(
    TipodeVeiculo_Codigo INT NOT NULL PRIMARY KEY REFERENCES TipodeVeiculo(Codigo),
    Portas INT NOT NULL,
    Num_Lugares INT NOT NULL,
    Combustivel VARCHAR(250) NOT NULL,
);

CREATE TABLE Pesado(
    TipodeVeiculo_Codigo INT NOT NULL PRIMARY KEY REFERENCES TipodeVeiculo(Codigo),
    Peso INT NOT NULL,
    Passageiros INT NOT NULL,
);

CREATE TABLE Similaridade(
    TipodeCodigo1 INT NOT NULL FOREIGN KEY REFERENCES TipodeVeiculo(Codigo),
    TipodeCodigo2 INT NOT NULL FOREIGN KEY REFERENCES TipodeVeiculo(Codigo),
    PRIMARY KEY(TipodeCodigo1, TipodeCodigo2),
);