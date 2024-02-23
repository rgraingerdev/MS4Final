Welcome To the Megashop, The Megashop and everything it stands for are the focus of this website. You can Win prizes or dream holidays.

## Getting Started

Visit https://megashop-d3bc08f15f0a.herokuapp.com on your preferred web browser to access the Developer friends Page. The website is completely responsive; regardless of whether you're using a desktop computer, tablet or smartphone, it should look excellent on all of them.

## User Storys
I have developed user stories to direct my design and development process; in order to make sure that the Developer friends Page satisfies the requirements of my users. Here are some usage examples for user stories:


* As a developer i want a way to broaden my development skills.
* I want to be able to see current prizes.
* I want to be able add things to my basket.
* I want to be able to add and edit current stock.
* I want to learn more about coding.
* i want to be able to easily navigate the website.
* I want to be able to view the webpage on mobile or tablet.


By developing user stories, I can make sure that the website satisfies user needs and offers a satisfying browsing experience. I regularly gather user feedback and apply it to the design and functionality of the website.

## UI/UX

* The aim is for a first-time user to be able to easily navigate.
* The colour scheme was chosen to be easy on the eye and not draw attention away from content. 
* This page was made so that both new and current members can enjoy.

### Future features
* Add a group messageboard for users to ask questions and disscuss together.
* More categorys for the prizes.
* Add examples and links to past winners page.

### Font

* Roboto was the font I chose. The typeface was picked because it is slick and simple for the end user to read, additionally it comes from Google Fonts.


## Technologies used
* HTML - Was used for the structure of the page.
* CSS - was used for the style of elements.
* Python - Was used to add to create backend tables and interactivity.
* Django - Was used as the main framework
* SQLalchemy - used for creating tables to store user information.
* ElephantSQL - Used to manage tables
* Github - is the hosting site for storing the code and version control.
* Heroku - was used to deploy the site.
* balsamiq - used for wireframes.
* Fontawesome - for icons on navbar.
* Devtools - used for debugging and testing to ensure responsiveness.
* Google chrome lighthouse - used for testing.
* W3C HTML Validator - used for validating HTML of the page.
* W3C CSS validator - used for validating CSS of the page.

## Testing
The Megashop has undergone comprehensive testing to guarantee that it operates properly and offers a satisfying user experience. The website has been tested on a variety of hardware, browsers, and operating systems, including:

Systems running Windows, macOS, and Linux.
Web browsers such as Safari, Edge, Firefox and Chrome that can run on mobile and desktop.
I carried out user testing to gather opinions from people. I used this feedback to improve the website's functionality and appearance.

Please contact me via the website's contact form if you experience any problems while using the CCFC Fan Page. I consider all comments carefully and attempt to resolve any problems as soon as possible.

### Page Testing

Testing began with automated testing as per the table below with screenshots.

|Test |Lighthouse| W3 html validator| W3 schools jigsaw| 
|-----|-----|-----|-----|
|Home| Pass| Pass| Pass|
|Products| Pass| Pass| Pass|
|Payment| Pass| Pass| Pass|
|My Details| Pass| Pass| Pass|
|Sign in| Pass | Pass| Pass|

### Manual testing

#### Home

| Feature | Expect | Action | Result | Pass/Fail |
|-----|-----|-----|-----|-----|
|Enter button| To navigate to history page | clicked the enter button | Opened history page correctly | |
|Nav links | When clicked navigate to page | Clicked all nav links on all pages| All pages opened as expected| Pass
|Menu Drop down | To drop down on mobile and tablet devices | opened on mutiple devices and pressed button | menu droped and displayed correctly| Pass|

### Store
| Feature | Expect | Action | Result | Pass/Fail |
|-----|-----|-----|-----|-----|
|Nav links | When clicked navigate to page | Clicked all nav links on all pages| All pages opened as expected| Pass
|Menu Drop down | To drop down on mobile and tablet devices | opened on mutiple devices and pressed button | menu droped and displayed correctly| Pass|

#### Sign in

