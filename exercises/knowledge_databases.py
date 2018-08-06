from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic_name,article_topic,article_title,rating):
	knowledge_object=Knowledge(
		topic_name=topic_name,
		article_topic=article_topic,
		article_title=article_title,
		rating=rating)
	session.add(knowledge_object)
	session.commit()

def query_all_articles():
	knowledge=session.query(Knowledge).all()
	return knowledge

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
add_article("jazz","Louis Armstrong","The Louis Armstrong Foundation", 6)
print(query_all_articles())

