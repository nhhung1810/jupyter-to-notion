# jupyter-to-notion
Take your Jupyter Notebook(s) and upload to your Notion account only on one step. Available on Window.

# Why I make this project
I'm tired of browsing all of my notebooks when I have to revise something. Notion is a great application to take note and organise them in a nice way. Their structure also very similar to Jupyter Notebook, so I want to transfer all my notebook folder to Notion automatically. Therefore, I spend a day to find a good way to do this.

# Instruction
Clone this repo. Go to /nbconvert and run command to install notion, md2notion, nbconvert.

        pip install -r requirements.txt

Then following these steps to obtain token_v2
1.  Open your browser and logged out from Notion.so (if logged in).
2.  Open Developer Tool and inspect the cookies
3.  Log in
4.  Find the row has the enrty as token_v2. Copy its value
5.  Go back to /nbconvert folder, open main.py using text editor
6.  Find token_v2, then replace it with the above token
7.  Go the end of the main function, replace the url with your Notion Page URL (Just make and empty one and copy from the URL bar) 
8.  Copy the script to folder contains Notebook(s), then run the script

# Requirements to run
This script will scan your folder and transfer all your Notebook(s) to your predefined Notion URL.  
Do not create any folder name "md" before running this script.  
This Script only transfer inputs/markdowns block of Notebook, all the outputs and figures will be remove.

### TO DO

- [X] Add dependencies 
- [X] Refactor code
- [X] Add a instruction
- [ ] Planning on adding features
