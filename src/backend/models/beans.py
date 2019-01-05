class BeanModel(application.db.Model):
    __tablename__ = "beans"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    color = Column(String(80), nullable=False)

    profiles = relationship("Profile")

    def __init__(self, name, color, profile_id=None):
        self.name = name
        self.color = color
        
        if type(profile_id) is int:
            c = SESSION.query(Profile).get(profile_id)
            self.children.append(c)

    def repr(self):
        return "<{} | {}>".format(self.name, self.color)
