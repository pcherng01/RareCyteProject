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
	- For variable vlue, copy the full python application path
		- Use semicolon and add Python Scripts path after the semicolon
	This is how my Variable value would look like:
		C:\Users\Leaf\AppData\Local\Programs\Python\Python38-32
		;C:\Users\Leaf\AppData\Local\Programs\Python\Python38-32\Scripts
	- Click 'Ok'
	- Close the shell/PowerShell 
- Install flask:
	- Run 'pip install flask
	- Run 'pip install virtualenv'
	- Run 'pip install flask-cors'
- Go to server folder
- Run 'py app.py' in shell
- You should see the server started

Client:
- Make sure you have npm installed
- Run 'npm install -g @vue/cli' to install Vue
- Add vue to path (Similar to how we added Python to PATH)
- Edit the Path variable, click 'New'
- Add 'C:\Users\YourUserName\AppData\Roaming\npm'
	- Mine looks something like 'C:\Users\Leaf\AppData\Roaming\npm'
- Download the latest Node and update to latest npm
- Go to client folder, run 'npm i'
- Then run 'npm run serve'
