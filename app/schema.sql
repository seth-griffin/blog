use blog;

DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
  id INTEGER NOT NULL AUTO_INCREMENT,
  title VARCHAR(64) NOT NULL,
  posted_on DATE,
  content TEXT,
  url_path varchar(64) DEFAULT NULL,
  CONSTRAINT pk_post PRIMARY KEY (id)
); ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
