"""
This is the main/home file. 
It contains the empty board with the constraints for Futoshiki puzzle.
It also takes a 4x4 proposed solution as input from the user and validates it by invoking the validate_solution(board,solution) from functions.py file
Validation is done for the given conditions :-
1. There cannot be duplicate values in a row.
2. There cannot be duplicate values in a column.
3. Pre-existing constraints given in the empty board should be satisfied- 
    --> value in (A,A)>(A,B)
    --> value in (B,C)>(C,C)
    --> value in (C,B)<(D,B)
    --> value in (D,A)>(D,B)

"""


import pandas as pd
import functions as func


#Creation of empty board with given column and index names as well as its constraints - Pandas dataframe is used for this
""" Please note : The rows s1,s2,s3 and columns s1,s2,s3 are read-only used to store the comparison operators.
The rows named A,B,C,D and columns named A,B,C,D store the values provided by the user.
"""
board = pd.DataFrame(columns=['A','s1','B','s2','C','s3','D'], index=['A','s1','B','s2','C','s3','D'])
board.loc['A'] = ['','>','','','','','']
board.loc['s1'] = ['','','','','','','']
board.loc['B'] = ['','','','','','','']
board.loc['s2'] = ['','','','','v','','']
board.loc['C'] = ['','','','','','','']
board.loc['s3'] = ['','','^','','','','']
board.loc['D'] = ['','>','','','','','']

print('\n NOTE : The rows and columns named s1,s2,s3 are read-only containing comparison operators only.')
print('The 4x4 empty Futoshiki board with its constraints : ')
print(board)




# try block starts here
try :
    """
    Get 4 inputs from the user for each row and store them in a dataframe named user_input_df
    """
    rowA_colA,rowA_colB,rowA_colC,rowA_colD=(input('Please enter values between 1-4 for cells in order (A,A),(A,B),(A,C),(A,D) : ')).split()
    rowB_colA,rowB_colB,rowB_colC,rowB_colD=(input('Please enter values between 1-4 for cells in order (B,A),(B,B),(B,C),(B,D) : ')).split()
    rowC_colA,rowC_colB,rowC_colC,rowC_colD=(input('Please enter values between 1-4 for cells in order (C,A),(C,B),(C,C),(C,D) : ')).split()
    rowD_colA,rowD_colB,rowD_colC,rowD_colD=(input('Please enter values between 1-4 for cells in order (D,A),(D,B),(D,C),(D,D) : ')).split()

    user_input_df=pd.DataFrame(
        data={
            'A':[rowA_colA,rowB_colA,rowC_colA,rowD_colA],
            'B':[rowA_colB,rowB_colB,rowC_colB,rowD_colB],
            'C':[rowA_colC,rowB_colC,rowC_colC,rowD_colC],
            'D':[rowA_colD,rowB_colD,rowC_colD,rowD_colD]
        },
        index=['A','B','C','D']
    )
    print('\n Your proposed 4x4 solution looks like this :')
    print(user_input_df)



    # Invoke the validate_solution from functions.py for validating the proposed solution by the user.
    print('\n Validating solution provided by user : ')
    func.validate_solution(board,user_input_df)
#try block ends here



except Exception as arg:
    #Print exception, if any
    print('Please find the exception occured : ',arg)


