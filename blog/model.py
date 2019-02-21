from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, create_engine, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.dialects.mysql import LONGTEXT, TINYINT
from sqlalchemy.orm import sessionmaker, relationship
from .config import SQLURL, SQLDEBUG

# 实体基类
Base = declarative_base()


# 实体类
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(48), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return "<User ({}, {})>".format(self.id, self.name)

    __str__ = __repr__


class Post(Base):
    __tablename__ = "post"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(250), nullable=False)
    postdate = Column(DateTime, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    hist = Column(BigInteger, nullable=False, default=0)

    author = relationship('User')
    content = relationship('Content', uselist=False)

    def __repr__(self):
        return "<Post ({}, {})>".format(self.id, self.title)


class Content(Base):
    __tablename__ = "content"

    id = Column(BigInteger, ForeignKey('post.id'), primary_key=True)
    content = Column(LONGTEXT, nullable=False)

    def __repr__(self):
        return "<content ({}, {})>".format(self.id, self.content)


class Dig(Base):
    __tablename__ = 'dig'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(BigInteger, ForeignKey('post.id'), nullable=False)
    state = Column(TINYINT, nullable=False, default=0, comment="0 bury;1 dig")
    pubdate = Column(DateTime, nullable=False)

    user = relationship('User')

    __table_args__ = (UniqueConstraint('user_id', 'post_id'),)


# CREATE TABLE `tag` (
# 	`id` bigint(20) NOT NULL AUTO_INCREMENT,
# 	`tag` varchar(16) NOT NULL,
# 	PRIMARY KEY (`id`),
# 	UNIQUE KEY `tag` (`tag`)
# )	ENGINE=InnoDB DEFAULT CHARSET=utf8;
#
# CREATE TABLE `post_tag` (
# 	`post_id` bigint(20) NOT NULL,
# 	`tag_id` bigint(20) NOT NULL,
# 	PRIMARY KEY (`post_id`,`tag_id`),
# 	KEY `tag_id` (`tag_id`),
# 	CONSTRAINT `post_tag_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`),
# 	CONSTRAINT `post_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

class Tag(Base):
    __tablename__ = "tag"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tag = Column(String(16), nullable=False, unique=True)


class Post_tag(Base):
    __tablename__ = "post_tag"

    post_id = Column(BigInteger, ForeignKey('post.id'), nullable=False)
    tag_id = Column(BigInteger, ForeignKey('tag.id'), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('post_id', 'tag_id'),)

    post = relationship('Post')
    tag = relationship('Tag')


engine = create_engine(SQLURL, echo=SQLDEBUG)


def createalltables(tables=None):
    Base.metadata.create_all(engine, tables)


def dropalltables():
    Base.metadata.drop_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
