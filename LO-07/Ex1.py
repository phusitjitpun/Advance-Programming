engine = create_engine('sqlite:///:memory:', echo=True)
connection = engine.connect()
result = connection.execute([YOUE_QUERY])
for row in result:
    ...
connection