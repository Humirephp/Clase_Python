import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
 
nltk.download('punkt')
 
text = "Este es un ejemplo. Aquí hay más texto para tokenizar."
 
# Tokenización en oraciones
sentences = sent_tokenize(text)
print("Oraciones:", sentences)
 
# Tokenización en palabras
words = word_tokenize(text)
print("Palabras:", words)
 