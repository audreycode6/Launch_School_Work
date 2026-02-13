import psycopg2
from psycopg2 import extras

connection = psycopg2.connect(dbname='films')

try:
    with connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute(
                """SELECT genre, count(id) FROM films
                    WHERE duration < 110
                    GROUP BY genre;"""
                    )
            genre_dict = cursor.fetchall() # gets remaining 

finally:
    connection.close()

print(f'Connection closed: {connection.closed}')


print(genre_dict)

for genre, films in genre_dict:
    print(genre, films)

for row in genre_dict:
    print(f'Genre: {row['genre']}, Films: {row['count']}')