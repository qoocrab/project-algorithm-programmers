-- 예상 시간복잡도: O(N)
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') FROM BOOK
WHERE CATEGORY = '인문' and PUBLISHED_DATE LIKE '2021%';
