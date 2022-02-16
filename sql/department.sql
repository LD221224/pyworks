-- 관계 --
-- 부서 테이블 --
/*
CREATE TABLE department(
	deptId		integer PRIMARY KEY,-- 부서 번호
	deptName	text NOT NULL,		-- 부서 이름
	location	text NOT NULL		-- 사무실 위치
);
*/

-- 사원 테이블 --
/*
CREATE TABLE employee(
	empId	integer PRIMARY KEY,
	name	text NOT NULL,
	age		integer,
	deptId	integer,
	FOREIGN KEY(deptId) REFERENCES department(deptId)	-- 외래키 설정
);
*/

-- 테이블 삭제
-- DROP TABLE department;

-- 부서 추가
-- INSERT INTO department VALUES(10, '전산팀', '서울');
-- INSERT INTO department VALUES(20, '관리팀', '인천');

-- 사원 추가
-- INSERT INTO employee VALUES(101, '민정', 24, 10);
-- INSERT INTO employee VALUES(102, '지민', 27, 20);

-- 부서코드가 없으므로 외래키 제약사항 위반(에러)
-- FOREIGN KEY constraint failed 
-- INSERT INTO employee VALUES(103, 'RM', 28, 30);	

-- 검색
-- SELECT * FROM department;
SELECT * FROM employee; 

-- 삭제
-- 다른(참조) 테이블에서 부서코드를 사용하므로 외래키 제약조건 위배
-- FOREIGN KEY constraint failed
-- DELETE FROM department WHERE deptId = 20;