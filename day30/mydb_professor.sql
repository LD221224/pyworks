-- 교수와 학생의 관계 --

-- CREATE TABLE professor(
-- 	pid integer PRIMARY KEY,
-- 	name text NOT NULL,
-- 	major text NOT NULL
-- );

-- CREATE TABLE student(
-- 	sid char(4),
-- 	name text NOT NULL,
-- 	age integer,
-- 	pid integer NOT NULL,
-- 	PRIMARY KEY(sid),
-- 	FOREIGN KEY(pid) REFERENCES professor(pid)
-- );

-- 교수 추가
-- INSERT INTO professor VALUES(10, '고경희', '웹 프로그래밍');
-- INSERT INTO professor VALUES(11, '박응용', '파이썬 프로그래밍');

-- 학생 추가
-- INSERT INTO student VALUES('s101', '지민', 27, 10);
-- INSERT INTO student VALUES('s101', '지민', 27, 30);

-- 검색
SELECT * FROM professor;