SELECT * FROM emp;

SELECT ENAME, HIREDATE FROM emp;

SELECT EMPNO, ENAME FROM emp;

SELECT JOB FROM emp
GROUP BY JOB;

SELECT COUNT(*) AS '총 사원수' FROM emp;

SELECT ENAME FROM emp
WHERE DEPTNO = 10;

SELECT ENAME, SAL FROM emp
WHERE SAL >= 2500;

SELECT * FROM emp
WHERE ENAME = 'KING';

SELECT EMPNO, ENAME FROM emp
WHERE ENAME LIKE 'S%';

SELECT EMPNO, ENAME FROM emp
WHERE ENAME LIKE '%T%';

SELECT EMPNO, ENAME, SAL, COMM FROM emp
WHERE COMM IN (300,500,1400);

SELECT EMPNO, ENAME, SAL FROM emp
WHERE 1200<SAL<3500;

SELECT EMPNO, ENAME, JOB, DEPTNO FROM emp
WHERE JOB = 'MANAGER' AND DEPTNO = 30;

SELECT EMPNO, ENAME, DEPTNO FROM emp
WHERE NOT DEPTNO = 30;

SELECT EMPNO, ENAME, COMM FROM emp
WHERE NOT COMM IN (300,500,1400);
# 질문


-- 16. 이름에 S가 포함되지 않는 사원의 사번,이름을 조회하시오.

SELECT EMPNO, ENAME FROM emp
WHERE NOT ENAME LIKE '%S%';

-- 17. 급여가 1200보다 미만이거나 3700 초과하는 사원의 사번,이름,월급여를 조회하시오.

SELECT EMPNO, ENAME, SAL FROM emp
WHERE 1200>SAL OR  3700<SAL ;

-- 18. 직속상사가 NULL 인 사원의 이름과 직급을 조회하시오.

SELECT EMPNO, JOB FROM emp
WHERE MGR IS NULL;

-- 19. 부서별 평균월급여를 구하시오

SELECT DEPTNO, AVG(SAL) AS '평균월급여' #ROUND(AVG(SAL),2)
FROM emp
GROUP BY DEPTNO ;

-- 20. 부서별 전체 사원수와 커미션을 받는 사원들의 수를 구하시오.

SELECT DEPTNO, COUNT(*), COUNT(COMM) FROM emp
GROUP BY DEPTNO;

-- 21. 부서별 최대 급여와 최소 급여를 구하시오.

SELECT DEPTNO, MAX(SAL) AS '최대 급여', MIN(SAL) AS '최소 급여'
FROM emp
GROUP BY DEPTNO;
 
-- 22. 부서별로 급여 평균 (단, 부서별 급여 평균이 2000 이상만)을 구하시오.

SELECT DEPTNO, AVG(SAL) AS '급여 평균'
FROM emp
GROUP BY DEPTNO HAVING AVG(SAL) >= 2000;

-- 23. 월급여가 1000 이상인 사원만을 대상으로 부서별로 월급여 평균을 구하라. 단, 평균값이 2000 이상인 레코드만 구하라.

SELECT DEPTNO, AVG(SAL) AS '월 급여 평균'  
FROM emp
GROUP BY DEPTNO;


-- 24. 급여가 높은 순으로 조회하되 급여가 같을 경우 이름의 철자가 빠른 사원순으로 사번,이름,월급여를 조회하시오.

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




















