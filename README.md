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

Installing & Running the Client
1. Install Vue. NodeJs is needed for Vue
2. Install Material Design Bootstrap:
3. Go to client directory
4. Run 'vue add mdb'
5. Run client: 'npm run serve'
