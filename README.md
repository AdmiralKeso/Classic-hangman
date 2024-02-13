# Quiz Master 2022

[Link to Live Site](https://classichangman-281d9c7c84a8.herokuapp.com/)


## Table of Contents
- [Introduction](#introduction)
- [UX  ](#ux)
  * [Typography](#typography)
  * [Wireframes](#wireframes)
- [Features ](#features)
  * [Existing Features](#existing-features)
    + [Main Menu](#main-menu)
    + [Play Quick Quiz Round](#play-quick-quiz-round)
    + [Create Custom Quiz](#create-custom-quiz)
    + [Create Google Form Quiz](#create-google-form-quiz)
    + [Help](#help)
    + [Quiz Classes](#quiz-classes)
    + [Google Drive Utility Menu](#google-drive-utility-menu)
  * [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [External Python Packages Used](#external-python-packages-used)
- [Testing ](#testing)
  * [User Story Testing](#user-story-testing)
  * [Challenges Faced](#challenges-faced)
  * [Code Validation](#code-validation)
- [Deployment](#deployment)
- [Credits ](#credits)
  * [Content ](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## Introduction

The project is a Python command line application where you would play classic hangman against the computer. The computer chooses a random word and you will need to guess it before the stick figure is complete. If the stick figure is complete, you get hanged and the game is over but you can try again.

## UX  

The user will first read the rules and then press enter to start the game.
Messages will appear if right or wrong.
If user inputs same letter twice, error message pops up.
User will have the choice to play again at the end.


### Wireframes

I used the code institutes template and altered the python file.

#### Main Menu

The main menu is where you find information about the game. 
It displays to the user a welcome message and the user can choose to start the game.

#### Start game

The game begins and the user can pick a letter of choice. When the letter is picked and is part of the word the letter pops up in the word box.
The user has 6 tries before the game is over.

#### Play Again

The user will have the choice of playing again. The input is yes or no. If yes the game will start again from the begin. And if no. Application closes.

### Features Left to Implement

- More words and different words.
- Better ui
- Increased difficulity

## Technologies Used

- [Python](https://www.python.org/)
- [GitHub](https://github.com/) for storing the repository online during development.
- [PEP8-Online-Validator](https://pep8ci.herokuapp.com) for validation of the python file.

## Testing 

Testing was done using the terminal to ensure that the project was developed in the right way. When the project was deployed. It was tested using a desktop, laptop and mobile to ensure that it was playable on all devices.

### Code Validation

All the files pass PEP8 Validation, There is just a minor issue with the run.py file where the hangman uses whitespace which couldnt be fixed.

## Deployment

I deployed to Heroku using the Heroku CLI with the following steps
    - Create a new App in the Heroku web dashboard named 'classic-hangman'
    - In the Heroku Dashboard Settings, under Config Vars - add the contents of the `PORT` with a value of `8000`
    - Under Buildpacks, add Python and Nodejs and click save.
    - Connect the project with github.
    - Deploy the project.

## Credits 

### Content 

- [Code Institute Python Essentials](https://github.com/Code-Institute-Org/python-essentials-template) Template I used for my project.
I have only worked with the run.py file.

### Acknowledgements

- My mentor Mitko provided me good information and knowledge to complete this project.
- Slack community
