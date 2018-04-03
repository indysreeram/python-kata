def html_tag(tag):
    def wrap(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap

h1_tag =html_tag('h1')
h1_tag('Welcome to Cloud !!')
h1_tag('Newark DE 19702')
h2_tag =html_tag('h2')
h2_tag('aws is awesome!!')
