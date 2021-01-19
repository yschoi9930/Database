# mysql 사용하기 위한 모듈 선언
import pymysql

# # 각 함수에서 연결된 공용 DB를 같이 사용하도록 프로그래밍
# # CONNECTION 객체를 반환
# DBCONN = PyMySQL.CONNECT(host = 'localhost', port = 3306, user ='root', password = '0000',
#                         database = 'funct_test', charset = 'utf8')
#
# # 각 함수별로 예외처리 진행
# # SELECT 처리 함수
#
# def select(query) :
#     return 1
#
# # DML 처리 함수 : INSERT, UPDATE, DELETE 처리(에러 외에 반환되는 결과값이 뜨지 않음->return 구문이 필요하지 않음)
# # commit 처리 후에 에러가 발생하면 예외처리 후 rollback 처리
# # rollback : 트랜젝션으로 인한 하나의 묶음 처리가 시작되기 이전의 상태로 되돌린다 / 이전 커밋한 곳으로 복구
# # 사용자에게 쿼리와 쿼리에 사용될 값을 분리해서 받아 처리함
#
# def merge(query, values) :
#     return 1
#
# # DML을 대량 처리하는 함수 : INSERT, UPDATE, DELETE 대량 처리하는 함수
# # commit 처리 후에 에러가 발생하면 예외처리 후 rollback 처리
# # 사용자에게 쿼리와 쿼리에 사용될 값을 분리해서 받아 처리함
#
# def merge_all(query, values) :
#     return 1
#
# # DML 이외의 쿼리를 실행하는 함수 (CREATE, ALTER, DROP)
# # commit 처리 후에 에러가 발생하면 예외처리 후 rollback 처리
#
# def ddl_exec(query) :
#     return 1
#
# ### main
# # DB와 연결하는 코드는 예외처리를 반드시 하는게 좋다
#
#
# try :
#     # 1. 연습에 사용될 테이블이 미리 만들어져 있으면 삭제
#     ddl_exec('테이블을 삭제하는 쿼리 구문')
#
#     # 2. 연습에 사용할 테이블 생성
#     query = '테이블 생성하는 쿼리 구문'
#     ddl_exec(query)
#
#     # 3. 테이블에 데이터를 넣기 위한 연습
#     # 사용자에게 값을 입력받아서 해당 값을 테이블에 저장
#
#     # 사용자에게 저장할 값 입력받기
#     id_x = input('id를 입력하세요')
#     passwd = input('비밀번호를 입력하세요')
#     name_s = input('이름을 입력하세요')
#
#     # insert 구문 완성
#     query = 'insert 코드'
#     merge(query, values)
#
#     # 4. 테이블에 여러개의 정보 입력하기
#     query = '저장 쿼리 완성'
#     values = '저장할 값'
#
#     merge_all(query, values)
#
#     # 5. 입력된 데이터 확인하기
#     query = '검색쿼리'
#
#     res = select(query)
#
#     # 6. 입력된 데이터를 수정
#     # 수정 쿼리
#     query = '수정쿼리'
#     values = '수정할 데이터'
#     merge(query, values)
#
#     print('-------수정확인--------')
#     res = select(query)
#
#     # 7. 사용한 테이블을 삭제
#     ddl_exec('테이블을 삭제하는 쿼리 구문')
#
# except Exception as e :
#     print(e)
#
# finally :
#     # connection 객체 사용 종료 후 리소스 닫기
#     dbconn.close()





### 예제
# DB와 연결하는 코드는 예외처리를 반드시 하는게 좋다

# 각 함수에서 연결된 공용 DB를 같이 사용하도록 프로그래밍
# CONNECTION 객체를 반환
DBCONN = pymysql.connect(host = 'localhost', port = 3306, user ='root', password = '0000',
                        database = 'funct_test', charset = 'utf8')

# 각 함수별로 예외처리 진행
# SELECT 처리 함수 - commit
# select * from member를 처리해서 dbms로부터 넘어온 결과를 반환
def select(query) :
    # 전역에 선언되어 있는 connection 객체 참조
    global DBCONN
    # 커서 취득
    cursor = DBCONN.cursor()
    #쿼리 실행
    cursor.execute(query)
    # 쿼리 실행 결과 리턴 - cursor가 결과의 위치를 갖고 있음
    # fetch 함수 이용해서 일부분을 리턴하거나 리스트 형태로 리턴도 가능
    # 단 용량이 많으면 느려지게 됨(단점)
    return cursor # 커서가 리턴이 된다는 점 기억

