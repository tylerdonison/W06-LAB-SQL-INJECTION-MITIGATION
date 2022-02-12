#Provides constants for SQL Injection Mitigation.
#Contains lists of Usernames and Passwords for the 5 test cases.

#Valid Test cases
validUsernames =    ["whatissleep", "Thisguy234", "Byron86"]
validPasswords =    ["idontknow4", "BadatMath98", "chucky007"]

#Tautology Test Cases
tautologyUsernames =["Username", "Username", "Username"]
tautologyPasswords =["x OR 'y' = 'y", "stuff' OR NOT 'NULL", "Password' OR 'True' == 'True"]

#Union Test Cases
unionUsernames =    ["Username", "Username", "Username"]
unionPasswords =    ["nothing' UNION SELECT socialSecurity FROM directDepositList",  
                    "nothing' UNION SELECT creditCard FROM creditList",
                    "nothing' UNION SELECT username AND password FROM passwordList"]

#Additional Statement Test Cases
addStateUsernames = ["Username", "Username", "Username"]
addStatePasswords = ["nada; INSERT INTO passwordList (name, password) Values 'Hackerman', 'beammeup",
                    "zip; INSERT INTO authenticatedList (username, password) VALUES 'bad', 'guy",
                    "Thin'; UPDATE passwordList SET password = 'Hacked' Where username = 'Root';"]

#Comment Test Cases
commentUsernames =  ["Thisguy234'; - -", "whatissleep';- -", "Root'; - -"]
commentPasswords =  ["Thing whatever", "fiteme", "Nothing"]