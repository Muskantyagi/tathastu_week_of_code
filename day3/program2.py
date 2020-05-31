def permutation(List,String =""):
    Set =set(List)
    stringlist=[]
    if len(Set) == 1:
        String += " ".join(List)
    return list([String])
    for x in Set:
        List1 =list(List)
        S = String + x
        List1.remove(x)
        stringlist.extend(permutation(List1,S))
    return stringlist

string = input("enter a number")
List = permutation(list(string))
print("all the permutation of a String : " + " , ".join(List))
