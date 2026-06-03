-- 1. Agenda de um paciente num período
SELECT id_paciente, data, tipo_consulta, estado, sala FROM consultas WHERE id_paciente = 11111111-1111-1111-1111-111111111111 AND data >= '2025-03-01 00:00:00' AND data <= '2025-04-30 23:59:59' ORDER BY data ASC;

-- 2. BMI de pacientes
SELECT nome, peso, altura, bmi(peso, altura) AS imc FROM pacientes WHERE id = 55555555-5555-5555-5555-555555555555;

-- 3. Número de dias internado - p1
SELECT id, nome, numero_dias(data_entrada, data_saida) FROM pacientes WHERE id = 44444444-4444-4444-4444-444444444444;

-- 3. Visitas do mesmo paciente - p2
SELECT data, numero_pessoas, nome_relacao, duracao FROM visitas WHERE id_paciente = 44444444-4444-4444-4444-444444444444 ORDER BY data DESC LIMIT 5;

-- 5. Média geral de duração de consultas
SELECT media_duracao_consultas(duracao) FROM consultas;

-- 6. Medico da Medicina Interna
SELECT nome, telefone, email FROM medicos WHERE departamento = 'Medicina Interna';

-- 7. Média de pessoas por visita de um paciente
SELECT media_visitas_por_dia(numero_pessoas) FROM visitas WHERE id_paciente = 88888888-8888-8888-8888-888888888888;

-- 8. Número de consultas de um paciente
SELECT id_medico, id_paciente, COUNT(*) FROM consultas WHERE id_paciente = 11111111-1111-1111-1111-111111111111;

-- 9. Medico inativo
SELECT nome, telefone, email FROM medicos WHERE estado = 'inativo';

-- 10. Todas as consultas de urgência
SELECT id_paciente, data, diagnostico, sala FROM consultas WHERE tipo_consulta = 'urgência';
