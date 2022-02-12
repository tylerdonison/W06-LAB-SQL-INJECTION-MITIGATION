def genQuery(username, password):
  #generates a SQL statement if a given username and password are not invalid
  if username == "Invalid" or password == "Invalid":
    query ="You username/password is invalid."
  else: 
    query = "SELECT authenticate FROM passwordList WHERE name = '{}' and password = '{}';".format(username, password)
  print(f"-----Query: {query}")
