-- 1. UTILIZADORES (15 registos)

INSERT INTO utilizadores (username, nome, email, time) VALUES ('alice',  'Alice Ferreira',   'alice@email.pt',  '2023-01-10 09:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('bob',    'Bob Santos',       'bob@email.pt',    '2023-01-12 10:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('carol',  'Carol Mendes',     'carol@email.pt',  '2023-01-15 11:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('dave',   'Dave Oliveira',    'dave@email.pt',   '2023-01-20 08:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('eve',    'Eve Costa',        'eve@email.pt',    '2023-02-01 09:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('frank',  'Frank Rodrigues',  'frank@email.pt',  '2023-02-05 10:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('grace',  'Grace Pereira',    'grace@email.pt',  '2023-02-10 11:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('hugo',   'Hugo Carvalho',    'hugo@email.pt',   '2023-02-15 09:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('iris',   'Iris Sousa',       'iris@email.pt',   '2023-02-20 10:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('joao',   'João Martins',     'joao@email.pt',   '2023-03-01 11:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('lena',   'Lena Gomes',       'lena@email.pt',   '2023-03-05 09:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('mario',  'Mário Neves',      'mario@email.pt',  '2023-03-10 10:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('nuno',   'Nuno Pinto',       'nuno@email.pt',   '2023-03-15 11:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('olga',   'Olga Teixeira',    'olga@email.pt',   '2023-03-20 09:00:00+0000');
INSERT INTO utilizadores (username, nome, email, time) VALUES ('pedro',  'Pedro Lopes',      'pedro@email.pt',  '2023-04-01 10:00:00+0000');

-- 2. VIDEOS (12 registos)

INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (11111111-1111-1111-1111-111111111111, 'alice', 'Introdução ao Cassandra', 'Tutorial sobre modelação de dados em Cassandra', {'cassandra','nosql','database'},          '2024-01-10 10:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (22222222-2222-2222-2222-222222222222, 'bob',   'Python para Iniciantes',  'Aprende Python do zero',                        {'python','programação','iniciantes'},      '2024-01-11 09:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (33333333-3333-3333-3333-333333333333, 'alice', 'Docker em 10 Minutos',    'Introdução rápida ao Docker',                   {'docker','containers','devops'},           '2024-01-12 11:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (44444444-4444-4444-4444-444444444444, 'carol', 'Machine Learning Basics', 'Fundamentos de Machine Learning',               {'ml','ia','python'},                       '2024-01-13 14:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (55555555-5555-5555-5555-555555555555, 'dave',  'React do Zero',           'Aprende React desde o início',                  {'react','javascript','frontend'},          '2024-01-14 10:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (66666666-6666-6666-6666-666666666666, 'bob',   'PostgreSQL Avançado',     'Técnicas avançadas de PostgreSQL',              {'postgresql','sql','database'},            '2024-01-15 09:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (77777777-7777-7777-7777-777777777777, 'eve',   'Linux para Developers',   'Comandos Linux essenciais para devs',           {'linux','terminal','devops'},              '2024-01-16 11:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (88888888-8888-8888-8888-888888888888, 'carol', 'Git e GitHub',            'Controlo de versões com Git',                   {'git','github','versioning'},              '2024-01-17 10:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (99999999-9999-9999-9999-999999999999, 'alice', 'Kubernetes Basics',       'Orquestração de containers com Kubernetes',     {'kubernetes','k8s','devops'},              '2024-01-18 14:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, 'dave',  'Vue.js Crash Course',     'Aprende Vue.js rapidamente',                    {'vue','javascript','frontend'},            '2024-01-19 09:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb, 'eve',   'TypeScript Essentials',   'TypeScript para programadores JS',              {'typescript','javascript','programação'}, '2024-01-20 11:00:00+0000');
INSERT INTO videos (videoID, autor, nomeVideo, descricao, tags, timeUpload) VALUES (cccccccc-cccc-cccc-cccc-cccccccccccc, 'bob',   'Redis Caching',           'Cache com Redis em aplicações modernas',        {'redis','cache','backend'},               '2024-01-21 10:00:00+0000');

-- 3. VIDEO FOLLOWERS (20 registos)

INSERT INTO videoFollowers (videoID, username) VALUES (11111111-1111-1111-1111-111111111111, 'bob');
INSERT INTO videoFollowers (videoID, username) VALUES (11111111-1111-1111-1111-111111111111, 'carol');
INSERT INTO videoFollowers (videoID, username) VALUES (11111111-1111-1111-1111-111111111111, 'dave');
INSERT INTO videoFollowers (videoID, username) VALUES (22222222-2222-2222-2222-222222222222, 'alice');
INSERT INTO videoFollowers (videoID, username) VALUES (22222222-2222-2222-2222-222222222222, 'eve');
INSERT INTO videoFollowers (videoID, username) VALUES (33333333-3333-3333-3333-333333333333, 'frank');
INSERT INTO videoFollowers (videoID, username) VALUES (33333333-3333-3333-3333-333333333333, 'grace');
INSERT INTO videoFollowers (videoID, username) VALUES (44444444-4444-4444-4444-444444444444, 'hugo');
INSERT INTO videoFollowers (videoID, username) VALUES (44444444-4444-4444-4444-444444444444, 'iris');
INSERT INTO videoFollowers (videoID, username) VALUES (55555555-5555-5555-5555-555555555555, 'joao');
INSERT INTO videoFollowers (videoID, username) VALUES (55555555-5555-5555-5555-555555555555, 'lena');
INSERT INTO videoFollowers (videoID, username) VALUES (66666666-6666-6666-6666-666666666666, 'mario');
INSERT INTO videoFollowers (videoID, username) VALUES (77777777-7777-7777-7777-777777777777, 'nuno');
INSERT INTO videoFollowers (videoID, username) VALUES (77777777-7777-7777-7777-777777777777, 'olga');
INSERT INTO videoFollowers (videoID, username) VALUES (88888888-8888-8888-8888-888888888888, 'pedro');
INSERT INTO videoFollowers (videoID, username) VALUES (88888888-8888-8888-8888-888888888888, 'alice');
INSERT INTO videoFollowers (videoID, username) VALUES (99999999-9999-9999-9999-999999999999, 'bob');
INSERT INTO videoFollowers (videoID, username) VALUES (aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, 'carol');
INSERT INTO videoFollowers (videoID, username) VALUES (bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb, 'dave');
INSERT INTO videoFollowers (videoID, username) VALUES (cccccccc-cccc-cccc-cccc-cccccccccccc, 'eve');

-- 4. EVENTOS (20 registos)

INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('frank', 11111111-1111-1111-1111-111111111111, 'play',  '2024-01-15 10:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('frank', 11111111-1111-1111-1111-111111111111, 'pause', '2024-01-15 10:05:00+0000',  300);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('frank', 11111111-1111-1111-1111-111111111111, 'play',  '2024-01-15 10:06:00+0000',  300);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('frank', 11111111-1111-1111-1111-111111111111, 'stop',  '2024-01-15 10:20:00+0000',  1140);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('hugo',  22222222-2222-2222-2222-222222222222, 'play',  '2024-01-16 09:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('hugo',  22222222-2222-2222-2222-222222222222, 'pause', '2024-01-16 09:10:00+0000',  600);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('hugo',  22222222-2222-2222-2222-222222222222, 'stop',  '2024-01-16 09:30:00+0000',  1800);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('joao',  33333333-3333-3333-3333-333333333333, 'play',  '2024-01-17 14:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('joao',  33333333-3333-3333-3333-333333333333, 'stop',  '2024-01-17 14:10:00+0000',  600);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('lena',  44444444-4444-4444-4444-444444444444, 'play',  '2024-01-18 09:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('lena',  44444444-4444-4444-4444-444444444444, 'pause', '2024-01-18 09:15:00+0000',  900);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('lena',  44444444-4444-4444-4444-444444444444, 'stop',  '2024-01-18 09:45:00+0000',  2700);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('nuno',  55555555-5555-5555-5555-555555555555, 'play',  '2024-01-19 11:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('nuno',  55555555-5555-5555-5555-555555555555, 'stop',  '2024-01-19 11:25:00+0000',  1500);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('pedro', 66666666-6666-6666-6666-666666666666, 'play',  '2024-01-20 08:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('pedro', 66666666-6666-6666-6666-666666666666, 'pause', '2024-01-20 08:20:00+0000',  1200);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('pedro', 66666666-6666-6666-6666-666666666666, 'stop',  '2024-01-20 08:50:00+0000',  3000);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('bob',   77777777-7777-7777-7777-777777777777, 'play',  '2024-01-21 10:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('dave',  88888888-8888-8888-8888-888888888888, 'play',  '2024-01-22 14:00:00+0000',  0);
INSERT INTO eventos (username, videoID, tipoEvento, timeEvento, videoTime) VALUES ('dave',  88888888-8888-8888-8888-888888888888, 'stop',  '2024-01-22 14:15:00+0000',  900);

-- 5. RATINGS (20 registos)

INSERT INTO ratings (videoID, ratingID, rating) VALUES (11111111-1111-1111-1111-111111111111, 550e8400-e29b-11d4-a716-446655440001, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (11111111-1111-1111-1111-111111111111, 550e8400-e29b-11d4-a716-446655440002, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (11111111-1111-1111-1111-111111111111, 550e8400-e29b-11d4-a716-446655440003, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (22222222-2222-2222-2222-222222222222, 550e8400-e29b-11d4-a716-446655440004, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (22222222-2222-2222-2222-222222222222, 550e8400-e29b-11d4-a716-446655440005, 3);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (33333333-3333-3333-3333-333333333333, 550e8400-e29b-11d4-a716-446655440006, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (33333333-3333-3333-3333-333333333333, 550e8400-e29b-11d4-a716-446655440007, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (44444444-4444-4444-4444-444444444444, 550e8400-e29b-11d4-a716-446655440008, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (44444444-4444-4444-4444-444444444444, 550e8400-e29b-11d4-a716-446655440009, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (55555555-5555-5555-5555-555555555555, 550e8400-e29b-11d4-a716-446655440010, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (55555555-5555-5555-5555-555555555555, 550e8400-e29b-11d4-a716-446655440011, 3);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (66666666-6666-6666-6666-666666666666, 550e8400-e29b-11d4-a716-446655440012, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (66666666-6666-6666-6666-666666666666, 550e8400-e29b-11d4-a716-446655440013, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (77777777-7777-7777-7777-777777777777, 550e8400-e29b-11d4-a716-446655440014, 3);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (77777777-7777-7777-7777-777777777777, 550e8400-e29b-11d4-a716-446655440015, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (88888888-8888-8888-8888-888888888888, 550e8400-e29b-11d4-a716-446655440016, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (99999999-9999-9999-9999-999999999999, 550e8400-e29b-11d4-a716-446655440017, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, 550e8400-e29b-11d4-a716-446655440018, 5);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb, 550e8400-e29b-11d4-a716-446655440019, 4);
INSERT INTO ratings (videoID, ratingID, rating) VALUES (cccccccc-cccc-cccc-cccc-cccccccccccc, 550e8400-e29b-11d4-a716-446655440020, 3);

-- 6. VIDEOS POR AUTOR (12 registos)

INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('alice', '2024-01-10 10:00:00+0000', 11111111-1111-1111-1111-111111111111, 'Introdução ao Cassandra');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('alice', '2024-01-12 11:00:00+0000', 33333333-3333-3333-3333-333333333333, 'Docker em 10 Minutos');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('alice', '2024-01-18 14:00:00+0000', 99999999-9999-9999-9999-999999999999, 'Kubernetes Basics');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('bob',   '2024-01-11 09:00:00+0000', 22222222-2222-2222-2222-222222222222, 'Python para Iniciantes');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('bob',   '2024-01-15 09:00:00+0000', 66666666-6666-6666-6666-666666666666, 'PostgreSQL Avançado');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('bob',   '2024-01-21 10:00:00+0000', cccccccc-cccc-cccc-cccc-cccccccccccc, 'Redis Caching');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('carol', '2024-01-13 14:00:00+0000', 44444444-4444-4444-4444-444444444444, 'Machine Learning Basics');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('carol', '2024-01-17 10:00:00+0000', 88888888-8888-8888-8888-888888888888, 'Git e GitHub');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('dave',  '2024-01-14 10:00:00+0000', 55555555-5555-5555-5555-555555555555, 'React do Zero');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('dave',  '2024-01-19 09:00:00+0000', aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, 'Vue.js Crash Course');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('eve',   '2024-01-16 11:00:00+0000', 77777777-7777-7777-7777-777777777777, 'Linux para Developers');
INSERT INTO videosAutor (autor, timeUpload, videoID, nomeVideo) VALUES ('eve',   '2024-01-20 11:00:00+0000', bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb, 'TypeScript Essentials');

-- 7. COMENTARIOS POR UTILIZADOR (22 registos)

INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('alice', '2024-01-20 09:00:00+0000', 66666666-6666-6666-6666-666666666666, 'Ótimas dicas de performance.');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('bob',   '2024-01-21 10:00:00+0000', 77777777-7777-7777-7777-777777777777, 'Linux desmistificado!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('carol', '2024-01-21 11:00:00+0000', 77777777-7777-7777-7777-777777777777, 'Uso estes comandos todos os dias.');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('dave',  '2024-01-22 14:00:00+0000', 88888888-8888-8888-8888-888888888888, 'Git finalmente faz sentido!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('eve',   '2024-01-22 15:00:00+0000', 88888888-8888-8888-8888-888888888888, 'Perfeito para quem começa com Git.');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('frank', '2024-01-15 10:00:00+0000', 11111111-1111-1111-1111-111111111111, 'Excelente tutorial, muito claro!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('frank', '2024-01-17 15:00:00+0000', 33333333-3333-3333-3333-333333333333, 'Uso Docker há anos e aprendi coisas novas!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('frank', '2024-01-23 09:00:00+0000', 99999999-9999-9999-9999-999999999999, 'K8s explicado com clareza!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('grace', '2024-01-15 11:00:00+0000', 11111111-1111-1111-1111-111111111111, 'Aprendi muito, obrigada!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('grace', '2024-01-24 10:00:00+0000', aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, 'Vue é incrível, obrigado!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('hugo',  '2024-01-16 09:00:00+0000', 22222222-2222-2222-2222-222222222222, 'Melhor tutorial de Python que vi!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('hugo',  '2024-01-25 11:00:00+0000', bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb, 'TypeScript mudou a minha vida!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('iris',  '2024-01-16 10:00:00+0000', 22222222-2222-2222-2222-222222222222, 'Muito bom para iniciantes.');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('iris',  '2024-01-26 09:00:00+0000', cccccccc-cccc-cccc-cccc-cccccccccccc, 'Redis é poderoso!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('joao',  '2024-01-17 14:00:00+0000', 33333333-3333-3333-3333-333333333333, 'Docker explicado de forma simples.');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('joao',  '2024-01-27 10:00:00+0000', 11111111-1111-1111-1111-111111111111, 'Quando sai a parte 2?');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('lena',  '2024-01-18 09:00:00+0000', 44444444-4444-4444-4444-444444444444, 'Conteúdo fantástico sobre ML.');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('lena',  '2024-01-27 11:00:00+0000', 22222222-2222-2222-2222-222222222222, 'Precisava disto há muito tempo!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('mario', '2024-01-18 10:00:00+0000', 44444444-4444-4444-4444-444444444444, 'Muito didático, parabéns!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('nuno',  '2024-01-19 11:00:00+0000', 55555555-5555-5555-5555-555555555555, 'Finalmente percebo React!');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('olga',  '2024-01-19 12:00:00+0000', 55555555-5555-5555-5555-555555555555, 'Muito bem estruturado.');
INSERT INTO comentariosUser (username, timeComentario, videoID, comentario) VALUES ('pedro', '2024-01-20 08:00:00+0000', 66666666-6666-6666-6666-666666666666, 'PostgreSQL nunca foi tão claro!');

-- 8. COMENTARIOS POR VIDEO (22 registos)

INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (11111111-1111-1111-1111-111111111111, '2024-01-15 10:00:00+0000', 'frank', 'Excelente tutorial, muito claro!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (11111111-1111-1111-1111-111111111111, '2024-01-15 11:00:00+0000', 'grace', 'Aprendi muito, obrigada!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (11111111-1111-1111-1111-111111111111, '2024-01-27 10:00:00+0000', 'joao',  'Quando sai a parte 2?');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (22222222-2222-2222-2222-222222222222, '2024-01-16 09:00:00+0000', 'hugo',  'Melhor tutorial de Python que vi!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (22222222-2222-2222-2222-222222222222, '2024-01-16 10:00:00+0000', 'iris',  'Muito bom para iniciantes.');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (22222222-2222-2222-2222-222222222222, '2024-01-27 11:00:00+0000', 'lena',  'Precisava disto há muito tempo!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (33333333-3333-3333-3333-333333333333, '2024-01-17 14:00:00+0000', 'joao',  'Docker explicado de forma simples.');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (33333333-3333-3333-3333-333333333333, '2024-01-17 15:00:00+0000', 'frank', 'Uso Docker há anos e aprendi coisas novas!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (44444444-4444-4444-4444-444444444444, '2024-01-18 09:00:00+0000', 'lena',  'Conteúdo fantástico sobre ML.');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (44444444-4444-4444-4444-444444444444, '2024-01-18 10:00:00+0000', 'mario', 'Muito didático, parabéns!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (55555555-5555-5555-5555-555555555555, '2024-01-19 11:00:00+0000', 'nuno',  'Finalmente percebo React!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (55555555-5555-5555-5555-555555555555, '2024-01-19 12:00:00+0000', 'olga',  'Muito bem estruturado.');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (66666666-6666-6666-6666-666666666666, '2024-01-20 08:00:00+0000', 'pedro', 'PostgreSQL nunca foi tão claro!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (66666666-6666-6666-6666-666666666666, '2024-01-20 09:00:00+0000', 'alice', 'Ótimas dicas de performance.');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (77777777-7777-7777-7777-777777777777, '2024-01-21 10:00:00+0000', 'bob',   'Linux desmistificado!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (77777777-7777-7777-7777-777777777777, '2024-01-21 11:00:00+0000', 'carol', 'Uso estes comandos todos os dias.');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (88888888-8888-8888-8888-888888888888, '2024-01-22 14:00:00+0000', 'dave',  'Git finalmente faz sentido!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (88888888-8888-8888-8888-888888888888, '2024-01-22 15:00:00+0000', 'eve',   'Perfeito para quem começa com Git.');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (99999999-9999-9999-9999-999999999999, '2024-01-23 09:00:00+0000', 'frank', 'K8s explicado com clareza!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, '2024-01-24 10:00:00+0000', 'grace', 'Vue é incrível, obrigado!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb, '2024-01-25 11:00:00+0000', 'hugo',  'TypeScript mudou a minha vida!');
INSERT INTO comentariosVideo (videoID, timeComentario, username, comentario) VALUES (cccccccc-cccc-cccc-cccc-cccccccccccc, '2024-01-26 09:00:00+0000', 'iris',  'Redis é poderoso!');

-- 9. VIDEOS POR TAG (36 registos)

INSERT INTO videosTag (tag, videoID) VALUES ('cassandra', 11111111-1111-1111-1111-111111111111);
INSERT INTO videosTag (tag, videoID) VALUES ('nosql', 11111111-1111-1111-1111-111111111111);
INSERT INTO videosTag (tag, videoID) VALUES ('database', 11111111-1111-1111-1111-111111111111);
INSERT INTO videosTag (tag, videoID) VALUES ('python', 22222222-2222-2222-2222-222222222222);
INSERT INTO videosTag (tag, videoID) VALUES ('programação', 22222222-2222-2222-2222-222222222222);
INSERT INTO videosTag (tag, videoID) VALUES ('iniciantes', 22222222-2222-2222-2222-222222222222);
INSERT INTO videosTag (tag, videoID) VALUES ('docker', 33333333-3333-3333-3333-333333333333);
INSERT INTO videosTag (tag, videoID) VALUES ('containers', 33333333-3333-3333-3333-333333333333);
INSERT INTO videosTag (tag, videoID) VALUES ('devops', 33333333-3333-3333-3333-333333333333);
INSERT INTO videosTag (tag, videoID) VALUES ('ml', 44444444-4444-4444-4444-444444444444);
INSERT INTO videosTag (tag, videoID) VALUES ('ia', 44444444-4444-4444-4444-444444444444);
INSERT INTO videosTag (tag, videoID) VALUES ('python', 44444444-4444-4444-4444-444444444444);
INSERT INTO videosTag (tag, videoID) VALUES ('react', 55555555-5555-5555-5555-555555555555);
INSERT INTO videosTag (tag, videoID) VALUES ('javascript', 55555555-5555-5555-5555-555555555555);
INSERT INTO videosTag (tag, videoID) VALUES ('frontend', 55555555-5555-5555-5555-555555555555);
INSERT INTO videosTag (tag, videoID) VALUES ('postgresql', 66666666-6666-6666-6666-666666666666);
INSERT INTO videosTag (tag, videoID) VALUES ('sql', 66666666-6666-6666-6666-666666666666);
INSERT INTO videosTag (tag, videoID) VALUES ('database', 66666666-6666-6666-6666-666666666666);
INSERT INTO videosTag (tag, videoID) VALUES ('linux', 77777777-7777-7777-7777-777777777777);
INSERT INTO videosTag (tag, videoID) VALUES ('terminal', 77777777-7777-7777-7777-777777777777);
INSERT INTO videosTag (tag, videoID) VALUES ('devops', 77777777-7777-7777-7777-777777777777);
INSERT INTO videosTag (tag, videoID) VALUES ('git', 88888888-8888-8888-8888-888888888888);
INSERT INTO videosTag (tag, videoID) VALUES ('github', 88888888-8888-8888-8888-888888888888);
INSERT INTO videosTag (tag, videoID) VALUES ('versioning', 88888888-8888-8888-8888-888888888888);
INSERT INTO videosTag (tag, videoID) VALUES ('kubernetes', 99999999-9999-9999-9999-999999999999);
INSERT INTO videosTag (tag, videoID) VALUES ('k8s', 99999999-9999-9999-9999-999999999999);
INSERT INTO videosTag (tag, videoID) VALUES ('devops', 99999999-9999-9999-9999-999999999999);
INSERT INTO videosTag (tag, videoID) VALUES ('vue', aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa);
INSERT INTO videosTag (tag, videoID) VALUES ('javascript', aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa);
INSERT INTO videosTag (tag, videoID) VALUES ('frontend', aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa);
INSERT INTO videosTag (tag, videoID) VALUES ('typescript', bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb);
INSERT INTO videosTag (tag, videoID) VALUES ('javascript', bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb);
INSERT INTO videosTag (tag, videoID) VALUES ('programação', bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb);
INSERT INTO videosTag (tag, videoID) VALUES ('redis', cccccccc-cccc-cccc-cccc-cccccccccccc);
INSERT INTO videosTag (tag, videoID) VALUES ('cache', cccccccc-cccc-cccc-cccc-cccccccccccc);
INSERT INTO videosTag (tag, videoID) VALUES ('backend', cccccccc-cccc-cccc-cccc-cccccccccccc);

-- 10. RATINGS SUMMARY

UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = 11111111-1111-1111-1111-111111111111;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = 11111111-1111-1111-1111-111111111111;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = 11111111-1111-1111-1111-111111111111;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = 22222222-2222-2222-2222-222222222222;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 3, ratingCount = ratingCount + 1 WHERE videoID = 22222222-2222-2222-2222-222222222222;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = 33333333-3333-3333-3333-333333333333;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = 33333333-3333-3333-3333-333333333333;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = 44444444-4444-4444-4444-444444444444;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = 44444444-4444-4444-4444-444444444444;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = 55555555-5555-5555-5555-555555555555;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 3, ratingCount = ratingCount + 1 WHERE videoID = 55555555-5555-5555-5555-555555555555;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = 66666666-6666-6666-6666-666666666666;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = 66666666-6666-6666-6666-666666666666;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 3, ratingCount = ratingCount + 1 WHERE videoID = 77777777-7777-7777-7777-777777777777;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = 77777777-7777-7777-7777-777777777777;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = 88888888-8888-8888-8888-888888888888;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = 99999999-9999-9999-9999-999999999999;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 5, ratingCount = ratingCount + 1 WHERE videoID = aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 4, ratingCount = ratingCount + 1 WHERE videoID = bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb;
UPDATE ratingsSum SET ratingTotal = ratingTotal + 3, ratingCount = ratingCount + 1 WHERE videoID = cccccccc-cccc-cccc-cccc-cccccccccccc;

-- 12. PLAYLIST VIDEOS (10 registos)

INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (dddddddd-dddd-dddd-dddd-dddddddddddd, '2024-01-24 21:00:00+0000', 99999999-9999-9999-9999-999999999999, 'Kubernetes Basics', 'alice', 'frank');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (dddddddd-dddd-dddd-dddd-dddddddddddd, '2024-01-24 20:45:00+0000', 33333333-3333-3333-3333-333333333333, 'Docker em 10 Minutos', 'alice', 'frank');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (dddddddd-dddd-dddd-dddd-dddddddddddd, '2024-01-24 20:30:00+0000', 11111111-1111-1111-1111-111111111111, 'Introdução ao Cassandra', 'alice', 'frank');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (dddddddd-dddd-dddd-dddd-dddddddddddd, '2024-01-24 20:10:00+0000', 66666666-6666-6666-6666-666666666666, 'PostgreSQL Avançado', 'bob', 'frank');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (dddddddd-dddd-dddd-dddd-dddddddddddd, '2024-01-24 20:00:00+0000', 77777777-7777-7777-7777-777777777777, 'Linux para Developers', 'eve', 'frank');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee, '2024-01-25 09:30:00+0000', bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb, 'TypeScript Essentials', 'eve', 'grace');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee, '2024-01-25 09:20:00+0000', aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, 'Vue.js Crash Course', 'dave', 'grace');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee, '2024-01-25 09:10:00+0000', 55555555-5555-5555-5555-555555555555, 'React do Zero', 'dave', 'grace');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee, '2024-01-25 09:00:00+0000', 88888888-8888-8888-8888-888888888888, 'Git e GitHub', 'carol', 'grace');
INSERT INTO playlistVideos (playlistID, timeAdicao, videoID, nomeVideo, autor, addedBy) VALUES (eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee, '2024-01-25 08:50:00+0000', 22222222-2222-2222-2222-222222222222, 'Python para Iniciantes', 'bob', 'grace');

-- 13. Views de videos (12 registos)

UPDATE videoViewsByDay SET views = views + 1520 WHERE viewDate = '2024-01-10' AND videoID = 11111111-1111-1111-1111-111111111111;
UPDATE videoViewsByDay SET views = views + 3200 WHERE viewDate = '2024-01-10' AND videoID = 22222222-2222-2222-2222-222222222222;
UPDATE videoViewsByDay SET views = views + 870  WHERE viewDate = '2024-01-10' AND videoID = 33333333-3333-3333-3333-333333333333;
UPDATE videoViewsByDay SET views = views + 3840 WHERE viewDate = '2024-01-11' AND videoID = 22222222-2222-2222-2222-222222222222;
UPDATE videoViewsByDay SET views = views + 1100 WHERE viewDate = '2024-01-11' AND videoID = 44444444-4444-4444-4444-444444444444;
UPDATE videoViewsByDay SET views = views + 2560 WHERE viewDate = '2024-01-11' AND videoID = 55555555-5555-5555-5555-555555555555;
UPDATE videoViewsByDay SET views = views + 2760 WHERE viewDate = '2024-01-12' AND videoID = 33333333-3333-3333-3333-333333333333;
UPDATE videoViewsByDay SET views = views + 4100 WHERE viewDate = '2024-01-12' AND videoID = 88888888-8888-8888-8888-888888888888;
UPDATE videoViewsByDay SET views = views + 990  WHERE viewDate = '2024-01-12' AND videoID = 66666666-6666-6666-6666-666666666666;
UPDATE videoViewsByDay SET views = views + 5100 WHERE viewDate = '2024-01-13' AND videoID = 44444444-4444-4444-4444-444444444444;
UPDATE videoViewsByDay SET views = views + 2340 WHERE viewDate = '2024-01-13' AND videoID = 77777777-7777-7777-7777-777777777777;
UPDATE videoViewsByDay SET views = views + 1870 WHERE viewDate = '2024-01-13' AND videoID = bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb;
UPDATE videoViewsByDay SET views = views + 4230 WHERE viewDate = '2024-01-14' AND videoID = 55555555-5555-5555-5555-555555555555;
UPDATE videoViewsByDay SET views = views + 3010 WHERE viewDate = '2024-01-14' AND videoID = aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa;
UPDATE videoViewsByDay SET views = views + 1650 WHERE viewDate = '2024-01-14' AND videoID = cccccccc-cccc-cccc-cccc-cccccccccccc;
UPDATE videoViewsByDay SET views = views + 1980 WHERE viewDate = '2024-01-15' AND videoID = 66666666-6666-6666-6666-666666666666;
UPDATE videoViewsByDay SET views = views + 5430 WHERE viewDate = '2024-01-15' AND videoID = 11111111-1111-1111-1111-111111111111;
UPDATE videoViewsByDay SET views = views + 2200 WHERE viewDate = '2024-01-15' AND videoID = 99999999-9999-9999-9999-999999999999;
UPDATE videoViewsByDay SET views = views + 3310 WHERE viewDate = '2024-01-16' AND videoID = 77777777-7777-7777-7777-777777777777;
UPDATE videoViewsByDay SET views = views + 4890 WHERE viewDate = '2024-01-16' AND videoID = 44444444-4444-4444-4444-444444444444;
UPDATE videoViewsByDay SET views = views + 1420 WHERE viewDate = '2024-01-16' AND videoID = 22222222-2222-2222-2222-222222222222;
UPDATE videoViewsByDay SET views = views + 6750 WHERE viewDate = '2024-01-17' AND videoID = 88888888-8888-8888-8888-888888888888;
UPDATE videoViewsByDay SET views = views + 3100 WHERE viewDate = '2024-01-17' AND videoID = 55555555-5555-5555-5555-555555555555;
UPDATE videoViewsByDay SET views = views + 2780 WHERE viewDate = '2024-01-17' AND videoID = bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb;
UPDATE videoViewsByDay SET views = views + 2890 WHERE viewDate = '2024-01-18' AND videoID = 99999999-9999-9999-9999-999999999999;
UPDATE videoViewsByDay SET views = views + 4560 WHERE viewDate = '2024-01-18' AND videoID = 33333333-3333-3333-3333-333333333333;
UPDATE videoViewsByDay SET views = views + 1730 WHERE viewDate = '2024-01-18' AND videoID = 66666666-6666-6666-6666-666666666666;
UPDATE videoViewsByDay SET views = views + 4470 WHERE viewDate = '2024-01-19' AND videoID = aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa;
UPDATE videoViewsByDay SET views = views + 3850 WHERE viewDate = '2024-01-19' AND videoID = 77777777-7777-7777-7777-777777777777;
UPDATE videoViewsByDay SET views = views + 2010 WHERE viewDate = '2024-01-19' AND videoID = cccccccc-cccc-cccc-cccc-cccccccccccc;
UPDATE videoViewsByDay SET views = views + 3920 WHERE viewDate = '2024-01-20' AND videoID = bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb;
UPDATE videoViewsByDay SET views = views + 5670 WHERE viewDate = '2024-01-20' AND videoID = 88888888-8888-8888-8888-888888888888;
UPDATE videoViewsByDay SET views = views + 1340 WHERE viewDate = '2024-01-20' AND videoID = 11111111-1111-1111-1111-111111111111;
UPDATE videoViewsByDay SET views = views + 2150 WHERE viewDate = '2024-01-21' AND videoID = cccccccc-cccc-cccc-cccc-cccccccccccc;
UPDATE videoViewsByDay SET views = views + 4800 WHERE viewDate = '2024-01-21' AND videoID = aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa;
UPDATE videoViewsByDay SET views = views + 3390 WHERE viewDate = '2024-01-21' AND videoID = 99999999-9999-9999-9999-999999999999;

-- 14. HISTORICO DE VÍDEOS CONCLUIDOS POR UTILIZADOR (10 registos)

INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('frank', '2024-01-15 10:20:00+0000', 11111111-1111-1111-1111-111111111111, 'Introdução ao Cassandra', 100);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('frank', '2024-01-23 09:40:00+0000', 99999999-9999-9999-9999-999999999999, 'Kubernetes Basics', 96);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('grace', '2024-01-24 10:45:00+0000', aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa, 'Vue.js Crash Course', 99);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('hugo', '2024-01-16 09:30:00+0000', 22222222-2222-2222-2222-222222222222, 'Python para Iniciantes', 100);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('joao', '2024-01-17 14:10:00+0000', 33333333-3333-3333-3333-333333333333, 'Docker em 10 Minutos', 100);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('lena', '2024-01-18 09:45:00+0000', 44444444-4444-4444-4444-444444444444, 'Machine Learning Basics', 100);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('nuno', '2024-01-19 11:25:00+0000', 55555555-5555-5555-5555-555555555555, 'React do Zero', 100);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('pedro', '2024-01-20 08:50:00+0000', 66666666-6666-6666-6666-666666666666, 'PostgreSQL Avançado', 98);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('bob', '2024-01-21 10:35:00+0000', 77777777-7777-7777-7777-777777777777, 'Linux para Developers', 95);
INSERT INTO historicoVisionamentos (username, timeVisto, videoID, nomeVideo, percentagemVisionamento) VALUES ('dave', '2024-01-22 14:15:00+0000', 88888888-8888-8888-8888-888888888888, 'Git e GitHub', 100);
