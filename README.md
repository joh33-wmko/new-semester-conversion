New Semester Conversion
=======================
Updated: 27-Jul-2026

Converts PHP files to operate in IPYNBs

Organization:

Project root:

- php_files/ (originals)

- notebooks/ (.ipynb "notebooks")

- input_fules/ (.csv files exported from .xlsx|.xlsm files)

- output_files/ (.sql db import files)

- python_files/ (.py files for command line use, tbd)


IPYNB's for PHP -> Python conversion of the New Semester Observing Schedue

1. Staff Schedules (SA, OA, NA. but not EEOC)


- Run as xlsx files are  received


- Convert xlsx file to .csv file


- Enter the following into the .ipynb notebook:


  - type: SA, OA, or NA (not EEOC)

  - copy the .csv file to the project's input_files/ dir


- Execute the relevant cells in the notebook


- Find generated .sql files in the output_files/ dir


2. Telescope Scheudule


- Implement list of fixes (like replacing TBD with actual values, and check list of recent issues)


Container: TBD


Additional module(s): TBD


Reverts to manual procesing of xlsx -> sql files to db imports:


    - removes end-to-end automation


    - auto-filetype detection


    - auto db updates


    - separates telescope schedule from staff schedule


Development on local machine


- Run on any server (test on RTI Build and RTI Tools, TBD)

