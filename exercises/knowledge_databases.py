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

def query_article_by_topic(name):
	knowledge=session.query(Knowledge).filter_by(topic_name=name).all()
	return knowledge
def query_article_by_rating(threshold):
	knowledge=session.query(Knowledge).filter(Knowledge.rating< threshold).all()
	return knowledge
def query_article_by_primary_key(id):
	knowledge=session.query(Knowledge).filter_by(article_id=id).first()
	return knowledge
def delete_article_by_topic(name):
	session.query(Knowledge).filter_by(article_topic=name).delete()
	session.commit()
def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
def edit_article_rating(updated_rating, topic_name):
	knowledge=session.query(Knowledge).filter_by(topic_name=topic_name).first()
	knowledge.rating=updated_rating
	session.commit()
def delete_article_by_rating(threshold):
	session.query(Knowledge).filter(Knowledge.rating<threshold).delete()
	session.commit()
def query_top_five():
	b=0
	knowledge=session.query(Knowledge).all()

	for i in knowledge:
		for a in range(10,1,-1):
			while b<5:
				if i.rating==a:
					b+=1
					return knowledge


#add_article("jazz","Louis Armstrong","The Louis Armstrong Foundation", 6)
#edit_article_rating(9,"jazz")
#print(query_all_articles())
print(query_top_five())