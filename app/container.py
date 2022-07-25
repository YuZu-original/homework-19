from app.dao.movie import MovieDAO
from app.services.movie import MovieService
from app.dao.director import DirectorDAO
from app.services.director import DirectorService
from app.dao.genre import GenreDAO
from app.services.genre import GenreService
from app.dao.user import UserDAO
from app.services.user import UserService
from app.services.auth import AuthService
from app.setup_db import db


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDAO(session=db.session)
user_service = UserService(dao=user_dao)

auth_service = AuthService(user_service=user_service)