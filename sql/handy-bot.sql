DROP TABLE adk_session;
DROP TABLE bot_user;

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

CREATE INDEX idx_phone_no
ON bot_user(phone_no);
