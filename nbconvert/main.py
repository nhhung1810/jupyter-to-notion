import os
import glob
from shutil import copyfile
from shutil import rmtree
from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload

token_v2 = '<token_v2>'

def make_dir():
    md = glob.glob("md")
    if (len(md) != 0):
        print("Exist a md dir. Please remove, or move them outside of this directory!")
        print("----------------------------------------------------------------------")
        opt = input("Do you want to remove /md dir(y/n): ")
        if(opt == 'y'):
            rmtree("md")
            os.mkdir("md")
        elif(opt == 'n'):
            print("Terminate.")
            exit(0)
    else:
        os.mkdir("md")



def main():
    filename = glob.glob("*.ipynb")
    if (len(filename) == 0):
        print("There are no Jupyter Notebook file in this folder!")
        exit(0)

    make_dir()

    for f in filename:
        newPath = "md\\" + f
        copyfile(f, newPath)

    os.chdir("md")
    os.system("cmd /c jupyter nbconvert --clear-output *.ipynb")
    os.system("cmd /c jupyter nbconvert --to markdown  *.ipynb")

    filename = glob.glob("*.md")

    # Follow the instructions at https://github.com/jamalex/notion-py#quickstart to setup Notion.py
    client = NotionClient(token_v2)
    page = client.get_block("https://www.notion.so/import-d2e84c7408d64bcc92345fea9c747985")


    for f in filename:
        with open(f, "r", encoding="utf-8") as mdFile:
            newPage = page.children.add_new(PageBlock, title=f)
            upload(mdFile, newPage) #Appends the converted contents of TestMarkdown.md to newPage
    
    os.chdir("..")
    rmtree("md")

if __name__ == "__main__":
    main()
    