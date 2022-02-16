-- 멤버 테이블 생성 --
/*
CREATE TABLE member(
	memberId	char(5) PRIMARY KEY,
	passwd		char(10) NOT NULL,
	name		TEXT NOT NULL,
	gender		char(4),
	age			INTEGER
	);
*/

-- 테이블 삭제
DROP TABLE member;	
	
-- 자료 삽입
-- INSERT INTO member VALUES('10001', 'm123456789', '지민', '남자', 30);

-- 자료 검색
-- SELECT * FROM member;

-- COMMIT;