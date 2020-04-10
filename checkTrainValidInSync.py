# Checks if all the classes (folders) in train are also present in validation 
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
