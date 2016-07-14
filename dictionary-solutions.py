aditi = {
  'name': 'Aditi',
  'email': 'aditi@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print '-' * 30
# get aditi's email
print aditi['email']
# get aditi's first interest
print aditi['interests'][0]
# get email address of jasmine
print aditi['friends'][0]['email']
# get jan's second interest
print aditi['friends'][1]['interests'][1]
