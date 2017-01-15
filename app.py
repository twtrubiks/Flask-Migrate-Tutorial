from Model.dModel import *
import uuid

uuid = str(uuid.uuid4())
title = "test Title"
description = "test Description"

insert_data = PictureDate(Uuid=uuid
                          , Title=title
                          , Description=description
                          )
db.session.add(insert_data)
db.session.commit()
print("DONE")
