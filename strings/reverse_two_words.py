# Given a sentence S of 2 words reverse the order of two words.
S = input().strip()
words = S.split()

reversed_sentence = words[1] + " " + words[0]
print(reversed_sentence)