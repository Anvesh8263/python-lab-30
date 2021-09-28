"""
create a csv file by entering user-id and password, read and search the password for given user-id 
"""

import pandas as pd
data = []
flag = 'Y'
while flag != 'N':
    user_id = input("Enter the user-id: ")
    password = input("Enter the password: ")
    data.append([user_id, password])
    flag = input("Do you want to enter another entry Y/N: ").strip()



df = pd.DataFrame(data, columns=["user-id", "password"])
print(df)
df.to_csv('e:\\Python39\\dsa-python\\dsa-python\\dsa-python\\python practical\\password.csv', index=False)


# read and search password by user-id 
import pandas as pd
user_id = input("Enter the user-id for password: ")

df = pd.read_csv("e:\\Python39\\dsa-python\\dsa-python\\dsa-python\\python practical\\password.csv")
# print(df)

for i in range(len(df['user-id'])):
    if df.iloc[i]['user-id'] == user_id:
        password = df.iloc[i]['password']

print(f"The password at user-id: {user_id} is {password}")
