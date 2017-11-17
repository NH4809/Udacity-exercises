import urllib

def read_text():
    quotes = open("C:\Python27\movie_quotes.txt")
    contents_of_file = quotes.read()
    print("***Original file:")
    print(contents_of_file)
    quotes.close()
    print("")
    print("***File with profanity filtering:")
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text="+text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("This document has no curse words")
    else:
        print("Could not scan the document properly")
        print(output)
    connection.close()
    
read_text()

