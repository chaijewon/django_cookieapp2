from django.db import models
import cx_Oracle
# Create your models here.

def getConnection():
   try:
        conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
   except Exception as e:
        print(e)
   return conn

def movie_list(page):
    conn=getConnection()
    cursor=conn.cursor()
    rowSize = 12
    start = (rowSize * page) - (rowSize - 1)
    end = (rowSize * page)
    sql = f"""
                SELECT mno,title,poster,num 
                FROM (SELECT mno,title,poster,rownum as num
                FROM (SELECT mno,title,poster
                FROM daum_movie ORDER BY mno ASC))
                WHERE num BETWEEN {start} AND {end}
              """
    cursor.execute(sql)
    movie_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return movie_data

def movie_totalpage():
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT CEIL(COUNT(*)/12.0) FROM daum_movie
          """
    cursor.execute(sql)
    total=cursor.fetchone()  # (100,)  => fetchall()  [(),(),()....], fetchone() => (....)
    cursor.close()
    conn.close()
    return total[0]

def movie_detail(mno):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT mno,poster,title,genre,grade,score,regdate,time,story,nation,key
            FROM daum_movie
            WHERE mno={mno}
          """
    cursor.execute(sql)
    dd=cursor.fetchone()
    detail_data=(dd[0],dd[1],dd[2],dd[3],dd[4],dd[5],dd[6],dd[7],dd[8].read(),dd[9],dd[10])
    cursor.close()
    conn.close()
    return detail_data

def movie_info(mno):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT mno,poster FROM daum_movie
            WHERE mno={mno}
          """
    cursor.execute(sql)
    movie_info=cursor.fetchone()
    cursor.close()
    conn.close()
    return movie_info
