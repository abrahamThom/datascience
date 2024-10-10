print("SJC23MCA-2045 : PRINCE THOMAS")
print("Batch : MCA 2023-25")
def gen_ngrams(text, wordsToCombine):
 words = text.split()
 output = []
 for i in range(len(words)-wordsToCombine+1):
  output.append(words[i:i+wordsToCombine])
 return output
x = gen_ngrams(text='Using the iris data set, implement the KNNalgorithm',wordsToCombine=3)
print(x)