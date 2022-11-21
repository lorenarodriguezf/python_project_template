 This document contains additional instructions about how to use this Python
project template.

Getting Started in VSCode
=========================

To get an initial virtual environment for your project, perform the following
steps:

  1. Type `Ctrl-Shift-P` and enter "Tasks: Run Tasks", hit the `Enter` key
  2. Select the task "Create Virtual environment" and hit the `Enter` key
  3. A message box will popup about noticing a new virtual environment and
     whether this should be used for the workspace. Choose 'Yes'

The full tutorial to get started with Python under VSCode can be found here:
https://code.visualstudio.com/docs/python/python-tutorial


Submission via Moodle or other LMS
==================================

From the root directory of your project run the following git command:

    git bundle create <projectname>.bundle --all

Now you can simply upload the newly created file `<projectname>.bundle` to
Moodle.

Make sure you replace `<projectname>` in the above examples with a name that
identifies your own project.

Using the provided VS Code task
-------------------------------

Alternatively you can also use the VS Code task "Bundle for Submission" by
following these steps:

  1. Type `Ctrl-Shift-P` and enter "Tasks: Run Tasks", hit the `Enter` key
  2. Select the task "Bundle for Submission" and hit the `Enter` key

Now you should find a `.bundle` file in your project folder that is named
with your project folder name. This can be submitted to Moodle.