print ("I am explaining DRY")
message = '''A principle of software development aimed at reducing repetition of
of information of all kinds'''
print(message)

def navMenu():
        print ("<a href ='#'>Home</a>")
        print ("<a href ='#'>About</a>")
        print ("<a href ='#'>Contact</a>")

def header():
    print ('<div class="header">')
    navMenu()
    print ("</div>")

def footer():
    print ("<div class=\"footer\">")
    navMenu()
    print ("</div>")

def homePage():
    header()
    footer()

def aboutPage():
        header()

homePage()
