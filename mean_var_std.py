import numpy as np

def calculate(list):
    
    # for incomplete list
    if (len(list) < 9):
        raise ValueError('List must contain nine numbers.')
        
    # make an array 
    work_array = np.array(list, ).reshape(3,3)
    print(work_array)
    

    
    mean_1 = work_array.mean(axis = 1).tolist()
    mean_0 = work_array.mean(axis = 0).tolist()
    mean_flat = work_array.mean().tolist()

   
    
    var_1 = work_array.var(axis = 1).tolist()
    var_0 = work_array.var(axis = 0).tolist()
    var_flat = work_array.var().tolist()
    
    std_1 = work_array.std(axis = 1).tolist()
    std_0 = work_array.std(axis = 0).tolist()
    std_flat = work_array.std().tolist()
    
    max_1 = work_array.max(axis = 1).tolist()
    max_0 = work_array.max(axis = 0).tolist()
    max_flat = work_array.max().tolist()
    
    min_1 = work_array.min(axis = 1).tolist()
    min_0 = work_array.min(axis = 0).tolist()
    min_flat = work_array.min().tolist()
    
    sum_1 = work_array.sum(axis = 1).tolist()
    sum_0 = work_array.sum(axis = 0).tolist()
    sum_flat = work_array.sum().tolist()
    
    
    calculations = {'mean' : [mean_0, mean_1, mean_flat],
                    'variance' : [var_0, var_1, var_flat],
                    'standard deviation' : [std_0, std_1, std_flat],
                    'max' : [max_0, max_1, max_flat],
                    'min' : [min_0, min_1, min_flat],
                    'sum' : [sum_0, sum_1, sum_flat]}
    return calculations