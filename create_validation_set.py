# Creates the validation folders based on the train folder class structure 
# Copies files from the train folder structure into each of the class folders in the validatin folders


def count_files(DIR):
    return len(os.listdir(Path(DIR)))



def create_validation_set(root_path,pct):
    '''
    Creates the validation folders and copies the files in the respective folders 
    based on the folders present in the train folder
    '''
    train_folder = Path(root_path/'train')
    validation_folder = Path(root_path/'valid')
    train_classes = os.listdir(train_folder)
    print(train_classes)
    
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
            print("%d files already existing in validation folder " %(no_of_files_valid_existing))
            print("%d more to add" %(count_valid_files_to_add))
            
            list_of_random_files  = random.sample(train_class_files,count_valid_files_to_add)
            #print(list_of_random_files)
            for file_to_move in list_of_random_files :
                src = train_folder/Path(train_class)/file_to_move
                dest = validation_folder/Path(train_class)/file_to_move
                shutil.move(src,dest)
            print("Moved %d files to validation folder %s" %(count_valid_files_to_add,validation_folder/Path(train_class)))    
           
            
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
            print("Moved %s files to validation folder %s" %(validation_folder/Path(train_class)))    
    return 0
