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
