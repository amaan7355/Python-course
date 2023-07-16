#WAP to fill in a letter template given below with name and date.
letter='''Dear, <|Name|>
                You're selected!
                                 <|Date|>'''
name=input("Enter your name: ")
date=input("Enter the date: ")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)