# DML 처리 함수 : INSERT, UPDATE, DELETE 처리(에러 외에 반환되는 결과값이 뜨지 않음->return 구문이 필요하지 않음)
# commit 처리 후에 에러가 발생하면 예외처리 후 rollback 처리
# rollback : 트랜젝션으로 인한 하나의 묶음 처리가 시작되기 이전의 상태로 되돌린다 / 이전 커밋한 곳으로 복구
# 사용자에게 쿼리와 쿼리에 사용될 값을 분리해서 받아 처리함

def merge(query, values) :
    # 전역에 선언되어 있는 connection 가져오기
    global DBCONN
    try :
        # 커서 취득
        cursor = DBCONN.cursor()
        # 쿼리 실행
        # execute 함수는 내부에서 문자열 포맷팅으로 설정된 값에 실제 값을 매칭시켜줌
        cursor.execute(query,values)
        DBCONN.commit()
    except Exception as e :
        DBCONN.rollback()



# DML을 대량 처리하는 함수 : INSERT, UPDATE, DELETE 대량 처리하는 함수
# commit 처리 후에 에러가 발생하면 예외처리 후 rollback 처리
# 사용자에게 쿼리와 쿼리에 사용될 값을 분리해서 받아 처리함

def merge_all(query, values) :
    global DBCONN
    try :
        # 위 함수와 동일 프로세스
        cursor = DBCONN.cursor()
        cursor.executemany(query,values)
        DBCONN.commit()
    except Exception as e :
        DBCONN.rollback()

# DML 이외의 쿼리를 실행하는 함수 (CREATE, ALTER, DROP)
# commit 처리 후에 에러가 발생하면 예외처리 후 rollback 처리

def ddl_exec(query) :
    # 전역에 선언되어 있는 connection 가져오기
    global DBCONN
    try:
        cursor = DBCONN.cursor()
        cursor.execute(query) # values를 굳이 지정받을 필요가 없음
        DBCONN.commit()
    except Exception as e:
        DBCONN.rollback()
    return 1





# 어떤 테이블을 생성할 건지(테이블 생성코드)
# 테이블 이름 member
# 필드 :
# id varchar(20) not null primarykey
# passwd varchar(20) not null
# name varchar(20) not null


try:
    # 1. 연습에 사용될 테이블이 미리 만들어져 있으면 삭제
    # ddl_exec('drop table member')

    # # 2. 연습에 사용할 테이블 생성
    # query = '''create table member (
    #             id varchar(20) not null primarykey,
    #             passwd varchar(20) not null,
    #             name varchar(20) not null)
    #         '''
    # ddl_exec(query)
    #
    # # 3. 테이블에 데이터를 넣기 위한 연습
    # # 사용자에게 값을 입력받아서 해당 값을 테이블에 저장
    #
    # # 사용자에게 저장할 값 입력받기
    # id_x = input('id를 입력하세요 : ')
    # passd = input('비밀번호를 입력하세요 : ')
    # name_s = input('이름을 입력하세요 : ')
    #
    # # insert 구문 완성
    # query = "insert into member values (%s, %s,%s)"
    # values = (id_x, passd, name_s)
    # merge(query, values)
    #
    # # 4. 테이블에 여러개의 정보 입력하기
    # query = "insert into member values (%s, %s,%s)"
    # values = [('apple', 'apple', '홍길동'),
    #           ('peach', 'peach', '김철수')]
    #
    # merge_all(query, values)

    # 5. 입력된 데이터 확인하기
    # query = 'select * from member'
    #
    # res = select(query)
    # print(res)

    # # 6. 입력된 데이터를 수정
    # # 수정 쿼리
    # query = 'update member set passwd = %s where id = %s'
    # id = input('수정할 id를 입력하세요. : ')
    # passd = input('변경할 비밀번호를 입력하세요. : ')
    # values = passd, id
    # merge(query, values)
    #
    # print('-------수정확인--------')
    # query = 'select *
    # # 7. 사용한 테이블을 삭제
    # ddl_exec('drop table member')

except Exception as e:
    print(e)

finally:
    # connection 객체 사용 종료 후 리소스 닫기
    DBCONN.close()















