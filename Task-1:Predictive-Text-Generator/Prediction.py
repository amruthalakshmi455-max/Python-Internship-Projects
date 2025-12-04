from collections import defaultdict

model=defaultdict(list)

text=open("data.txt").read().lower().split()
# print(text)


for w1,w2 in zip(text[:-1],text[1:]):
   model[w1].append(w2)

def predict(word):
   if not word in model:
       return ["no prediction"]
   return list(set(model[word]))[:5]

word = " "
while word != "q":
   word =input("enter a word (or q to quit) : ").lower()
   if word =="q":
       break
   print(f"Suggession : {predict(word)}")