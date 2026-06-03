-- 1. UTILIZADORES
CREATE TABLE utilizadores (username TEXT, nome TEXT, email TEXT, time TIMESTAMP, PRIMARY KEY (username));

-- 2. VIDEOS
CREATE TABLE videos (videoID UUID, autor TEXT, nomeVideo TEXT, descricao TEXT, tags SET<TEXT>, timeUpload TIMESTAMP, PRIMARY KEY (videoID));

CREATE INDEX IF NOT EXISTS ind_tag ON videos(tags);

-- 3. VIDEO FOLLOWERS
CREATE TABLE videoFollowers (username TEXT, videoID UUID, PRIMARY KEY (videoID, username));

-- 4. EVENTOS 
CREATE TABLE eventos (username TEXT, videoID UUID, timeEvento TIMESTAMP, tipoEvento TEXT, videoTime INT, PRIMARY KEY (username, videoID, timeEvento)) WITH CLUSTERING ORDER BY (videoID ASC, timeEvento DESC);

CREATE INDEX IF NOT EXISTS idx_eventos_tipo ON eventos(tipoEvento);

-- 5. RATINGS
CREATE TABLE ratings (videoID UUID, ratingID TIMEUUID, rating INT, PRIMARY KEY (videoID, ratingID));

-- 6. VIDEOS POR AUTOR
CREATE TABLE videosAutor (autor TEXT, timeUpload TIMESTAMP, videoID UUID, nomeVideo TEXT, PRIMARY KEY (autor, timeUpload, videoID)) WITH CLUSTERING ORDER BY (timeUpload DESC);

-- 7. COMENTARIOS POR UTILIZADOR
CREATE TABLE comentariosUser (username TEXT, timeComentario TIMESTAMP, videoID UUID, comentario TEXT, PRIMARY KEY (username, timeComentario)) WITH CLUSTERING ORDER BY (timeComentario DESC);

-- 8. COMENTARIOS POR VIDEO
CREATE TABLE comentariosVideo (videoID UUID, timeComentario TIMESTAMP, username TEXT, comentario TEXT, PRIMARY KEY (videoID, timeComentario)) WITH CLUSTERING ORDER BY (timeComentario DESC);

-- 9. RATINGS SUMMARY
CREATE TABLE ratingsSum (videoID UUID, ratingTotal COUNTER, ratingCount COUNTER, PRIMARY KEY (videoID));

-- 10. VIDEOS POR TAG 
CREATE TABLE videosTag (tag TEXT, videoID UUID, PRIMARY KEY (tag, videoID));
