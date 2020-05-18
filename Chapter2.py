#name = "tony elder"
#print (name.title())

# print ("Languages:\nPython\nC\nJavaScript")

# ~ # 2.3
# ~ name = "Eric"
# ~ message = "Hello " + name + ", would you like to learn some Python this morning?"
# ~ print (message)

# 2.4
# ~ name = "Tony Elder"
# ~ name_lowercase = name.lower()
# ~ name_uppercase = name.upper()
# ~ name_titlecase = name.title()

# ~ message = "Our contestant today is " + name + ". In lowercase, that looks like " + name_lowercase + ", in uppercase like " + name_uppercase + ", and in titlecase, like " + name_titlecase + "."
# ~ print (message)

# 2.5
# quote = 'Walt Disney once said - "The way to get started is to quit talking and begin doing."' 
# print (quote)

# 2.6
# person = "Walt Disney"
# quote = '"The way to get started is to quit talking and begin doing."'
# output = person + " once said - " + quote
# print (output)

# 2.7
name = "\n\tTony Elder\t"
leftstrip = name.lstrip()
rightstrip = name.rstrip()
allstrip = name.strip()

message1 = "The original is \n" + name + ".\n"
message2 = "With left hand whitespace stripped out it is \n" + leftstrip + ".\n"
message3 = "With right hand whitespace stripped out it is \n" + rightstrip + ".\n"
message4 = "With all whitespace stripped out it is \n" + allstrip
wholemessage = message1 + message2 + message3 + message4  
print (wholemessage)
