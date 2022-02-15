doc = input()
dic = input()
doc_list = []
counter = 0

len_doc = 0
while len_doc < len(doc):
    end = len(dic)+len_doc
    if end > len(doc):
        end = len(doc)
    if doc[len_doc:end] == dic:
        counter += 1
        len_doc += len(dic)
    else:
        len_doc += 1
print(counter)