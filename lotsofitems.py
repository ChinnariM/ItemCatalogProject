from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Items , User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Add User
user1 = User(name='Mayuree Chinnari',email='ch.mayureesubudhi@gmail.com' )
session.add(user1)
session.commit()

# Add Catagories
category1 = Category(name="Soccer")
session.add(category1)
session.commit()

category2 = Category(name="BasketBall")
session.add(category2)
session.commit()

category3 = Category(name="BaseBall")
session.add(category3)
session.commit()

category4 = Category(name="Frisbee")
session.add(category4)
session.commit()

category5 = Category(name="Snow Boarding")
session.add(category5)
session.commit()

category6 = Category(name="Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(name="FoosBall")
session.add(category7)
session.commit()

category8 = Category(name="Skating")
session.add(category8)
session.commit()

category9 = Category(name="Hockey")
session.add(category9)
session.commit()
print ("added Catagories !") 

Item1 = Items(title="Soccer Shoes", description="soccer shoes are an item of footwear worn when playing Soccer. Those designed for grass pitches have studs on the outsole to aid grip",
                      category=category1, user=user1)

session.add(Item1)
session.commit()
Item2 = Items(title="Soccer Balls", description="A soccer ball, is the ball used in the sport of association Scccer. ",
                      category=category1, user=user1)

session.add(Item2)
session.commit()

Item3 = Items(title="Soccer Apparel", description="A cloth weared during the soccer game. ",
                      category=category1, user=user1)

session.add(Item3)
session.commit()

Item4 = Items(title="Shin guard", description="is a piece of equipment worn on the front of a player’s shin to protect them from injury.",
                      category=category1, user=user1)

session.add(Item4)
session.commit()


Item5 = Items(title="Basketball Balls", description="A  ball, is the ball used in the sport of association for Basketball.",
                      category=category2, user=user1)

session.add(Item5)
session.commit()

Item6 = Items(title="BasketBall hoop", description="A backboard is a piece of basketball equipment. It is a raised vertical board with an attached basket consisting of a net suspended from a hoop.",
                      category=category2, user=user1)

session.add(Item6)
session.commit()


Item7 = Items(title="Baseball Bat", description="A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher.",
                      category=category3, user=user1)

session.add(Item7)
session.commit()
Item8 = Items(title="Baseball Balls", description="A Baseball ball, is the ball used in the sport of association Baseball. ",
                      category=category3, user=user1)

session.add(Item8)
session.commit()

Item9 = Items(title="BaseBall Halmet", description="A batting helmet is worn by batters in the game of baseball , It is meant to protect the batter's head from errant pitches thrown by the pitcher.",
                      category=category3, user=user1)

session.add(Item9)
session.commit()

Item10 = Items(title="Flying Disc", description="A frisbee is a gliding toy or sporting item that is generally plastic round disc It is used recreationally and competitively for throwing and catching, as in flying disc games.",
                      category=category4, user=user1)

session.add(Item10)
session.commit()


Item11 = Items(title="Snowboard Goggles", description="these are type of glasses t prevent people from snow blindness.",
                      category=category5, user=user1)

session.add(Item11)
session.commit()

Item12 = Items(title="Snowboard", description="A snowboard is a flat board with bindings that hold your feet in place while gliding down the mountain.",
                      category=category5, user=user1)

session.add(Item12)
session.commit()






print ("added menu items!")