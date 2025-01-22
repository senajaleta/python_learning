from collections import Counter
text =input("enter your text: ")
vowel_list = ["A","E","I","O","U","a","e","i","o","u"]
number_of_words = 0
unique_words = []
text = text.split()
def vowel_consonant():
    vowels = 0
    consonant = 0
    for word in text:
        for char in word:
            if char.isalpha():
                if char in vowel_list:
                    vowels += 1
                else:
                    consonant += 1
    print("number of vowels: ",vowels)
    print("number of consonant: ",consonant)


def unique_frequent():
    counter = Counter(text)
    print("This words are redundant")
    for i,j in counter.most_common():
        print(i ,"---->",j)
    for unique in text:
        if unique not in unique_words:
            unique_words.append(unique)
    print("the unique words : ",unique_words)

vowel_consonant()
unique_frequent()