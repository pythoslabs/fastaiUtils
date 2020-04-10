# To do

# About v2 :
# Removed all pathlib Path references and recreated with string paths


# Contains these methods 
# 1. create_validation_folders
# This creates the validation folders in the same directory as 'train' folder
# Moves a percentage ( pct ) of the files from the train directory to the 'valid' directory ( creates the dir if that does not exist)

# Assumptions
# 1.folder 'train' exists 
# The classes are defined as the sub-directories of the train folder


#from pathlib import Path
import os
import shutil
import random # to select random files from train folder

# ---------------------------------------

def count_files(DIR):
    return len(os.listdir(DIR))
# ---------------------------------------
def check_train_valid_sync(root_path):
    print(root_path)
    valid_folder = root_path+'/valid'
    train_folder = root_path+'/train'
    valid_classes = os.listdir(valid_folder)
    train_classes = os.listdir(train_folder)
    #print(train_classes)
    count_valid_minus_train = len(set(valid_classes)- set(train_classes))
    count_train_minus_valid = len(set(train_classes)- set(valid_classes))
    # Redo this ! 
    # This is not the right check .
    # Check if the same directories exist 
    if(count_train_minus_valid > 0 or  count_valid_minus_train > 0 ):
        print("Present in train , not in valid " + str(set(train_classes)- set(valid_classes)))
        print("--------")
        print("Present in valid , not in train " +  str(set(valid_classes)- set(train_classes)))
    else :
        print("Train and valid folders in sync")

# ----------------------------------------------------

def create_validation_folders(root_path,pct):
    '''
    version 2.0
    Removed the use of pathlib Path due to random errors in type conversion.
    Uses all string paths to denote

    Creates the validation folders and copies the files in the respective folders
    based on the folders present in the train folder
    root_path is the parent folder that contains the data ( in thr 'train' folder ( which has classes within it))
    '''

    train_folder = root_path+'/train'
    validation_folder = root_path +'/valid'

    if not os.path.exists(validation_folder):
        os.mkdir(validation_folder)


    train_classes = os.listdir(train_folder)
    print("Training classes  : %s" %(train_classes))

    # get count of each folder
    for train_class in train_classes :
        train_class_files = os.listdir(train_folder+'/'+train_class)
        no_of_files_train = len(train_class_files)

        print("Folder:train/%s - %d" %(train_class,no_of_files_train))
        if os.path.exists(validation_folder+'/'+train_class):
            print("Validation folder exists. Not creating")
            no_of_files_valid_existing = count_files(validation_folder+'/'+train_class)
            count_valid_file_ideal = (no_of_files_train+no_of_files_valid_existing)*pct
            count_valid_files_to_add = int(count_valid_file_ideal - no_of_files_valid_existing)

            print("Ideal count of validation files : %d" %(count_valid_file_ideal))
            print("%d files already existing in validation folder, %d more to add" %(no_of_files_valid_existing,count_valid_files_to_add))

            list_of_random_files  = random.sample(train_class_files,count_valid_files_to_add)
            #print(list_of_random_files)
            for file_to_move in list_of_random_files :
                src = train_folder+'/'+train_class+'/'+file_to_move
                dest = validation_folder+'/'+train_class+'/'+file_to_move
                shutil.move(src,dest)
            print("Moved %d files to validation folder %s\n--------\n" %(count_valid_files_to_add,validation_folder+'/'+train_class))


        else :
            print("Validation folder does not exist. Creating folder:%s" %(validation_folder+'/'+train_class))
            os.mkdir(validation_folder+'/'+train_class)
            count_valid_file_ideal = int(no_of_files_train*pct)
            print("number of files to create in valid folder = %d" %(count_valid_file_ideal))
            list_of_random_files  = random.sample(train_class_files,count_valid_file_ideal)
            for file_to_move in list_of_random_files :
                src = train_folder+'/'+train_class+'/'+file_to_move
                dest = validation_folder+'/'+train_class+'/'+file_to_move
                shutil.move(src,dest)
            print("Moved %d files to validation folder %s\n--------\n" %(count_valid_file_ideal,validation_folder+'/'+train_class))

# --------------------------------------------------------
# This creates a 'scoring' folder structure based on the 'training' folder structure
# Make sure you move all the files from the scoring folder to test folder
# Run the function - moveScoringFiles(path) -  to do it
# This is NOT for multilabel classification - this is only for single label
def create_score_folder_structure(root_path):
    score_folder = root_path+'/score'
    train_folder= root_path+'/train'

    if (os.path.exists(score_folder)):
        #shutil.rmtree(score_folder)
        print("WARNING ! The score folder already exists - Delete or look into  ")
    else :
        os.makedirs(score_folder)

    train_classes = os.listdir(train_folder)
    for train_class in train_classes :
        if not os.path.exists(score_folder+'/'+train_class) :
            print("Creating folder %s" %(train_class))#create the folder
            os.makedirs(score_folder+'/'+train_class)

    print("Score directory structure created ")

# ------------------------------------------------------
def move_validation_files(root_path):
    '''
    Moves all the images in the validation folder
    back to their corresponding classes in train folder
    Note: Remember to run the 'create_validation_folders' function after this
    '''
    root_path= Path(root_path)
    valid_folder = root_path+'/'+'valid'
    train_folder= root_path+'/'+'train'

    valid_classes = os.listdir(valid_folder)
    print(valid_classes)
    for valid_class in valid_classes :
        if(os.path.exists(train_folder+'/'+valid_class)) :
            valid_class_files = os.listdir(valid_folder/Path(valid_class))
            no_of_files_valid = len(valid_class_files)
            for file_to_move in valid_class_files:
                src = valid_folder+'/'+valid_class+'/'+file_to_move
                dest = train_folder+'/'+valid_class+'/'+file_to_move
                #print("src = %s dest = %s" %(src,dest))
                shutil.move(src,dest)
            print("%d file moved to %s" %(no_of_files_valid,valid_class))
        else :
            print("ATTENTION - Train folder - %s - does not exist" %(valid_class))

# ------------------------------------------------------

#Moves all the SCORED files ( in score folder) back into the test folder
def move_scoring_files(root_path):
    root_path= Path(root_path)
    score_folder = root_path/'score'
    test_folder= root_path/'test'
    score_classes = os.listdir(score_folder)
    for score_class in score_classes :
        score_class_files = os.listdir(score_folder+'/'+score_class)
        no_of_files_score = len(score_class_files)
        for file_to_move in score_class_files:
            src = score_folder+'/'+score_class+'/'+file_to_move
            dest = test_folder+'/'+file_to_move
            shutil.move(src,dest)
            #print("Moving file %s to test" %(src))
        print("Moved %s file(s) from %s to test" %(score_class,no_of_files_score))
