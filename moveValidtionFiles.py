# Moves files from validation forlder back to train folder
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
