from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session
    
    def get_one(self, director_id):
        return self.session.query(User).get(director_id)
    
    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()
    
    def get_all(self):
        return self.session.query(User).all()
    
    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user
    
    def update(self, data):
        user = self.get_one(data.get("id"))
        
        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")

        self.session.add(user)
        self.session.commit()
    
    def delete(self, uid):
        user = self.get_one(uid)
        
        self.session.delete(user)
        self.session.commit()