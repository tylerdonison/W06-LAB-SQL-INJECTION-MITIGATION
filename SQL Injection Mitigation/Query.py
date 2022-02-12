def genQuery(username, password):
  query = "SELECT authenticate FROM passwordList WHERE name = '{}' and password = '{}';".format(username, password)
  print(query)