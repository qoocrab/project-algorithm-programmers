-- 예상 시간복잡도: O(NlogN)
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') FROM DOCTOR
WHERE MCDP_CD in ('GS', 'CS')
ORDER BY HIRE_YMD desc, DR_NAME asc;
