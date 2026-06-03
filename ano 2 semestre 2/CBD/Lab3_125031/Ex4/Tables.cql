-- PACIENTES
CREATE TABLE pacientes (id UUID, nome TEXT, sexo TEXT, idade INT, altura FLOAT, peso FLOAT, doenca SET<TEXT>, telefone INT, data_entrada TIMESTAMP, data_saida TIMESTAMP, PRIMARY KEY(id));
CREATE INDEX ind_pacientes_nome ON pacientes (nome);

-- MEDICOS
CREATE TABLE medicos (id UUID, nome TEXT, especializacao TEXT, departamento TEXT, telefone INT, email TEXT, estado TEXT, PRIMARY KEY(id));
CREATE INDEX ind_medicos_especializacao ON medicos (especializacao);
CREATE INDEX ind_medicos_departamento ON medicos (departamento);
CREATE INDEX ind_medicos_estado ON medicos (estado);

-- CONSULTAS/OPERACOES 
CREATE TABLE consultas (id_paciente UUID, id_medico UUID, data TIMESTAMP, duracao INT, tipo_consulta TEXT, prescricao LIST<TEXT>,diagnostico TEXT, observacoes TEXT, estado TEXT, sala TEXT, prioridade TEXT,  PRIMARY KEY((id_paciente), data)) WITH CLUSTERING ORDER BY (data DESC);
CREATE INDEX ind_consultas_medico ON consultas (id_medico);
CREATE INDEX ind_consultas_estado ON consultas (estado);
CREATE INDEX ind_consultas_tipo ON consultas (tipo_consulta);

-- VISITAS
CREATE TABLE visitas (id_paciente UUID, numero_pessoas INT, data TIMESTAMP, nome_relacao MAP<TEXT, TEXT>, duracao INT, PRIMARY KEY ((id_paciente), data)) WITH CLUSTERING ORDER BY (data DESC);
