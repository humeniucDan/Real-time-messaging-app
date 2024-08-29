import json
import psycopg2 

FILE_PATH = 'db.config'
with open(FILE_PATH, 'r') as file:
    conn_params = json.load(file)
print(conn_params)

def loginUser(user, password):
    print("STARTED")
    try:
        # date = str(date)

        dbCon = psycopg2.connect(**conn_params)
        if dbCon == None:
            print('Could not connect to DataBase')
            return -1
        cursor = dbCon.cursor()

        query = ''' 
                select * from p1.user
                where
                name = %s and password = %s;
                '''

        cursor.execute(query, user, password)
        result = cursor.fetchall()


        print(len(result))

        return len(result)

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        if dbCon is not None:
            cursor.close()
            dbCon.close()
            print("ENDED")


def insertNewMessage(senderId, recieverId, date, content):
    print("STARTED")
    try:
        # date = str(date)

        dbCon = psycopg2.connect(**conn_params)
        if dbCon == None:
            print('Could not connect to DataBase')
            return -1
        cursor = dbCon.cursor()

        # query = ''' SELECT 
        #                 senderId, 
        #                 receiverId, 
        #                 date, 
        #                 content
        #             FROM 
        #                 p1.Messages
        #             WHERE 
        #                 senderId = %s
        #             ORDER BY 
        #                 date DESC
        #             LIMIT 1;
        #         '''

        # cursor.execute(query, senderId)
        # result = cursor.fetchall()

        # # print(result[0][3] + ' ' + content)

        # print(len(result))

        # if len(result) != 0 and result[0][3] == content: 
        #     return

        query = '''
            INSERT INTO p1.Messages (senderId, receiverId, date, content)
            VALUES (%s, %s, %s, %s);
            '''

        cursor.execute(query, [senderId, recieverId, date, content])
        dbCon.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        if dbCon is not None:
            cursor.close()
            dbCon.close()
            print("ENDED")

def pullUser(id):
    try:
        dbCon = psycopg2.connect(**conn_params)
        if dbCon == None:
            print('Could not connect to DataBase')
            return -1
        cursor = dbCon.cursor()

        query = ''' select * from p1.user as u where u.id = %s; '''

        cursor.execute(query, id)
        result = cursor.fetchall()

        print(result)
        return result if result else None

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        if dbCon is not None:
            cursor.close()
            dbCon.close()

def pullAllMsgHistory(user1Id, user2Id):
    try:
        dbCon = psycopg2.connect(**conn_params)
        if dbCon == None:
            print('Could not connect to DataBase')
            return -1
        cursor = dbCon.cursor()

        query = ''' select * from p1.messages 
                    WHERE 
                        (senderId = %s AND receiverId = %s)
                        OR 
                        (senderId = %s AND receiverId = %s)
                    ORDER BY 
                        date ASC;'''

        cursor.execute(query, [user1Id, user2Id, user2Id, user1Id])
        result = cursor.fetchall()

        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        if dbCon is not None:
            cursor.close()
            dbCon.close()
            print("Connection closed.")

def pullFriends(userId):
    try:
        dbCon = psycopg2.connect(**conn_params)
        if dbCon == None:
            print('Could not connect to DataBase')
            return -1
        cursor = dbCon.cursor()

        query = ''' SELECT 
                        u.id AS friendId, 
                        u.name AS friendName
                    FROM 
                        p1.Friends f
                    JOIN 
                        p1.User u 
                        ON u.id = CASE 
                                    WHEN f.friend1Id = %s THEN f.friend2Id
                                    ELSE f.friend1Id
                                END
                    WHERE 
                        f.friend1Id = %s OR f.friend2Id = %s;'''

        cursor.execute(query, [userId, userId, userId])
        result = cursor.fetchall()

        print(result)
        return result if result else None

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        if dbCon is not None:
            cursor.close()
            dbCon.close()