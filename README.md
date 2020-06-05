# RareCyteProject
Server (For Windows):
- Install Python by downloading python3 
	- https://www.python.org/downloads/
- Add python to path:
	- Right click on 'This PC' icon then select 'Properties'
	- Click on 'Advanced system settings'
	- Click on 'Environment variables...'
	- Click on 'New...' located user User variables box
	- For Variable name, type 'Path'
	- For variable value, copy the full python application path
		- Use semicolon and add Python Scripts path after the semicolon
	This is how my Variable value would look like:
		C:\Users\Leaf\AppData\Local\Programs\Python\Python38-32
		;C:\Users\Leaf\AppData\Local\Programs\Python\Python38-32\Scripts
	- Click 'Ok'
	- Close & restart the shell/PowerShell 
- Install pip:
	- Run 'py get-pip.py'
- Install flask:
	- Run 'py -m pip install flask
	- Run 'py -m pip install virtualenv'
	- Run 'py -m pip install flask-cors'
- Go to server folder
- Run 'py app.py' in shell
- You should see the server started

Client:
- Download the latest Node from the official Node website: https://nodejs.org/en/download/
	- When installing, click 'Add to Path'
- Make sure you have npm installed
- Run 'npm install -g @vue/cli' to install Vue
- Add vue to path (Similar to how we added Python to PATH)
	- Edit the Path variable, click 'New'
	- Add 'C:\Users\YourUserName\AppData\Roaming\npm'
		- Mine looks something like 'C:\Users\Leaf\AppData\Roaming\npm'
- In some cases, PowerShell will block script from running, thus it cannot run vue commands. More info: https://stackoverflow.com/questions/57673913/vsc-powershell-after-npm-updating-packages-ps1-cannot-be-loaded-because-runnin
- Run 'Set-ExecutionPolicy RemoteSigned' in PowerShell
- Go to client folder, run 'npm i'
- Then run 'npm run serve'
