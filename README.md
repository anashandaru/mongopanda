# mongopanda
Interfacing Panda dataframe to mongodb
writen by Anas Handaru


#How to use
1. place mongopanda.py on the desired directory

2. import the module
'''python
import mongopanda as mp
'''

3. connect to mongodb specify host and port
'''python
client = mp.client('localhost',21017)
'''
or leave it as default 
'''python
client = mp.client()
'''

4. inserting panda dataframe on particular topic
'''python
counter = client.insert('anytopic',testdf)
'''

5. retrieving from mongodb to dataframe from particulat topic
'''pyhton
dataFrame = client.retrieve('anytopic')
'''
