"CREATE TABLE student(name VARCHAR(50) NOT NULL,\
           birth INT(4),team VARCHAR(30),\
           phone VARCHAR(11),\
           address VARCHAR(30))engine=innoDB default charset=utf8;",

import datetime, time
import pymysql
# 함수(모듈)
# 공통사용
# 데이터베이스 연결함수
def connect_db() :
    u = 'root'
    p = '0000'
    db = 'test'
    connect = pymysql.connect(host = 'localhost', user = u, passwd = p, db = db, charset = 'utf8')
    return (connect)

# 출력함수
def print_result(result) :
    print("\n-------------------------------------------------------------------")
    title = ['이름', '출생년도', '소속', '전화번호', '거주지']
    for t in title : # 필드명출력
        print(t.center(8,' '),end='\t')

    print("\n-------------------------------------------------------------------")
    keys=['name','birth','team','phone','address']

    # 검색해서 넘어온 결과 리스트의 원소들을 하나씩 출력
    for row in result :
        for k in keys :
            print(str(row[k]).center(8,' '),end='\t')
        print("")
        print('-----------------------------------------------------------------')


# 관리자 사용
def create_db() :
    try :
        sql = ['DROP DATABASE IF EXISTS test;', 'CREATE DATABASE test;','SHOW DATABASES;']
        db_conn = connect_db()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor) # dbms에서 반환되는 레코드를 딕셔너리 형태로 제공
        # 커서 형태를 선택할 수 있다는 점, 기본은 튜플 형태
        for s in sql :
            cursor.execute(s)
            result = cursor.fetchall()
        for r in result :
            print (r)
        db_conn.close()
    except Exception as e :
        print(e)


def create_table() :
    db_conn = connect_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    sql = ["use test;",
                "CREATE TABLE student(name VARCHAR(50) NOT NULL,\
                birth INT(4),\
                team VARCHAR(30),\
                phone VARCHAR(11),\
                address VARCHAR(30))engine=innoDB default charset=utf8;",
                "SHOW TABLES;"     ]
    for s in sql :
        cursor.execute(s)
        result = cursor.fetchall()

    for r in result :
        print(r)
    db_conn.close()
    return
#쿼리 구문은 "" 사용이 일반적

# 관리자가 사용할 DB, TABLE 생성함수 생성
# create_db()
# create_table()

# 기능합수
# 1번, 2번 담당
def select(query) :
    db_conn = connect_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    print_result(result)
    db_conn.close()
    return

# 3,4,5번 기능 담당
def dml_exec(query, values) :
    try :
        db_conn = connect_db()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query,values)
        result = cursor.fetchall()
        db_conn.commit()
    except Exception as e :
        print(e)
        db_conn.rollback()
    finally:
        db_conn.close()



