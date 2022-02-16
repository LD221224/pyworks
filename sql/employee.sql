-- 사원 테이블 만들기
/*
CREATE TABLE employee(
	emp_id	char(10) PRIMARY KEY,
	name TEXT NOT NULL,
	age	INTEGER,
	salary INTEGER
)
*/

-- 칼럼 명 : 사번, 이름, 나이, 급여(달러)
-- PRIMARY KEY : 기본키(중복 방지, NOT NULL)
-- NOT NULL : 비어있지 않게 함



-- 자료 추가 : INSERT INTO 테이블이름(칼럼명) VALUES(값)
-- INSERT INTO employee VALUES('e101', '추신수', 39, 10000);
-- INSERT INTO employee(emp_id, name, age) VALUES('e102', '안산', 21);
-- INSERT INTO employee VALUES('e103', '손흥민', 30, 20000);

-- 실행 완료 : 자료의 삽입, 수정, 삭제 시 변경사항 저장하기, 반드시 실행
-- COMMIT;	



-- 자료 검색 : SELECT 칼럼명 FROM 테이블이름
-- SELECT * FROM employee;

-- 특정 칼럼 검색
-- SELECT emp_id, name FROM employee;

-- 특정 자료 검색 : SELECT 칼럼명 FROM 테이블이름 WHERE 칼럼명 = 값
-- SELECT * FROM employee WHERE emp_id = 'e101';

-- 정렬하여 검색 : ORDER BY 칼럼명 DESC 내림차순, 생략 / ASC 오름차순
SELECT * FROM employee ORDER BY salary;



-- 자료 수정 : UPDATE 테이블이름 SET 칼럼명 = 값 WHERE 칼럼명 = 값
-- UPDATE employee SET salary = 30000 WHERE emp_id = 'e101';



-- 자료 삭제
-- DELETE FROM employee;

-- 특정 자료 삭제 : DELETE FROM 테이블이름 WHERE 칼럼명 = 값
-- DELETE FROM employee WHERE emp_id = 'e102'

-- COMMIT 전에 실행하면 복구됨
-- ROLLBACK;
