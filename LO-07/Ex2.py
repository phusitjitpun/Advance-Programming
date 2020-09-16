engine = create_engine('sqlite:///:memory:', echo=True)
connection = engine.connect()
result = connection.execute([YOUR_QUERY])
for row in result:
    ...
connection.close()