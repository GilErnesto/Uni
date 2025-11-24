CREATE TABLE Medico (
    IDSNS INT NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Especialidade VARCHAR(30) NOT NULL,

    PRIMARY KEY(IDSNS),
);

CREATE TABLE Paciente (
    NumeroUtente INT NOT NULL,
    DataNascimento DATE NOT NULL,
    Endereco VARCHAR(50) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    IDSNSMedico INT NOT NULL,

    PRIMARY KEY(NumeroUtente),
    FOREIGN KEY(IDSNSMedico) REFERENCES Medico(IDSNS),
);

CREATE TABLE Farmacia (
    NIF INT NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Endereco VARCHAR(50) NOT NULL,
    Telefone INT NOT NULL,

    PRIMARY KEY(NIF),
    UNIQUE(Nome, Endereco, Telefone),
);

CREATE TABLE Farmaceutica (
    NumeroRegistoNacional INT NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Endereco VARCHAR(50) NOT NULL,
    Telefone INT NOT NULL,

    PRIMARY KEY(NumeroRegistoNacional),
    UNIQUE(Endereco, Telefone),
);

CREATE TABLE Farmaco (
    NomeComercial VARCHAR(50) NOT NULL,
    Formula varchar(200) NOT NULL,
    NIFFarmacia INT NOT NULL,
    NumeroRegistoNacionalFarmaceutica INT NOT NULL,

    PRIMARY KEY(NomeComercial),
    FOREIGN KEY(NIFFarmacia) REFERENCES Farmacia(NIF),
    FOREIGN KEY(NumeroRegistoNacionalFarmaceutica) REFERENCES farmaceutica(NumeroRegistoNacional),
    UNIQUE(Formula),
);

CREATE TABLE Prescricao (
    ID INT NOT NULL,
    [Data] DATE NOT NULL,
    IDSNSMedico INT NOT NULL,
    NumeroUtentePaciente INT NOT NULL,
    NomeComercialFarmaco VARCHAR(50) NOT NULL,
    NIFFarmacia INT NOT NULL,

    PRIMARY KEY(ID),
    FOREIGN KEY(IDSNSMedico) REFERENCES Medico(IDSNS),
    FOREIGN KEY(NumeroUtentePaciente) REFERENCES Paciente(NumeroUtente),
    FOREIGN KEY(NomeComercialFarmaco) REFERENCES Farmaco(NomeComercial),
    FOREIGN KEY(NIFFarmacia) REFERENCES Farmacia(NIF),
);