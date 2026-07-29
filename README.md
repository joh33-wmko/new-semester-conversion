New Semester Conversion
=======================

Converts PHP files to operate in IPYNBs

- Development on local machine to run on any server

- Caveat: Reverts to manual procesing of xlsx -> sql files to db imports removes 
end-to-end automation, auto-filetype detection, auto db updates, separates telescope schedule from staff schedule


Organization:

- Project root

  - php_files/ (originals)

  - notebooks/ (.ipynb "notebooks")

  - input_fules/ (.csv files exported from .xlsx|.xlsm files)

  - output_files/ (.sql db import files)

  - python_files/ (.py files for command line use, tbd)


Container: TBD


Additional module(s): TBD


IPYNB's: 

1. Staff Schedules (SA, OA, NA. but not EEOC)


    - Run as xlsx files are  received


    - Convert xlsx file to .csv file


    - Copy the .csv file(s) to the project's input_files/ dir


    - Enter the following into the .ipynb notebook:


      - type: SA, OA, or NA (not EEOC)


      - input .csv filename in input_files/


      - date range (TBD)


    - Execute the relevant cells in the notebook


      - Find generated .sql files in the output_files/ dir



2. Telescope Scheudule


   - Implement list of fixes (like replacing TBD with actual values, and check list of recent issues)



[Updated: 27-Jul-2026]
