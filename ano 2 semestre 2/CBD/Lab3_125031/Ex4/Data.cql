-- PACIENTES
INSERT INTO pacientes (id, nome, sexo, idade, altura, peso, doenca, telefone, data_entrada, data_saida)
VALUES (11111111-1111-1111-1111-111111111111, 'Ana Ferreira', 'F', 45, 1.62, 68.5, {'diabetes tipo 2', 'hipertensão'}, 912345678, '2025-03-01 08:00:00', '2025-03-10 11:00:00');

INSERT INTO pacientes (id, nome, sexo, idade, altura, peso, doenca, telefone, data_entrada, data_saida)
VALUES (44444444-4444-4444-4444-444444444444, 'Miguel Costa', 'M', 38, 1.80, 90.2, {'hérnia discal'}, 915678901, '2025-03-20 10:00:00', null);

INSERT INTO pacientes (id, nome, sexo, idade, altura, peso, doenca, telefone, data_entrada, data_saida)
VALUES (55555555-5555-5555-5555-555555555555, 'Beatriz Santos', 'F', 71, 1.58, 63.0, {'artrite reumatoide', 'osteoporose', 'hipertensão'}, 916789012, '2025-03-22 08:15:00', null);

INSERT INTO pacientes (id, nome, sexo, idade, altura, peso, doenca, telefone, data_entrada, data_saida)
VALUES (88888888-8888-8888-8888-888888888888, 'Fernando Pinto', 'M', 66, 1.70, 75.0, {'DPOC', 'insuficiência respiratória'}, 919012345, '2025-04-07 09:00:00', null);


