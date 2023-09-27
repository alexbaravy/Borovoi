import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name

    def execute_sql_query(self, task, query):
        try:
            with sqlite3.connect(self.database_name) as con:
                cur = con.cursor()
                cur.execute(query)
                results = cur.fetchall()
                print(task)
                for line in results:
                    print(line)
        except sqlite3.Error as e:
            print("Ошибка при выполнении SQL запроса:", e)


database_manager = DatabaseManager('Actors New')

TASK_3 = '\n3.	Напишите SQL-запрос, который вычисляет средний возраст актеров (используйте таблицу "actors") по полу (столбец "sex") и выводит результат в виде двух столбцов: "sex" и "average_age"\n'
QUERY_3 = "SELECT sex, ROUND(AVG(age),2)  from actors a GROUP BY sex"

TASK_4 = '\n4.	Напишите SQL-запрос, который находит режиссера (имя и фамилия) с максимальным бюджетом фильма.\n'
# QUERY_4 = "SELECT name, surname FROM directors d JOIN movies m USING (director_id) ORDER BY budget DESC LIMIT 1"
QUERY_4 = "SELECT name, surname, max(budget) FROM directors d JOIN movies m USING (director_id)"

TASK_5 = '\n5.	Напишите SQL-запрос, который выводит список режиссеров (имя и фамилия) и количество фильмов, которые они сняли, причем только для режиссеров, у которых есть хотя бы один фильм в базе данных. Отсортируйте результат по убыванию количества фильмов.\n'
QUERY_5 = "SELECT name, surname, COUNT(director_id)  FROM directors d JOIN movies m USING (director_id) GROUP BY director_id ORDER BY COUNT(director_id) DESC"

TASK_6 = '\n6.	Напишите SQL-запрос, который находит актеров (имя и фамилия) и названия фильмов, в которых они снимались, но только для фильмов с бюджетом более 50 миллионов долларов.\n'
QUERY_6 = "SELECT name, surname, name_movie  FROM movies m JOIN actors_movies am USING (movie_id) JOIN actors a USING (actor_id) WHERE budget >50000000"

TASK_7 = '\n7.	Напишите SQL-запрос, который находит пять самых популярных актеров (те, кто снялся в наибольшем количестве фильмов) и выводит их имена и фамилии, а также количество фильмов, в которых они снимались.\n'
QUERY_7 = "SELECT name, surname, count(actor_id)  FROM actors a JOIN actors_movies am USING (actor_id) GROUP BY actor_id ORDER BY COUNT(actor_id) DESC limit 5"

TASK_8 = '\n8.	Напишите SQL-запрос, который выводит список режиссеров (имя и фамилия) и количество фильмов, которые они сняли, для каждого года выпуска фильмов. Посчитайте отдельно для каждого года.\n'
QUERY_8 = "SELECT name, surname, count(director_id), release FROM directors d JOIN movies m USING (director_id) GROUP BY director_id, release ORDER BY release"

tasks_queries = [
    (TASK_3, QUERY_3),
    (TASK_4, QUERY_4),
    (TASK_5, QUERY_5),
    (TASK_6, QUERY_6),
    (TASK_7, QUERY_7),
    (TASK_8, QUERY_8),
]

for task, query in tasks_queries:
    database_manager.execute_sql_query(task, query)