cmd = 'na' # 사용자에게 명령어를 입력받기 위해 선언
while cmd != 'q' : # while True
    print('\n*** 사용가능 메뉴 ***')
    print('a : 모든 데이터 조회(all)')
    print('f : 조건에 맞는 데이터 조회(find)')
    print('i : 수강생 입력(insert)')
    print('d : 수강생 삭제(delete)')
    print('r : 정보변경(update)')
    print('q : 종료(quit) \n')

    cmd = input('메뉴 입력 : ')

    if cmd == 'a' :
        sql = 'SELECT * FROM student' # 모든 수강생 검색
        select(sql)

    elif cmd == 'f' :
        print("검색할 기준 입력(이름/나이/소속/전화번호/거주지) : ")
        col = input('> ')
        # 검색 처리 코드
        if col == '이름' :
            name = input('\n 검색할 수강생 이름은? : ')
            sql = "SELECT * FROM student WHERE name = '{}'".format(name)
            print(sql)
            select(sql)
        elif col == '나이' :
            print('\n 숫자만 입력해주세요. ')
            input_age1 = int(input('몇 살 이상을 검색하겠습니까? '))
            input_age2 = int(input('몇 살 이하를 검색하겠습니까?'))
            # 오늘날짜만 연도에서 추출
            d =datetime.date.today() # 오늘날짜
            year1 = d.year-input_age2 +1
            year2 = d.year-input_age1 +1
            sql = "SELECT * FROM student WHERE birth BETWEEN {} AND {}".format(year1, year2)
            select(sql)
        elif col == '소속' :
            col2 = input('\n 검색하실 수강 그룹을 입력하세요(A/B/C)')
            sql = "SELECT * FROM student WHERE team = '{}'".format(col2)
            select(sql)
        elif col == '전화번호' :
            tel = input('\n 검색하실 전화번호를 입력하세요(숫자 11자리) : ')
            sql = "SELECT * FROM student WHERE phone = '{}' ".format(tel)
            select(sql)
        elif col =='거주지' :
            adr =input('\n 검색하실 거주지를 입력하세요. : ')
            sql = "SELECT * FROM student WHERE address = '{}'".format(adr)
            select(sql)
        else :
            print('잘못된 검색조건입니다. 처음 메뉴부터 다시 선택 ')

    elif cmd == 'i' :
        name = input('수강생 이름 : ')
        birth = input('출생연도(4자) : ')
        team = input('소속그룹(A/B/C) : ')
        phone = input('전화번호(숫자 11자리) : ')
        address = input('거주지 : ')
        sql = "INSERT INTO student VALUES(%s,%s,%s,%s,%s)" # int라고 설정되어도 그것은 ex
        values = name, birth, team, phone, address
        dml_exec(sql, values)
        print('해당 데이터 저장 완료')

    elif cmd == 'd' :
        print("수강생 삭제는 전화번호를 통해서만 가능합니다.")
        phone = input('목록에서 삭제할 수강생의 전화번호(숫자11자리) : ')
        sql = "DELETE FROM student WHERE  phone = %s"
        dml_exec(sql, phone)
        print('해당 데이터의 삭제가 완료되었습니다.')

    elif cmd == 'r' :
        print('수강생 정보 수정은 전화번호를 통해서만 가능합니다.')
        phone = input('전화번호 숫자 11자리 입력 : ')
        # 사용자에게 해당 수강생 정보 출력
        sql = "SELECT * FROM student WHERE phone = '{}'"
        select(sql)

        col = input('\n 어떤 정보를 변경할껀지 입력(이름/생년월일/소속/전화번호/거주지)')
        if col == '이름' :
            name = input('\n 해당 수강생의 수정할 이름을 입력 : ')
            sql = "UPDATE student SET name = %s WHERE phone = %s"
            values = name, phone
            dml_exec(sql,values)
            print('\n 정보 변경이 완료되었습니다. ')
        elif col == '생년월일' :
            birth = input('\n 해당 수강생의 수정할 생년월일을 입력 : ')
            sql = "UPDATE student SET birth= %s WHERE phone = %s"
            values = birth, phone
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다. ')
        elif col == '소속' :
            col2 = input('\n 해당 수강생의 수정할 소속을 입력 : ')
            sql = "UPDATE student SET team = %s WHERE phone = %s"
            values = col2, phone
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다. ')
        elif col == '전화번호' :
            tel = input('\n 해당 수강생의 수정할 전화번호를 입력 : ')
            sql = "UPDATE student SET phone = %s WHERE phone = %s"
            values = tel, phone
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다. ')
        elif col == '거주지':
            adr = input('\n 해당 수강생의 수정할 주소를 입력 : ')
            sql = "UPDATE student SET address = %s WHERE phone = %s"
            values = adr, phone
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다. ')
        else :
            print('잘못된 정보입니다. 다시 입력하시오')



## 본 프로그램은 while 문을 이용해서 무한루프를 돌리면서 사용자의 종료 명령 전까지 계속 명령어가 입력되도록 설계계# 1. 데이터 조회
#   1.1 모든 데이터조회(ALL) - 사용자 입력 없음
#   1.2 조건에 맞는 데이터만 조회(FIND) - 사용자 입력 있음
#       1.2.1 이름
#       1.2.2 나이검색
#       1.2.3 소속
#       1.2.4 전화번호
#       1.2.5 거주지
# 2. 데이터 입력
# 3. 데이터 삭제
# 4. 데이터 변경
#   4.1 이름변경
#   4.2 생년월일변경
#   4.3 소속
#   4.4 전화번호
#   4.5 거주지
# 5. 종료

