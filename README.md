# fastaiUtils
All the helper functions for fastai


* _**fastaiutils.py**_  
 All the functions in one file ( that you can import directly into your code ) 
 import fastaiutils as futils

#----------------------------

These are util functions to be used along with fast.ai ( version 2 ) package

* _**checkTrainValidInSync.py**_  
 Checks if all the classes (folders) in train are also present in validation  ( Checks for only the folder structure - not the number of files )


* _**createScoreFolderStructure.py**_  
 Creates folder structure for the scoring folder in the same structure as train folder.


* _**create_validation_set.py**_  
 Creates a validation folder ( in the same structure as the train folder along with the class folders within) 


* _**moveScoringFiles.py**_  
 Moves the files in the scoring folder back into the test folder. 


* _**moveValidtionFiles.py**_  
 Moves the files in the validation folder structure back to its corresponding training fodler strucutre.





