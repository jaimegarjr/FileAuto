# FileAuto - automating files

Hello! This is FileAuto.

This project is a Python automating script that allows for maintaining and cleaning a user's Downloads folder. The script mainly relies off the os and watchdog modules provided by Python. The idea was to continue experimenting with Python automation, and so this is what was able to come from that.

Below details the basic functionality of the program, as well as installation and usage commands.

## **_Installation_**

First clone the Github repository into a safe location and move into the created directory to create the .env file with your Downloads path.

```
git clone "https://github.com/JJgar2725/FileAuto.git"
cd FileAuto
touch .env
```

Inside the .env file, your Downloads folder path should be in the following format:

```
PATH_TO_DOWNLOADS=your path goes here
```

## **_Windows Usage_**

After cloning the repository, you may want to casually use the script manually by opening it in PyCharm IDE, or using VS Code with the Python extension. You can simply do this by opening the folder in your preferred text editor, and run it from there.

However, if you're interested in making the script run in the background at all times, you'd follow the following steps on a Windows machine.

1. Decide on a location that you want the script to be in at all times. 
2. Click the Windows icon at the bottom right of the desktop and type in Task Scheduler to open the task scheduling interface.
3. From here, you can select the 'Create task...' option on the top right. 
4. Name the task whatever you like - it can be FileAuto so you can tell it apart from other preset tasks on your machine.
5. Select the Actions tab and select 'New...', and here you'll be prompted with entering a script. This is where you should find your python.exe file and paste in the path to it. If you'd also like the script to run without opening a GUI or terminal, you can find the location of the python.exe path, and append a 'w' to the python.exe file. In other words, instead of it being ```/path/to/python.exe```, it'd be ```/path/to/pythonw.exe```.
6. Next, in the 'Add arguments box', type in the name of the FileAuto script, in this case it would just be ```fileauto.py```.
7. In the 'Start in' box, you'd want to type in the path to the FileAuto script - this is why I mentioned this in step 1 in order to comfortably find the fileauto.py path. (Example: C:/Users/youruser/Projects/FileAuto)
8. Before continuing, select the 'Action:' drop down menu, and select the 'Start a program' option.
9. Next, click on the Triggers tab, and select 'New...'. From here, you can simply open the drop down menu to select 'On system startup'. This will start the python script at startup so it will consistently clean and organize your Downloads folder. In the case that the script stops working, simply come back to Task Scheduler and restart the task from the list of tasks in the main task list.
10. You're done! Enjoy :).

## **_Mac Usage_**

FIXME: Coming Soon!
