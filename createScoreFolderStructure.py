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
            
