import json
import md5

dict = {}

target = open('common_words.txt', 'r')
words = target.read()
basic_words = words.splitlines( )
print basic_words
for word in basic_words:


#     plaintext_password = word
#     print plaintext_password
#     # m = md5.new()
#     # m.update(plaintext_password)
#     # encrypted_password = m.hexdigest
#     # rainbow.append(encrypted_password)
#
# print rainbow


# info = open('accounts.json', 'r')
# database = json.loads(info.read())
# # user = raw_input('input username:' )
# for tuple in database:
#     print tuple['password']

# plaintext_password = 'opensesame'
# m = md5.new()
# m.update(plaintext_password)
# encrypted_password = m.hexdigest()