-- MEDICOS
INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a1111111-1111-1111-1111-111111111111, 'Dr. João Pereira', 'Cardiologia', 'Cardiologia', 961000001, 'joao.pereira@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a2222222-2222-2222-2222-222222222222, 'Dra. Marta Oliveira', 'Anestesiologia', 'Bloco Operatório', 961000002, 'marta.oliveira@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a3333333-3333-3333-3333-333333333333, 'Dr. Ricardo Silva', 'Ortopedia', 'Ortopedia', 961000003, 'ricardo.silva@hospital.pt', 'férias');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a4444444-4444-4444-4444-444444444444, 'Dra. Filipa Torres', 'Neurologia', 'Neurologia', 961000004, 'filipa.torres@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a5555555-5555-5555-5555-555555555555, 'Dr. Nuno Baptista', 'Cirurgia Geral', 'Cirurgia', 961000005, 'nuno.baptista@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a6666666-6666-6666-6666-666666666666, 'Dra. Cláudia Reis', 'Endocrinologia', 'Medicina Interna', 961000006, 'claudia.reis@hospital.pt', 'inativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a7777777-7777-7777-7777-777777777777, 'Dr. Hugo Fernandes', 'Pneumologia', 'Pneumologia', 961000007, 'hugo.fernandes@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a8888888-8888-8888-8888-888888888888, 'Dra. Vera Castro', 'Medicina Interna', 'Medicina Interna', 961000008, 'vera.castro@hospital.pt', 'licenciatura');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (a9999999-9999-9999-9999-999999999999, 'Dr. Sérgio Monteiro', 'Gastrenterologia', 'Gastrenterologia', 961000009, 'sergio.monteiro@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (b1111111-1111-1111-1111-111111111111, 'Dra. Ana Lopes', 'Psiquiatria', 'Psiquiatria', 961000010, 'ana.lopes@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (b2222222-2222-2222-2222-222222222222, 'Dr. Luís Correia', 'Reumatologia', 'Reumatologia', 961000011, 'luis.correia@hospital.pt', 'férias');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (b3333333-3333-3333-3333-333333333333, 'Dra. Sandra Fonseca', 'Dermatologia', 'Dermatologia', 961000012, 'sandra.fonseca@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (b4444444-4444-4444-4444-444444444444, 'Dr. Pedro Azevedo', 'Urgência', 'Urgência', 961000013, 'pedro.azevedo@hospital.pt', 'ativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (b5555555-5555-5555-5555-555555555555, 'Dra. Raquel Nogueira', 'Oncologia', 'Oncologia', 961000014, 'raquel.nogueira@hospital.pt', 'inativo');

INSERT INTO medicos (id, nome, especializacao, departamento, telefone, email, estado)
VALUES (b6666666-6666-6666-6666-666666666666, 'Dr. António Vieira', 'Nefrologia', 'Nefrologia', 961000015, 'antonio.vieira@hospital.pt', 'ativo');


-- CONSULTAS/OPERACOES
INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (11111111-1111-1111-1111-111111111111, a1111111-1111-1111-1111-111111111111, '2025-03-01 10:00:00', 30, 'rotina', ['Metformina 500mg', 'Losartan 50mg'], 'Diabetes controlada', 'Paciente estável', 'realizada', 'Consulta 1', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (11111111-1111-1111-1111-111111111111, a1111111-1111-1111-1111-111111111111, '2025-03-08 10:30:00', 25, 'seguimento', ['Metformina 500mg'], 'Controlo glicémico em melhoria', 'Ajuste de alimentação recomendado', 'realizada', 'Consulta 1', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (44444444-4444-4444-4444-444444444444, a3333333-3333-3333-3333-333333333333, '2025-03-20 11:00:00', 60, 'pré-operatória', ['Ibuprofeno 400mg', 'Omeprazol 20mg'], 'Hérnia discal L4-L5', 'Candidato a cirurgia', 'realizada', 'Consulta 5', 'alta');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (44444444-4444-4444-4444-444444444444, a5555555-5555-5555-5555-555555555555, '2025-03-25 08:30:00', 120, 'operação', ['Morfina 10mg pós-op', 'Paracetamol 1g'], 'Microdiscectomia L4-L5', 'Operação sem complicações', 'realizada', 'Bloco 1', 'alta');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (55555555-5555-5555-5555-555555555555, b2222222-2222-2222-2222-222222222222, '2025-03-23 10:30:00', 40, 'rotina', ['Metotrexato 7.5mg', 'Ácido fólico 5mg'], 'Artrite reumatoide ativa', 'Resposta parcial ao tratamento', 'realizada', 'Consulta 4', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (55555555-5555-5555-5555-555555555555, b2222222-2222-2222-2222-222222222222, '2025-04-02 10:00:00', 35, 'seguimento', ['Metotrexato 10mg', 'Ácido fólico 5mg'], 'Artrite reumatoide moderada', 'Queixas de dor matinal', 'realizada', 'Consulta 4', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (88888888-8888-8888-8888-888888888888, a7777777-7777-7777-7777-777777777777, '2025-04-07 10:00:00', 50, 'internamento', ['Broncodilatador nebulizado', 'Prednisolona 40mg'], 'Exacerbação DPOC', 'Internamento necessário', 'realizada', 'Consulta 6', 'alta');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (88888888-8888-8888-8888-888888888888, a7777777-7777-7777-7777-777777777777, '2025-04-09 11:30:00', 30, 'urgência', ['Salbutamol inalador', 'Prednisolona 20mg'], 'Dispneia aguda em contexto de DPOC', 'Melhoria após nebulização', 'realizada', 'Urgência 1', 'alta');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (11111111-1111-1111-1111-111111111111, a6666666-6666-6666-6666-666666666666, '2025-03-09 09:00:00', 20, 'rotina', ['Metformina 500mg'], 'Hiperglicemia leve', 'Mantém plano terapêutico', 'realizada', 'Consulta 2', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (11111111-1111-1111-1111-111111111111, a1111111-1111-1111-1111-111111111111, '2025-03-10 10:00:00', 30, 'seguimento', ['Metformina 850mg', 'Losartan 50mg'], 'Diabetes estabilizada', 'Sem eventos adversos', 'realizada', 'Consulta 1', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (44444444-4444-4444-4444-444444444444, a5555555-5555-5555-5555-555555555555, '2025-03-27 09:00:00', 25, 'pós-operatória', ['Paracetamol 1g'], 'Recuperação pós cirurgia', 'Ferida operatória limpa', 'realizada', 'Consulta 5', 'alta');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (44444444-4444-4444-4444-444444444444, a3333333-3333-3333-3333-333333333333, '2025-04-03 10:30:00', 30, 'seguimento', ['Fisioterapia lombar'], 'Melhoria da mobilidade', 'Iniciar reabilitação', 'realizada', 'Consulta 5', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (55555555-5555-5555-5555-555555555555, b2222222-2222-2222-2222-222222222222, '2025-04-06 09:30:00', 35, 'seguimento', ['Metotrexato 10mg', 'Ácido fólico 5mg'], 'Dor articular persistente', 'Reforço de exercício leve', 'realizada', 'Consulta 4', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (55555555-5555-5555-5555-555555555555, b2222222-2222-2222-2222-222222222222, '2025-04-12 10:30:00', 40, 'rotina', ['Metotrexato 12.5mg', 'Prednisona 5mg'], 'Artrite em vigilância', 'Ajuste terapêutico', 'realizada', 'Consulta 4', 'normal');

INSERT INTO consultas (id_paciente, id_medico, data, duracao, tipo_consulta, prescricao, diagnostico, observacoes, estado, sala, prioridade)
VALUES (88888888-8888-8888-8888-888888888888, a7777777-7777-7777-7777-777777777777, '2025-04-12 11:00:00', 45, 'seguimento', ['Tiotrópio 18mcg', 'Prednisolona 10mg'], 'DPOC com melhoria clínica', 'Sem necessidade de internamento', 'realizada', 'Consulta 6', 'normal');

-- VISITAS
INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (11111111-1111-1111-1111-111111111111, '2025-03-02 15:00:00', 2, {'Pedro Ferreira': 'marido', 'Joana Ferreira': 'filha'}, 45);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (11111111-1111-1111-1111-111111111111, '2025-03-05 16:00:00', 1, {'Pedro Ferreira': 'marido'}, 30);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (44444444-4444-4444-4444-444444444444, '2025-03-21 17:00:00', 2, {'Sara Costa': 'esposa', 'Tomás Costa': 'filho'}, 50);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (55555555-5555-5555-5555-555555555555, '2025-03-24 15:30:00', 2, {'Alberto Santos': 'marido', 'Rita Santos': 'neta'}, 40);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (55555555-5555-5555-5555-555555555555, '2025-03-26 16:00:00', 3, {'Alberto Santos': 'marido', 'Rita Santos': 'neta', 'Marta Santos': 'filha'}, 50);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (88888888-8888-8888-8888-888888888888, '2025-04-08 17:30:00', 3, {'Alice Pinto': 'esposa', 'Gonçalo Pinto': 'filho', 'Marta Pinto': 'filha'}, 55);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (44444444-4444-4444-4444-444444444444, '2025-04-01 17:00:00', 1, {'Sara Costa': 'esposa'}, 40);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (88888888-8888-8888-8888-888888888888, '2025-04-10 16:00:00', 2, {'Alice Pinto': 'esposa', 'Gonçalo Pinto': 'filho'}, 35);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (11111111-1111-1111-1111-111111111111, '2025-03-07 15:30:00', 2, {'Pedro Ferreira': 'marido', 'Carolina Ferreira': 'neta'}, 35);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (11111111-1111-1111-1111-111111111111, '2025-03-09 17:00:00', 1, {'Joana Ferreira': 'filha'}, 25);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (44444444-4444-4444-4444-444444444444, '2025-03-28 16:30:00', 2, {'Sara Costa': 'esposa', 'Tomás Costa': 'filho'}, 45);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (44444444-4444-4444-4444-444444444444, '2025-04-04 18:00:00', 1, {'Sara Costa': 'esposa'}, 30);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (55555555-5555-5555-5555-555555555555, '2025-04-05 15:00:00', 2, {'Alberto Santos': 'marido', 'Rita Santos': 'neta'}, 40);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (55555555-5555-5555-5555-555555555555, '2025-04-13 16:15:00', 1, {'Marta Santos': 'filha'}, 30);

INSERT INTO visitas (id_paciente, data, numero_pessoas, nome_relacao, duracao)
VALUES (88888888-8888-8888-8888-888888888888, '2025-04-12 17:00:00', 3, {'Alice Pinto': 'esposa', 'Gonçalo Pinto': 'filho', 'Marta Pinto': 'filha'}, 50);




-- UPDATE
UPDATE pacientes SET doenca = doenca + {'hipertensão'}  WHERE id = 88888888-8888-8888-8888-888888888888;

UPDATE consultas SET prescricao = prescricao + ['Ibuprofeno 400mg'] WHERE id_paciente = 44444444-4444-4444-4444-444444444444 AND data = '2025-03-27 09:00:00';

UPDATE visitas SET nome_relacao = nome_relacao + {'Carolina Ferreira': 'neta'} WHERE id_paciente = 11111111-1111-1111-1111-111111111111 AND data = '2025-03-02 15:00:00';

UPDATE visitas SET nome_relacao = nome_relacao - {'Joana Ferreira'} WHERE id_paciente = 11111111-1111-1111-1111-111111111111 AND data = '2025-03-02 15:00:00';

UPDATE visitas SET nome_relacao['Carolina Ferreira'] = 'bisneta' WHERE id_paciente = 11111111-1111-1111-1111-111111111111 AND data = '2025-03-02 15:00:00';



-- DELETE

DELETE doenca['osteoporose'] FROM pacientes WHERE id = 55555555-5555-5555-5555-555555555555;

DELETE prescricao[1] FROM consultas WHERE id_paciente = 55555555-5555-5555-5555-555555555555 AND data = '2025-04-02 10:00:00';

DELETE nome_relacao['Marta Santos'] FROM visitas WHERE id_paciente = 55555555-5555-5555-5555-555555555555 AND data = '2025-03-26 16:00:00';

DELETE prescricao[0] FROM consultas WHERE id_paciente = 44444444-4444-4444-4444-444444444444 AND data = '2025-03-27 09:00:00';

DELETE nome_relacao['Carolina Ferreira'] = 'bisneta' FROM visitas WHERE id_paciente = 11111111-1111-1111-1111-111111111111 AND data = '2025-03-02 15:00:00';
