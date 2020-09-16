engine = create_engine('sqlite:///:memory:', echo=True)
result = connection.execute([YOUE_QUERY])
for row in result:
    ...
result.close()