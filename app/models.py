import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Project(db.Model):
    id:          so.Mapped[int] = so.mapped_column(primary_key=True)
    title:       so.Mapped[str] = so.mapped_column(sa.String(32), index=True, unique=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=True)
    gitRepoLink: so.Mapped[str] = so.mapped_column(sa.String(32), index=True, unique=True)
    projectType: so.Mapped[str] = so.mapped_column(sa.String(16), index=True) # solo or team project
    languages:   so.Mapped[str] = so.mapped_column(sa.String(64), index=True) # programming languages/technologies used
    imageName:   so.Mapped[str] = so.mapped_column(sa.String(32), index=True, unique=True) # image filename without extension included

    def __repr__(self):
        return '<Projects {}>'.format(self.title)
