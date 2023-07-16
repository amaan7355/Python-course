# WAP to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up.
mydict={
    "Pankha":"Fan" ,
    "Dabba":"Box" ,
    "Vastu":"Item"
}
print("options are: ",mydict.keys())
a=input("Enter the hindi word ")
#print("The meaning of your word is:",mydict[a])
#Below line will not throw an error if the key is not present in the dictionary.
print("The meaning of your word is:",mydict.get(a))