from blog.model import createalltables, Base

createalltables(tables=[Base.metadata.tables['tag']])