import dataset
'''
# connecting to a SQLite database
db = dataset.connect('sqlite:///mydatabase.db')

# connecting to a MySQL database with user and password
db = dataset.connect('mysql://user:password@localhost/mydatabase')

# connecting to a PostgreSQL database
db = dataset.connect('postgresql://scott:tiger@localhost:5432/mydatabase')
'''


db=dataset.connect('mysql://root:root@localhost/data_wrangling')

#创建一个 Python 字典，里面是我们要保存的数据
my_data_source = {
 'url':
 'http://www.tsmplug.com/football/premier-league-player-salaries-club-by-club/',
 'description': 'Premier League Club Salaries',
 'topic': 'football',
 'verified': False,
}
#创建名为 data_sources 的新表
table=db['data_sources']
#将第一个数据源插入新表
table.insert(my_data_source)

#显示我们保存在 data_sources 表中的所有数据源
sources=db['data_sources'].all()
print(sources)