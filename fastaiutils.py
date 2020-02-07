from pathlib import Path
import os
import shutil

def count_files(DIR):
    return len(os.listdir(Path(DIR)))

            
def checkTrainValidInSync (root_path):
    root_path= Path(root_path)
    valid_folder = root_path/'valid'
    train_folder= root_path/'train'
    valid_classes = os.listdir(valid_folder)
    train_classes = os.listdir(train_folder)
    #print(train_classes)
    count_valid_minus_train = len(set(valid_classes)- set(train_classes))
    count_train_minus_valid = len(set(train_classes)- set(valid_classes))
    
    if(count_train_minus_valid > 0 or  count_valid_minus_train > 0 ):
        print("Present in train , not in valid " + str(set(train_classes)- set(valid_classes)))
        print("--------")
        print("Present in valid , not in train " +  str(set(valid_classes)- set(train_classes)))
    else :
        print("Train and valid folders in sync")
        
def create_validation_set(root_path,pct):
    '''
    Creates the validation folders and copies the files in the respective folders 
    based on the folders present in the train folder
    '''
    train_folder = Path(root_path/'train')
    validation_folder = Path(root_path/'valid')
    train_classes = os.listdir(train_folder)
    print("Training classes  : %s" %(train_classes))
    
    # get count of each folder 
    for train_class in train_classes :
        train_class_files = os.listdir(train_folder/Path(train_class))
        no_of_files_train = len(train_class_files)
        
        print("Folder:train/%s - %d" %(train_class,no_of_files_train))
        if os.path.exists(validation_folder/Path(train_class)):
            print("Validation folder exists. Not creating")
            no_of_files_valid_existing = count_files(validation_folder/Path(train_class))
            count_valid_file_ideal = (no_of_files_train+no_of_files_valid_existing)*pct
            count_valid_files_to_add = int(count_valid_file_ideal - no_of_files_valid_existing)
            
            print("Ideal count of validation files : %d" %(count_valid_file_ideal))
            print("%d files already existing in validation folder, %d more to add" %(no_of_files_valid_existing,count_valid_files_to_add))
            
            list_of_random_files  = random.sample(train_class_files,count_valid_files_to_add)
            #print(list_of_random_files)
            for file_to_move in list_of_random_files :
                src = train_folder/Path(train_class)/file_to_move
                dest = validation_folder/Path(train_class)/file_to_move
                shutil.move(src,dest)
            print("Moved %d files to validation folder %s\n--------\n" %(count_valid_files_to_add,validation_folder/Path(train_class)))    
           
            
        else : 
            print("Validation folder does not exist. Creating folder:%s" %(validation_folder/Path(train_class) ))
            os.mkdir(Path(validation_folder/Path(train_class)))
            count_valid_file_ideal = int(no_of_files_train*pct)
            print("number of files to create in valid folder = %d" %(count_valid_file_ideal))
            list_of_random_files  = random.sample(train_class_files,count_valid_file_ideal)
            for file_to_move in list_of_random_files :
                src = train_folder/Path(train_class)/file_to_move
                dest = validation_folder/Path(train_class)/file_to_move
                shutil.move(src,dest)
            print("Moved %d files to validation folder %s\n--------\n" %(count_valid_file_ideal,validation_folder/Path(train_class)))    

            
#Make sure you move all the files from the scoring folder to test folder 
# Run the function - moveScoringFiles(path) -  to do it 
def createScoreFolderStructure(root_path):
    root_path= Path(root_path)
    score_folder = root_path/'score'
    train_folder= root_path/'train'
    
    if (os.path.exists(score_folder)):
        shutil.rmtree(score_folder)
    os.makedirs(score_folder)
    
    train_classes = os.listdir(train_folder)    
    for train_class in train_classes :
        if not os.path.exists(score_folder/train_class) :
            print("Creating folder %s" %(train_class))#create the folder
            os.makedirs(score_folder/train_class)



def moveValidtionFiles(root_path):
    '''
    Moves all the images in the validation folder 
    back to their corresponding classes in train folder 
    Note: Remember to run the 'create_validation_set' function after this
    '''
    root_path= Path(root_path)
    valid_folder = root_path/'valid'
    train_folder= root_path/'train'
    
    valid_classes = os.listdir(valid_folder)    
    print(valid_classes)
    for valid_class in valid_classes :
        if(os.path.exists(train_folder/valid_class)) :
            valid_class_files = os.listdir(valid_folder/Path(valid_class))
            no_of_files_valid = len(valid_class_files)    
            for file_to_move in valid_class_files:
                src = valid_folder/Path(valid_class)/file_to_move
                dest = train_folder/Path(valid_class)/file_to_move        
                #print("src = %s dest = %s" %(src,dest))
                shutil.move(src,dest)
            print("%d file moved to %s" %(no_of_files_valid,valid_class))    
        else :
            print("ATTENTION - Train folder - %s - does not exist" %(valid_class))

#Moves all the SCORED files ( in score folder) back into the test folder
def moveScoringFiles(root_path):
    root_path= Path(root_path)
    score_folder = root_path/'score'
    test_folder= root_path/'test'
    score_classes = os.listdir(score_folder)    
    for score_class in score_classes :
        score_class_files = os.listdir(score_folder/Path(score_class))
        no_of_files_score = len(score_class_files)    
        for file_to_move in score_class_files:
            src = score_folder/Path(score_class)/file_to_move
            dest = test_folder/file_to_move        
            shutil.move(src,dest)
            #print("Moving file %s to test" %(src))
        print("Moved %s file(s) from %s to test" %(score_class,no_of_files_score))            
