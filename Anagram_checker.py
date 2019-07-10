word1 = "earth"
word2 = "heart"

def is_anagram():
    if sorted(word1)==sorted(word2):
        print("It's an anagram")

is_anagram()
