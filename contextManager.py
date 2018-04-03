print('hello there')
with open('sample.txt','w') as f:
    f.write("Sreeeram is writing in the file")
    print(f.mode)

with open('sample.txt','r') as f1:
    print(f1.read())


print('I am done')
