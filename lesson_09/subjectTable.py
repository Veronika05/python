from sqlalchemy import create_engine, text

class SubjectTable:
    __scripts = {
        "select" : text("SELECT * FROM subject"),
        "insert_new" : text("insert into subject(\"subject_title\") values (:new_title)"),
        "update" : text("update subject set subject_title = :new_title where subject_id = :id"),
        "delete" : text("DELETE FROM subject WHERE subject_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows
    
    def add_subject(self, title):
        connection = self.__db.connect()
        transaction = connection.begin()
        result = connection.execute(self.__scripts["insert_new"], {"new_title" :title})
        transaction.commit()
        connection.close()
        return result

    def update(self, id, new_title):
        connection = self.__db.connect()
        transaction = connection.begin()
        connection.execute(self.__scripts["update"], {"id": id, "new_title": new_title})
        
        transaction.commit()
        connection.close()

    def delete(self, id):
        connection = self.__db.connect()
        transaction = connection.begin()
        connection.execute(self.__scripts["delete"], {"id": id})

        transaction.commit()
        connection.close()


