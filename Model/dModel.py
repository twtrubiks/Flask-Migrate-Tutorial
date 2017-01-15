from Entity.Entity import *


class PictureDate(db.Model):
    __tablename__ = 'PictureDate'

    def __init__(self
                 , Uuid
                 , Title
                 , Description
                 ):
        self.Uuid = Uuid
        self.Title = Title
        self.Description = Description
