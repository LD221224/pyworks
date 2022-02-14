# willdb.db에 접속
import sqlite3


def getconn():
    conn = sqlite3.connect("c:/mydb/willdb.db")
    return conn


def create_table():
    # member 테이블 생성
    conn = getconn()
    cur = conn.cursor()
    sql = """
            CREATE TABLE member(
                memberId	char(5) PRIMARY KEY,
                passwd		char(10) NOT NULL,
                name		TEXT NOT NULL,
                gender		char(4),
                age			INTEGER
            )
    """
    cur.execute(sql)
    conn.commit()
    print("member 테이블 생성")
    conn.close()


def select_member():
    conn = getconn()

    cur = conn.cursor()   # db 작업 객체
    # print("연결", conn)  # db 연결 확인

    # cur.execute("SELECT * FROM member")
    sql = "SELECT * FROM member"
    cur.execute(sql)

    rs = cur.fetchall()   # 리스트로 반환(값은 튜플)
    print(rs)

    conn.close()


def insert_member():
    # 회원 추가
    conn = getconn()
    cur = conn.cursor()
    # 정적(고정) 바인딩 형식
    # sql = "INSERT INTO member(memberId, passwd, name, gender, age) " \
    #       "VALUES('10002', 'm123456780', '민정', '여자', 24)"
    # cur.execute(sql)
    # 동적 바인딩 형식
    sql = "INSERT INTO member(memberId, passwd, name, gender, age) " \
          "VALUES(?, ?, ?, ?, ?)"
    cur.execute(sql, ('10003', 'm123456781', 'RM', '남자', 28))
    conn.commit()
    conn.close()


def select_one():
    # 1명 검색
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT memberId, passwd FROM member WHERE memberId = ?"
    cur.execute(sql, ('10003', ))   # 자료가 1개인 경우 콤마(,)를 붙임 - 튜플 자료 구조
    rs = cur.fetchone()
    print(rs)
    conn.close()


# 메인 영역
# create_table()
# insert_member()
# select_member()
select_one()