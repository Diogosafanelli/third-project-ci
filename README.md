# ATM Bank

 With the ATM bank project you will have access to your bank account being able to perform all the most common services of a common bank such as checking your balance, making a deposit, withdrawing money

The project is deployed on Heroku and is strictly terminal-based for user interaction

 - Here is the link to the final project > [ATM](https://atm-3d08234ef3ca.herokuapp.com/)

 
![am I responsive ATM](https://github.com/Diogosafanelli/third-project-ci/assets/131887685/0ea9402f-ae07-41b8-ad04-4050186dc7cd)


 ## UX/UI Design
 <hr>

 ### Strategy

#### Site owner goals

- ATM bank is a project for those who love money, you will have the experience of having an ATM inside your home, being able to do your banking transactions in the comfort of your home, of course this is just a fun experience of how to deal with an atm inside your home

#### User stories

- As a user, I want to understand the purpose of the website, so I can know if it's of interest to me.
- As a user, I want to easily navigate the site/ATM, so I don't lose enthusiasm for using the site.
- As a user, I want to be able to learn something new, so I fulfill the objective that brought me to the site.
- As a user, I want to be able to restart/quit the ATM, if it is in my interest to start again for some reason

### Scope

- For the ATM Bank I have planned the following features.
  - Use of the python language efficiently to make the ATM don't show any problems.
  - Through the terminal-based, display as clearly as possible the ATM dynamic.
  - Use technologies and tools that improve site development and performance.


### Structure

The ATM Bank project structure is based on a single static web page with the terminal-based to run the game.

### Surface

#### Colour scheme

- To make the ATM Bank more intuitive and to highlight certain aspects such as suits, selection options or to highlight one information differently from another. I chose to use ANSI colors in the terminal.


## Features
<hr>

### Existing Features


#### Main menu

- When you start the program, the main menu is displayed. In which the name of the ATM/project appears in Green followed by the initial options for the user to run. These are [Mike] to Username, [2122] to PIN, and [Q] to close the program.

![ATM main page](https://github.com/Diogosafanelli/third-project-ci/assets/131887685/7d96b2b0-d11b-4010-b223-fb44fe80724a)
 
#### Rules

- When selecting the menu, the terminal will show a list containing Guide instructions and the objective of the ATM

![ATM menu page](https://github.com/Diogosafanelli/third-project-ci/assets/131887685/4e31f242-0520-4e17-829c-964815c91eed)

#### Quit

- When you execute the exit option, the program will be closed. It will no longer give the player the option to execute any commands, only after restarting the page or through the run button

![ATM Exit page](https://github.com/Diogosafanelli/third-project-ci/assets/131887685/d4213844-c07f-4078-b5d0-29025197cad5)

#### Selecting Opcions 

- Is executed right after the User chooses option [1, 2, 3, 4] to access. Before starting he must choose between one of the options to decide whether to withdraw, deposit or check the balance

![ATM options page](https://github.com/Diogosafanelli/third-project-ci/assets/131887685/3278b258-9ed8-416f-8f65-ad276d08cacd)


### Features Left to Implement

- To be implemented in the future, I am thinking about the possibility of adding a ranking that receives the users name defeat points. This ranking would be accessed from the menu to encourage users to try to use the program more often to become a regular customer.


## Testing
<hr>
- During these tests, the size of the displays was adjusted, when to clean the terminal to keep the ATM fixed. In the end, I found what I believe to be the most pleasing and intuitive look for the scope of a terminal-based ATM.


### Funcionality

- Once the ATM Bank was finished, I tryed it several times to find possible flaws or errors that could compromise the performance or interrupt the ATM. All commands are responding as they should, when some wrong selection is sent to the terminal, the answers are appearing to the user. So far, when I finished and made the final deployment, the ATM is responding with no apparent errors.

### Navegation and Devices

- Desktop
  - Sony Vaio (Laptop)
  - Dell XPS (Laptop)
  - Asus Chromebook (Laptop)
  - Macbook Air (Laptop)
  - HP (CPU)

- Browsers
  - Chrome
  - Firefox
  - Safari
  - Edge  
  

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
