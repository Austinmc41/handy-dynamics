DROP TABLE adk_session;
DROP TABLE bot_user;
DROP TABLE contractor;
DROP TABLE agent

CREATE TABLE bot_user
(
    user_id INT PRIMARY KEY,
    name TEXT,
    phone_no  VARCHAR(15),
    last_active TIMESTAMP,
    created_at TIMESTAMP
);

CREATE TABLE adk_session
(
    session_id INT PRIMARY KEY,
    created_at  TIMESTAMP,
    last_active  TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES bot_user(user_id)
);

CREATE TABLE contractor
(
contractor_id INT PRIMARY KEY,
name TEXT,
created_at TIMESTAMP,
email TEXT,
phone_no VARCHAR(15),
);

CREATE TABLE agent
(
id INT PRIMARY KEY,
created_at TIMESTAMP,
contractor_id INT

FOREIGN KEY contractor_id REFERENCES contractor(contractor_id)
);

CREATE INDEX idx_phone_no
ON bot_user(phone_no);

CREATE INDEX idx_phone_no
ON contractor(phone_no);

CREATE INDEX idx_contractor_id_agent
ON agent(contractor_id);
