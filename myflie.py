from firebase import firebase
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
url = config['DEFAULT']['firebase']
messenger = firebase.FirebaseApplication(url)

#engineer = {'id' :1001,'news':'nan go home'}
#engineer2 = {'id' :1002,'news':'Lung Tu'}
#engineer3 = {'id' :1003,'name':'Thairath','day':71118,'Time':13.55,'news':'thairath'}
#engineer3 = {'id' :1003,'name':'Thairath','day':71118,'Time':13.55,'news':'thairath'}
# engineer4 = {'name':'dailynews','day':91118,'Time':'12:45','news':'dailynews'}
# engineer5 = {'name':'Thainews','day':101118,'Time':'06.45','news':'none'}


#
# result = messenger.put('/thairath/20181108','1',engineer)
# result2 = messenger.put('/thairath/20181108','2',engineer2)
# result3 = messenger.put('/thairath/20181109','3',engineer3)
#result = messenger.get('/thairath/20181108',None)
#result4 = messenger.put('/dailynews/91118','4',engineer4)
result5 = messenger.put('/Thainews/101118','5',engineer5)
result = messenger.get('/Thainews',None)

#print("Engineer 1", result)
print("Engineer 4", result)
#print("Engineer 5", result5)

# print("Engineer 2", result2)
# print("Engineer 3", result3)
# print("Engineer 4", result4)