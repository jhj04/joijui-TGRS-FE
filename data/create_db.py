import sqlite3
import csv

# 데이터베이스 연결
conn = sqlite3.connect('site.db')
cur = conn.cursor()

# 테이블 생성
# 사기사이트링크(링크(PK))
cur.execute('''
    CREATE TABLE IF NOT EXISTS sites (
        link TEXT PRIMARY KEY,
    )
''')

# 회원(회원번호, 이름, 핸드폰번호, 이메일, 비밀번호, 등록일, 포인트)
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT,
        password TEXT,
        registration_date TEXT,
        points INTEGER
    )
''')

# 리뷰(회원번호, 링크, 리뷰)
cur.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        user_id INTEGER,
        link TEXT,
        review TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (link) REFERENCES sites(link)
    )
''')

# CSV 파일 읽기 및 데이터 삽입
with open('site.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        cur.execute('''
            INSERT INTO sites (link)
            VALUES (?)
        ''', (row[0],))
        print(row)

# 변경사항 저장 및 데이터베이스 연결 종료
conn.commit()
conn.close()
print("Data has been inserted into the database.")
