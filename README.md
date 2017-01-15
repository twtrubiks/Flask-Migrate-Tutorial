# Flask-Migrate-Tutorial
透過 Flask-Migrate-Tutorial  管理資料庫 (database) 📝  

* [Youtube Demo]()   

透過 [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)  管理資料庫 (database)


## 特色
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 管理資料庫 (database)。


## 安裝套件 
確定電腦有安裝 [Python](https://www.python.org/) 之後

請在  cmd (命令提示字元) 輸入以下指令
``` 
pip install Flask-Migrate
```

clone 我的簡單範例

``` 
git clone https://github.com/twtrubiks/Flask-Migrate-Tutorial.git
```

## 使用方法

clone 完之後，請切換到 <b>Entity</b> 資料夾底下

Entity.py

``` 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class PictureDate(db.Model):
    __tablename__ = 'PictureDate'

    Id = db.Column(db.Integer, primary_key=True)
    Uuid = db.Column(db.String(64), unique=True)
    Title = db.Column(db.String(64))
    Description = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()

```

步驟一 : 先初始化
``` 
python Entity.py db init
```
![alt tag](http://i.imgur.com/WK2vhKg.jpg)

步驟二 : 先初始化
``` 
python Entity.py db migrate
```
![alt tag](http://i.imgur.com/iCTWKlb.jpg)

步驟三 : 先初始化
``` 
python Entity.py db upgrade
```
![alt tag](http://i.imgur.com/4Wh369t.jpg)

你會發現目標資料夾裡多了 <b>app.db</b>

![alt tag](http://i.imgur.com/mpzTLgU.jpg)

可以使用 [SQLiteDatabaseBrowser](http://sqlitebrowser.org/)  打開 DB

![alt tag](http://i.imgur.com/1qL2vwP.jpg)

![alt tag](http://i.imgur.com/VtkNV3u.jpg)

其他說明 :

這裡是使用 SQLITE 當作範例，如果你要換其他的資料庫，請修改這串字串
``` 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
```

假如今天我們要使用 PostgreSQL ， 我們就要將這串字串修改為
``` 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PASSWORD@localhost/test'
```

假如今天我們要使用 MySQL ， 我們就要將這串字串修改為
``` 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:PASSWORD@XXX.XXX.XX.XX:3306/DB'
```
需要安裝套件 [mysql-connector-python](https://github.com/mysql/mysql-connector-python) 

假如今天我們要使用 MSSQL ， 我們就要將這串字串修改為
``` 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://user:PASSWORD@XXX.XXX.XX.XX/DB?driver=ODBC+Driver+11+for+SQL+Server'
```
需要安裝套件 [pyodbc](https://mkleehammer.github.io/pyodbc/) 

## 操作 db

增加一筆資料 ( app.py )

``` 
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

```

執行完上述指令，如果正確無誤，db 會多出一筆資料。

![alt tag](http://i.imgur.com/ywgs8zs.jpg)


更多操作請參考 [SQLAlchemy](https://zh.wikipedia.org/wiki/SQLAlchemy) 



## 執行環境
* Python 3.4.3

## Reference 
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) 


## License
MIT license
