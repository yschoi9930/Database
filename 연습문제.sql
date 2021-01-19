CREATE DATABASE EXERCISE_TEST;

USE EXERCISE_TEST;

CREATE TABLE DEPT (
    DEPTNO DECIMAL(2),
    DNAME VARCHAR(14),
    LOC VARCHAR(13),
    CONSTRAINT PK_DEPT PRIMARY KEY (DEPTNO) 
);
CREATE TABLE EMP (
    EMPNO DECIMAL(4),
    ENAME VARCHAR(10),
    JOB VARCHAR(9),
    MGR DECIMAL(4),
    HIREDATE DATE,
    SAL DECIMAL(7,2),
    COMM DECIMAL(7,2),
    DEPTNO DECIMAL(2),
    CONSTRAINT PK_EMP PRIMARY KEY (EMPNO),
    CONSTRAINT FK_DEPTNO FOREIGN KEY (DEPTNO) REFERENCES DEPT(DEPTNO)
);
CREATE TABLE SALGRADE ( 
    GRADE TINYINT,
    LOSAL SMALLINT,
    HISAL SMALLINT 
);
INSERT INTO DEPT VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS');
INSERT INTO DEPT VALUES (30,'SALES','CHICAGO');
INSERT INTO DEPT VALUES (40,'OPERATIONS','BOSTON');
INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,STR_TO_DATE('17-12-1980','%d-%m-%Y'),800,NULL,20);
INSERT INTO EMP VALUES (7499,'ALLEN','SALESMAN',7698,STR_TO_DATE('20-2-1981','%d-%m-%Y'),1600,300,30);
INSERT INTO EMP VALUES (7521,'WARD','SALESMAN',7698,STR_TO_DATE('22-2-1981','%d-%m-%Y'),1250,500,30);
INSERT INTO EMP VALUES (7566,'JONES','MANAGER',7839,STR_TO_DATE('2-4-1981','%d-%m-%Y'),2975,NULL,20);
INSERT INTO EMP VALUES (7654,'MARTIN','SALESMAN',7698,STR_TO_DATE('28-9-1981','%d-%m-%Y'),1250,1400,30);
INSERT INTO EMP VALUES (7698,'BLAKE','MANAGER',7839,STR_TO_DATE('1-5-1981','%d-%m-%Y'),2850,NULL,30);
INSERT INTO EMP VALUES (7782,'CLARK','MANAGER',7839,STR_TO_DATE('9-6-1981','%d-%m-%Y'),2450,NULL,10);
INSERT INTO EMP VALUES (7788,'SCOTT','ANALYST',7566,STR_TO_DATE('13-7-1987','%d-%m-%Y')-85,3000,NULL,20);
INSERT INTO EMP VALUES (7839,'KING','PRESIDENT',NULL,STR_TO_DATE('17-11-1981','%d-%m-%Y'),5000,NULL,10);
INSERT INTO EMP VALUES (7844,'TURNER','SALESMAN',7698,STR_TO_DATE('8-9-1981','%d-%m-%Y'),1500,0,30);
INSERT INTO EMP VALUES (7876,'ADAMS','CLERK',7788,STR_TO_DATE('13-7-1987', '%d-%m-%Y'),1100,NULL,20);
INSERT INTO EMP VALUES (7900,'JAMES','CLERK',7698,STR_TO_DATE('3-12-1981','%d-%m-%Y'),950,NULL,30);
INSERT INTO EMP VALUES (7902,'FORD','ANALYST',7566,STR_TO_DATE('3-12-1981','%d-%m-%Y'),3000,NULL,20);
INSERT INTO EMP VALUES (7934,'MILLER','CLERK',7782,STR_TO_DATE('23-1-1982','%d-%m-%Y'),1300,NULL,10);
INSERT INTO SALGRADE VALUES (1,700,1200);
INSERT INTO SALGRADE VALUES (2,1201,1400);
INSERT INTO SALGRADE VALUES (3,1401,2000);
INSERT INTO SALGRADE VALUES (4,2001,3000);
INSERT INTO SALGRADE VALUES (5,3001,9999);
COMMIT;


-- 1. 사원 테이블의 모든 레코드를 조회하시오.

-- 2. 사원명과 입사일을 조회하시오.

-- 3.사원번호와 이름을 조회하시오.

-- 4.사원테이블에 있는 직책의 목록을 조회하시오.


-- 5. 총 사원수를 구하시오.


-- 6.부서번호가 10인 사원을 조회하시오.

-- 7.월급여가 2500이상 되는 사원을 조회하시오.

-- 8.이름이 'KING'인 사원을 조회하시오.

-- 9.사원들 중 이름이 S로 시작하는 사원의 사원번호와 이름을 조회하시오.

-- 10.사원 이름에 T가 포함된 사원의 사원번호와 이름을 조회하시오.

-- 11.커미션이 300, 500, 1400 인 사원의 사번,이름,커미션을 조회하시오.

-- 12. 월급여가 1200 에서 3500 사이의 사원의 사번,이름,월급여를 조회하시오.

-- 13. 직급이 매니저이고 부서번호가 30번인 사원의 이름,사번,직급,부서번호를 조회하시오.

-- 14.부서번호가 30인 아닌 사원의 사번,이름,부서번호를 조회하시오.

-- 15. 커미션이 300, 500, 1400 이 모두 아닌 사원의 사번,이름,커미션을 조회하시오.

-- 16. 이름에 S가 포함되지 않는 사원의 사번,이름을 조회하시오.

-- 17. 급여가 1200보다 미만이거나 3700 초과하는 사원의 사번,이름,월급여를 조회하시오.

-- 18. 직속상사가 NULL 인 사원의 이름과 직급을 조회하시오.

-- 19. 부서별 평균월급여를 구하시오

-- 20. 부서별 전체 사원수와 커미션을 받는 사원들의 수를 구하시오.

-- 21. 부서별 최대 급여와 최소 급여를 구하시오.

-- 22. 부서별로 급여 평균 (단, 부서별 급여 평균이 2000 이상만)을 구하시오.

-- 23. 월급여가 1000 이상인 사원만을 대상으로 부서별로 월급여 평균을 구하라. 단, 평균값이 2000 이상인 레코드만 구하라.

--24. 급여가 높은 순으로 조회하되 급여가 같을 경우 이름의 철자가 빠른 사원순으로 사번,이름,월급여를 조회하시오.

-- 25. 사원명과 부서명을 조회하시오.

-- 26. 이름,월급여,월급여등급을 조회하시오.

-- 27. 이름,부서명,월급여등급을 조회하시오.

-- 28.이름,직속상사이름을 조회하시오.

-- 29. 이름,부서명을 조회하시오.단, 사원테이블에 부서번호가 40에 속한 사원이 없지만 부서번호 40인 부서명도 출력되도록 하시오.

-- 30. 이름,부서번호,부서이름을 조회하시오.

-- 31. 부서번호가 30번인 사원들의 이름, 직급, 부서번호, 부서위치를 조회하시오.

-- 32. 커미션을 받는 사원의 이름, 커미션, 부서이름,부서위치를 조회하시오.

-- 33. DALLAS에서 근무하는 사원의 이름,직급,부서번호,부서명을 조회하시오.

-- 34. 이름에 A 가 들어가는 사원의 이름,부서명을 조회하시오.

-- 35. 이름, 직급, 월급여, 월급여등급을 조회하시오.

-- 36. ALLEN과 같은 부서에 근무하는 사원의 이름, 부서번호를 조회하시오.

-- 37. 사원명 'JONES'가 속한 부서명을 조회하시오.


