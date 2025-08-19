---
title: |
  \vspace{-2cm} CSC 110\
  Introduction to Computer Science
subtitle: |
  **Homework Assignment 0**\
  Conditionals
geometry: margin=2cm 
header-includes: |
  \setlength{\headsep}{1cm}
  \hypersetup{colorlinks=true,
    urlcolor=[RGB]{6,69,173},
    linkcolor=[RGB]{6,69,173}}  
  \usepackage{color}  
output:
  pdf_document:
    highlight-style: monochrome
---
\vspace{-5\baselineskip}

**Due: Before Lecture 5**
 
*Note: Homework Assignment 00 should be completed individually.*


# Objective

This is a simple repository with one Readme (this one) and one simple executable python file (hw00.py)
Your objective is to READ all of these instructions and Only after you are finished, to FOLLOW any steps you were asked to complete.

# A Note on passing the tests

This assignment has no runnable tests. Those will come later. 

# Tasks

## Task 1: read the whole thing

Everything these days is "immediate feedback" this, and "rapid interaction" that.
We're being made addicted to instant gratification and feedback to such a degree that anything that takes longer than 2 or 3 minutes to do, starts feeling boring. Reading, is one of those things.

In this class, you'll have to read and follow instructions. A LOT of them, and quite often, they are complex and convoluted. They are, however, all quite doable. 
The biggest things you will absolutley need in order to succeed, is to be able to read, focus, and pay attention to details. This is your first go at it.

Read all of these instructions and only then go back and "DO" the things you need to modify or execute.

## Reading 1:

The Command Line Interface (CLI) is a program that allows users to communicate with the computer's operating system using text commands. 
It is a simpler method of interacting with your computer than the one most people are used to now, which is the Graphical User Interface, or GUI.
While a GUI just requires that you move a mouse and click on icons or buttons, in a CLI, you type commands and execute them. 
The result can be 1) symbols printed to the terminal window, 2) changes made to files, 3) programs being executed, or all of the above.

In a CLI, we use a window called a **Terminal** or a Console, that has a typing and reading area. 
Working under the hood of this window, a program called the **Shell** can read what the user writes and can take actions like printing out information to the window, 
changing the state of the filesystem, or running other programs (playing sounds, starting up zoom, or running python). 

When a user writes into the Terminal, it is important that they use instructions KNOWN to the Shell, otherwise it will not know what you mean. 
There are different Shell programs, but they mostrly do the same things. 
We will use the one called Bash, mostly, but you don't need to worry about memorizing its commands, since we will be only using it to:

  - move around in the filesystem, and
  - call python programs

## Task 2: Use the Terminal to focus on the program location

  * Open a Terminal window (Mac: search for Terminal; Win: Search for Windows Terminal)
  * You'll be focused at the filesystem location called home:
      *  Mac: /Users/`<username>` (e.g. /Users/pfrank)
      *  Win: C:\Users\`<username>` (e.g. C:\Users\pfrank)... and yes, Win uses backslash (╯°□°）╯︵ ┻━┻
      *  Linux: /home/`<username>` (e.g. /home/pfrank)
  * In Mac/Linux, the symbol ~ (tilde) is a nickname for /Users/<username> or /home/<username> respectively.
  * In windows, you also have a ~ but it points to the linux home (I can explain this later).
      * So, when in Win, I refer to ~, I mean C:\Users\\<username\>
  * Navigate to ~/Documents/csc110/`<name of this repository directory>`
  * if you execute the command `ls`
      * you should see the Readme.md and the file called hw00.py 

## Task 3: execute the original version of the program
  * if you execute the command `python3 hw00.py`
      * you should see the output printed to the terminal
      * If it doesn't work, try   `python3.13 hw00.py`

## Task 4: modify the original version of the program
  * Open the file using Sublime Text.
  * Modify the code so that, you do the following:
      1. remove the `, end=""` at the end of the third print. Note it includes the comma. Taking care to close the parenthesis.
      2. modify the text of what remains the third print so it reads: ``
      3. modify the text of what was the fourth print so it reads: `~~~ NOTE: this is NOW in a new line ~~~`
  * save the file and execute it again (in the terminal): `python3 hw00.py`
  * Verify the output looks like this:
```
hello world
printed line 2: (the default is to add a line jump at the end)
printed line 3: (this line also adds a default jump)
~~~ NOTE: this is NOW in a new line ~~~
```

## Submitting

  * Once you do what the Readme asks, you need to learn to submit it.
  * Tl;DR: I will explain, in class, how to do this.
  * Detailed explanation:
      * you will use the git command line program to
   
        
# Grading

## Grading criteria:

### General
The submission:

  * **IMPORTANT**: If your code does not compile, you lose 50% of your grade so make sure you run your code often (to avoid syntax or runtime errors) and you always have it in a "running" state,even if it does not get the desired results.
  * Your grade will be the percentage of tests you pass. If there are no tests (like in this HW, then it just needs to compile and do what the Readme asks).


          1. Stage: add al necessary files to the list of tracked files
          2. Commit: save a checkpoint in the history of modifications (if you have not already done this)
          3. Push: push changes to your remote repository
I can see and grade all remote repositoriesof your hw00 files and will grade them at the due date/time so make sure it is complete and running by then.
