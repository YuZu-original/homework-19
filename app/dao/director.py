from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session
    
    def get_one(self, director_id):
        return self.session.query(Director).get(director_id)
    
    def get_all(self):
        return self.session.query(Director).all()
    
    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director
    
    def update(self, data):
        director = self.get_one(data.get("id"))
        
        director.name = data.get("name")

        self.session.add(director)
        self.session.commit()
    
    def delete(self, director_id):
        director = self.get_one(director_id)
        
        self.session.delete(director)
        self.session.commit()