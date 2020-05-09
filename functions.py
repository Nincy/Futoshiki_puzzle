"""
This is the file containing all the functions for the internal processing to validate the solutions
This file is imported in the home.py and testing.py file.
It consists of the following functions :-
1. row_check(solution) - to check for duplicate values in the rows.
2. column_check(solution)- to check for duplicate values in the columns.
3. constraint_check(solution) - to check for the custom constraints(as described in home.py).
4. validate_solution(board,solution) - to validate the proposed 4X4 solutions after assigning them to the empty board.
                                    Its function definition involves invoking all the above mentioned functions and returns the appropriate result.
                                    It is further invoked in the home.py and testing.py file.
"""



# List with the row and column names
intervals=['s1','s2','s3']



# FUNCTIONS
def row_check(solution):
    """ Function to check if row contains duplicate values. 
    It takes the proposed solution as argument."""

    result=True
    for ind in range(len(solution.index)):        
        
        if (solution.iloc[ind].name in intervals): #Ignore/skip if the row name exists in the intervals list
            continue
        
        else:
            bool_series = solution.iloc[ind].duplicated() #Generates a boolean series which has True if there is a duplicate value in the row
            for series_index in bool_series.index:
                
                if (series_index in intervals): #Ignore/skip if the series' index exists in the intervals list
                    continue
                
                else:
                    if bool_series[series_index]==True:
                        print(f'Duplicate value in row : {solution.iloc[ind].name} in the proposed solution.')                  
                        result=False
                        return result
                        
    return result





def column_check(solution):
    """ Function to check if column contains duplicate values
    It takes the proposed solution as argument."""
    
    result=True
    for col in solution.columns:
        
        if (col in intervals):  #Ignore/skip if the column name exists in the intervals list
            continue
        
        else:
            bool_series = solution[col].duplicated()  #Generates a boolean series which has True if there is a duplicate value in the column.
            for dup_col in bool_series.index:
                
                if (dup_col in intervals): #Ignore/skip if the series' index exists in the intervals list
                    continue
                
                else:
                    if bool_series[dup_col]==True:
                        print(f'Duplicate value in column : {col} in the proposed solution.')                  
                        result=False
                        return result
    
    return result




def constraint_check(solution):
    """ Function to check if the constraints given in the empty board are satisfied or not :-
        --> value in (A,A)>(A,B)
        --> value in (B,C)>(C,C)
        --> value in (C,B)<(D,B)
        --> value in (D,A)>(D,B)
        It takes the proposed solution as argument.
    """ 
    result=True
    for ind in range(len(solution.index)):
        for col in range(len(solution.columns)):
            
            if(solution.iat[ind,col]=='>'):  #If the cell contains > sign,then perform the comparison operation and return the appropriate result
                if (solution.iat[ind,col-1])>(solution.iat[ind,col+1]):
                    result=True
                else:
                    col_name=col-1
                    print(f"Constraint issue in cell {solution.iloc[ind].name,solution.columns[col_name]} in the proposed solution.")
                    result=False
                    return result 
            
            elif(solution.iat[ind,col]=='v'):  #If the cell contains v sign,then perform the comparison operation and return the appropriate result
                if (solution.iat[ind-1,col])>(solution.iat[ind+1,col]):
                    result=True
                else:
                    index_name=ind-1
                    print(f"Constraint issue in cell {solution.iloc[index_name].name,solution.columns[col]} in the proposed solution.")
                    result=False
                    return result
            
            elif(solution.iat[ind,col]=='^'):  #If the cell contains ^ sign,then perform the comparison operation and return the appropriate result
                if (solution.iat[ind+1,col])>(solution.iat[ind-1,col]):
                    result=True
                else:
                    index_name=ind-1
                    print(f"Constraint issue in cell {solution.iloc[index_name].name,solution.columns[col]} in the proposed solution.")
                    result=False
                    return result                   

            elif(solution.iat[ind,col]=='<'):  #If the cell contains < sign,then perform the comparison operation and return the appropriate result
                if (solution.iat[ind,col-1])<(solution.iat[ind,col+1]):
                    result=True
                else:
                    col_name=col-1
                    print(f"Constraint issue in cell {solution.iloc[ind].name,solution.columns[col_name]} in the proposed solution.")
                    result=False
                    return result                   

            else:
                result=True

    return result






def validate_solution(board,solution):
    """ Function containing the solution validator
        It takes the proposed solution and assigns it to the pre-existing empty board with the constraints, and then validates the solution.
        It invokes all the above defined functions and returns the final result to the home.py file or the testing.py file, accordingly.
        Its arguments are the empty board and the proposed solution.
    """   

    result=True
    for ind in range(len(board.index)):
        for col in board.columns:
            index_name=board.iloc[ind].name    
            
            if (col not in intervals) and (index_name not in intervals):  #Get the cells whose rows and columns are not present in the intervals list
                #Assign the 4x4 proposed solution to the empty board created and validate the solution.
                board.at[index_name,col]=solution.at[index_name,col]               
            
            else:  
                continue

    if row_check(board)==False: 
        result=False
    elif column_check(board)==False:
        result=False 
    elif constraint_check(board)==False:
        result=False 
    else:
        print('This proposed solution is correct for the given futoshiki puzzle.')
        result=True
    
    return result

