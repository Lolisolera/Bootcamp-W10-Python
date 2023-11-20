
# a for adding to an existing file​ and creates the file if it does not exists
# Using context manager to handling resource usage
" automatically setup and teardown resources"

"Syntax :  with openMethod('pathtofolder/parthtofile/fileName.txt', 'w') as varName:"
with open(filePath1 = open('OneDrive_1_20-11-2023/1_FileHandling/Myfile1.txt', 'a')) as filePath1:
    contents ="\nYourA\ntext\ngoes\nhere\nin\nnewlines"
    filePath1.write(contents) #write to file 
contents = "/nHello/nHow/nare/nyou?"

filePath1.write(contents)

"To Do: Task 1: Task 1: Refer to the example code above to use the context manager to:"
# append to your file (yourName.txt), your interests and a fake address

"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html