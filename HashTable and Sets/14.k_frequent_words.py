from collections import defaultdict

def k_frequent_words(words):
    dic=defaultdict(int)
    for word in words:
        dic[word]+=1
    print(dic)

    sorted_dic=sorted(dic.items(),key=lambda x:(x[0],x[1]))

    print(dict(sorted_dic))






words = ["the","day","is","sunny","the","the","the","sunny","is","is","a"]
k = 4
print(k_frequent_words(words))