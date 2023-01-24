import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# i notice here that the second method looks at many more similarities and relations between the words
# the first method only draws a single and general similarity figure for each comparison

# the similarities between cat-apple and monkey-apple are interesting as it suggests that monkeys are only slightly more similar to the fruit than cats
# my guess here is because monkeys typically consume a lot of fruit since they are largely tree animals

# in examply.py, i notice that the second model - en_core_web_sm - produced less abstract similarities between the words than the initial model
# when running it on the second model, i get the UserWarning: [W007]
# it specifies that using en_core_web_sm limits the results as it cannot ship with word vectors and therefore none are loaded
# this is apparently because it is a small model - it only uses context-sensitive tensors