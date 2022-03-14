# DB - 사원 관리
import sqlite3


# 전체 사원 검색
def select_emp():
    # DB 연결 객체
    conn = sqlite3.connect("c:/mydb/willdb.db")

    # 작업 객체
    cur = conn.cursor()

    # SQL 실행
    sql = "SELECT * FROM employee ORDER BY salary DESC"  # ASC 오름차순, DESC 내림차순
    cur.execute(sql)

    # 자료 가져오기 - rs : resultset, fetchall() : Fetches all rows from the resultset
    rs = cur.fetchall()

    # print(rs)
    for i in rs:
        print(i)

    # 연결 종료
    conn.close()


# 사원 추가
def insert_emp():
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "INSERT INTO employee(emp_id, name, age) VALUES('e102', '안산', 21)"
    cur.execute(sql)
    # COMMIT 실행 필수
    conn.commit()
    conn.close()


# 특정 사원 검색
def select_one():
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE emp_id = 'e101'"
    cur.execute(sql)
    # fetchone() : Fetches one row from the resultset.
    rs = cur.fetchone()
    print(rs)
    conn.close()


# 사원 정보 수정
def update_emp():
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "UPDATE employee SET salary = 10000 WHERE name = '안산'"
    cur.execute(sql)
    conn.commit()
    conn.close()


# 사원 삭제
def delete_emp():
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE emp_id = 'e103'"
    cur.execute(sql)
    conn.commit()
    conn.close()


# insert_emp()
# select_one()
# update_emp()
# delete_emp()
select_emp()
