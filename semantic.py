# Compulsory Task 1 - Semantic Similarity

import spacy

# Pt 1: cat, monkey, banana

print("Test 1:\n")

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat cream monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Interesting observations:

"""
When looking at the semantic similarity scores generated by the words cat, monkey, and banana (plus
'cream' which I have chosen as an additional word), a few interesting things can be observed.

Understandably, cat and monkey share the highest similarity due to them both being animals within
the mammal classification. The score isn't overly high (0.59), which does reflect the otherwise
loose relationship between the two animals. If you ran the test with 'monkey' + another primate,
you'd expect to see higher similarity scores.

It's interesting to note that monkey and banana share a relatively high score, despite one being a
fruit and the other an animal. Taken out of context, the two things share no similarity but there
is a widespread belief that monkeys regularly eat bananas (reflected in various cultural depictions),
which explains the relatively high score of 0.40.

There is no such widespread belief in a connection between cats and bananas, and this is reflected
in the low similarity score of 0.22 between these two words. I added the word 'cream' to test whether
the common depictions of cats drinking milk/cream across different forms of media would result in a
similar score to the 'monkey' + 'banana' example. However, 'cat' + 'cream' scored much lower (0.15), perhaps
due to the cultural depiction not being as widely known.

Cream scored relatively highly when paired with banana (possibly due to a number of dishes containing
the two ingredients) at 0.48, but resulted in the lowest score of all when paired with 'monkey' (0.12).
This is likely due to monkeys not being associated with cream in terms of their habits, or in any
common depictions.

"""

# Pt 2: testing with alternative language model

print("\nTest 2\n")

nlp2 = spacy.load('en_core_web_sm')

word1 = nlp2("cat")
word2 = nlp2("monkey")
word3 = nlp2("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp2('cat cream monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Interesting observations:

"""
Upon running the same test with an alternative language model (sm instead of md), it's immediately
apparent that the scores have changed.

The most surprising change is the huge increase in similarity score between 'cream' + 'monkey'. In
the previous test, this had a low score (0.12), but with the simple language model it scores a huge
0.76. The first test seems to be a much more understandable result, due to these words and concepts
not sharing much in common.

Interestingly, 'cream' + 'monkey' scores more highly than 'banana' + 'monkey', the latter of which are
by far much more commonly associated terms.

Of equal interest is the increase in score between 'cream' + 'cat' (an increase from 0.15 to 0.57). This
at least makes sense on a surface level due to the associations between the two, but I feel that the
result can't be fully trusted due to the 'monkey' + 'cream' anomaly.

It's interesting to note that 'monkey' + 'cat' scored very similarly across the two tests, likely for
the reasons outlined in test 1 (i.e. they are both animals falling under the category of mammal, but 
otherwise don't share much in common).

"""

# Additional tests

print("\nAdditional tests:\n")

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)