from sqlmodel import Session, select
from typing import List, Optional
import uuid

# Importando os models do caminho correto que você indicou
from models.db_models import User, Server, Product, Acquisition
from .base_repository import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, session: Session):
        super().__init__(User, session)

    def get_by_email(self, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()

class ServerRepository(BaseRepository[Server]):
    def __init__(self, session: Session):
        super().__init__(Server, session)

    def get_by_owner(self, owner_id: uuid.UUID) -> List[Server]:
        statement = select(Server).where(Server.id_owner == owner_id)
        return list(self.session.exec(statement).all())

class ProductRepository(BaseRepository[Product]):
    def __init__(self, session: Session):
        super().__init__(Product, session)

    def get_by_server(self, server_id: uuid.UUID) -> List[Product]:
        statement = select(Product).where(Product.id_server == server_id)
        return list(self.session.exec(statement).all())

class AcquisitionRepository(BaseRepository[Acquisition]):
    def __init__(self, session: Session):
        super().__init__(Acquisition, session)

    def get_by_user(self, user_id: uuid.UUID) -> List[Acquisition]:
        statement = select(Acquisition).where(Acquisition.id_user == user_id)
        return list(self.session.exec(statement).all())
