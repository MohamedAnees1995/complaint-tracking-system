# Regular expressions, often abbreviated as regex or regexp  
# are sequences of characters that define a search pattern.

# import re
# text = "This   is   a   sentence   with   multiple   spaces."
# cleaned_text = re.sub(r'\s+', " ", text)
# print("Cleaned text :",cleaned_text)

# import re
# paragraph = '''AI is revolutionizing many industries.
# AI has the potential to change the world.'''

# updated_paragraph = re.sub(r'\bAI\b', "Artifical Intelligence", paragraph)
# print(updated_paragraph)

# import re

# text = '''The cat and the dog played with the ball. 
# Then the cat chased the dog.'''

# word_to_count = 'dog'

# occurrences = len(re.findall(r'\b' + re.escape(word_to_count) + r'\b',text,re.IGNORECASE))

# print("Occurrences of '{}' in the text : {}".format(word_to_count,occurrences))

import re
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s])[A-Za-z\d\W]{8,}$'
    if re.match(pattern,password):
        return True
    else:
        return False
    
password = "P@55w0rd"
if validate_password(password):
    print("Valid password.")
else:
    print('Invalid password.')
        
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\w\s])[A-Za-z\d\W]{8,}$'
    
    