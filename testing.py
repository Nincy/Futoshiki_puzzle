"""
This is the test file. 
It contains the empty board with the constraints for Futoshiki puzzle.
It also has 4 proposed solutions for testing purpose, which are validated by invoking the validate_solution(board,solution) from functions.py file
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


#Creation of 4x4 empty board with given column and index names - Pandas dataframe is used for this
""" Please note : The rows s1,s2,s3 and columns s1,s2,s3 are read-only used to store the comparison operators.
The rows named A,B,C,D and columns named A,B,C,D store the values provided by the proposed solution.
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



#Proposed 4x4 Test Solutions (Pandas dataframes are used here)

#Proposed Solution 1 - Correct solution
correct_solution_df=pd.DataFrame(
    data={
        'A':[2,1,3,4],
        'B':[1,4,2,3],
        'C':[4,3,1,2],
        'D':[3,2,4,1]
    },
    index=['A','B','C','D']
)


# Proposed Solution 2 - solution with duplicate value in row
duplicate_row_df=pd.DataFrame(
    data={
        'A':[2,1,4,3],
        'B':[1,3,2,4],
        'C':[3,4,4,2],
        'D':[4,2,3,1]
    },
    index=['A','B','C','D']
)


# Proposed Solution 3 - solution with duplicate value in column
duplicate_column_df=pd.DataFrame(
    data={
        'A':[2,1,4,3],
        'B':[4,4,3,2],
        'C':[1,3,2,4], 
        'D':[3,2,1,1]
    },
    index=['A','B','C','D']
)


# Proposed Solution 4 - solution with constraint issues
constraint_issue_df=pd.DataFrame(
    data={
        'A':[2,1,4,3],
        'B':[1,3,2,4],
        'C':[3,4,1,2],
        'D':[4,2,3,1]
    },
    index=['A','B','C','D']
)



# Invoke the validate_solution from functions.py for validating all the above given proposed solutions.
print('\n Validating solution : constraint_issue_df')
func.validate_solution(board,constraint_issue_df)

print('\n Validating solution : duplicate_row_df')
func.validate_solution(board,duplicate_row_df)

print('\n Validating solution : duplicate_column_df')
func.validate_solution(board,duplicate_column_df)

print('\n Validating solution : correct_solution_df')
func.validate_solution(board,correct_solution_df)
