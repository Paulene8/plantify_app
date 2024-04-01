import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pa$$w0rd",
  database="blogpostdb" # database name on sql
)


def main():
    print(mydb)

    cursor = mydb.cursor()

    sql = "INSERT INTO blogpost (post_ID, username, title, post) VALUES (%s, %s, %s, %s)"   # blogpost = table name in db. sql query to insert columns and placeholder values (%)
    val = ("Rana", "I love flowers", "I love flowers buy me more")  #SUGGESTION: Add date. How to auto add present date?
    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",
        database="blogpostdb"
    )

    return mydb


def add_blogpost(post_ID, username, title, post):
    conn = get_db_connection() #get the method above
    cursor = conn.cursor()

    sql = "INSERT INTO blogpost (post_ID, username, title, post) VALUES (%s, %s, %s, %s)"
    val = (post_ID, username, title, post)
    cursor.execute(sql, val)

    conn.commit()   #predefined method


def get_blogpost():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "Select post_ID, username, title, post from blogpost"
    cursor.execute(sql)

    result_set = cursor.fetchall()  # pre-def method
    blog_list = []
    for blogpost in result_set:
        blog_list.append({'post_ID': blogpost[0], 'username': blogpost[1], 'title': blogpost[2], 'post': blogpost[3]})
    return blog_list


if __name__ == "__main__":
    main()