| Feature | Expect | Action | Result | Pass/Fail |
|-----|-----|-----|-----|-----|
|Nav links | When clicked navigate to page | Clicked all nav links on all pages| All pages opened as expected| Pass
|Form submission| Does not allow sign in without sign up| input invalid credentials| did not allow sign in| Pass
|Form submission| Allows sign in with correct credentials| Input valid credentials| Sign in successful| Pass


#### Sign up

| Feature | Expect | Action | Result | Pass/Fail |
|-----|-----|-----|-----|-----|
|Nav links | When clicked navigate to page | Clicked all nav links on all pages| All pages opened as expected| Pass
|Form submission| Does not allow empty or invalid input| Input invalid informatian| did not allow sign up| Pass
|Form submission| Allows sign up with proper information| Input correct information| Allowed sign up | Pass
|Credential storage| Stores credentials in correct tables| Submitted input| Checked postgre table for information| Pass


Continuing with testing, I tested the page across multiple devices (iPhone, Galaxy Fold, Edge and Firefox) ensuring all links and pages loaded all elements correctly and promptly.

### known bugs

Bugs found during writing have been fixed. 

## Local Development

To develop this repository locally, you will need to do the following:

1. Install PostgreSQL (Version 15), though with modification to the DB_URI env key you can use another relational
   database.
2. Install Python (Version 3.10).
3. Clone this repository.
    - This can be done by either using `git clone https://github.com/rgraingerdev/MS3` in
      the terminal, or by using GitHub Desktop.
4. Create a virtual environment.
    - This can be done by using `python -m venv venv` in the terminal.
    - The purpose of a virtual environment is to keep the dependencies for this project separate from other projects.
5. Activate the virtual environment.
    - This can be done by using `source venv/bin/activate` in the terminal.
6. Install program requirements.
    - This can be done by using `pip install -r requirements.txt` in the terminal.
7. Create a `.gitignore` file and add `env.py`.
8. Create the env.py file in the root of your project directory.
9. Add the following to env.py

- ```python
   import os

   # Set IP for Flask Server - 0.0.0.0 uses all IPs on Device
   os.environ.setdefault("IP", "0.0.0.0")
        
   # Set Port for Flask Server - 5000 is common but interferes with Airport on macOS
   os.environ.setdefault("PORT", "5555")
        
   # Set Debug to True - Enables development server for Flask
   # Remove this key before deploying to production
   os.environ.setdefault("DEBUG", "True")
        
   # Set SECRET_KEY for Flask Flashes
   os.environ.setdefault("SECRET_KEY", "<SECRET_KEY>")
        
   # Database Connection String
   os.environ.setdefault("DB_URI", "postgresql://user:password@hostname/database_name")

10. Run the run.py file.
    - This can be done by using `python run.py` in the terminal.

## ElephantSQL

1. Logged into ElephantSQL via GitHub.
2. Selected 'Create New Instance'.
3. Named DB 'Developer_friends' and selected 'Tiny Turtle' plan.
4. Selected Region.
5. Confirm creation.

## Deployment from github repository to Heroku
1. At the heroku dashboard, click "New" and the select create new app
2. Chouse a unique name for your app 
3. Under "Deployment method" section, select github
4. Connect your Heroku app to your Github repositry by searching for and selecting the repo.
5. Choose a branch to deploy.
6. Click "Enable automatic deplys" to allow heroku to redeploy the app when changes are pushed.
7. Click Deploy branch.

## Creating a fork
1. Navigate to the [repository](https://github.com/rgraingerdev/MS4Final)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description 
4. Choose to copy only the main branch or all branches to the new fork. 
5. Click Create a Fork. A repository should appear in your GitHub.

### Cloning Repository
1. Navigate to the [repository](https://github.com/rgraingerdev/MS4Final)
2. Click on the Code button on top of the repository and copy the link. 
3. Open Git Bash and change the working directory to the location where you want the cloned directory. 
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

## Acknowledgements
* Thank you to my mentor for supporting me through this project
* Everybody on slack for answering any questions I had along the way.
* Project structure from Boutiqe ado project
* Models from boutique ado
