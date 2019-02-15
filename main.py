from timeit import default_timer


# ===========================================================
# PROBLEM 16 -- Power Digit Sum
# ===========================================================
#
#  2^15 = 32768 and the sum of its digits is:
#
#       3 + 2 + 7 + 6 + 8 = 26
#
#  What is the sum of the digits of the number 2^1000
#
# ===========================================================
def problem_16( ):
    # Print Problem Context
    print( "Project Euler Problem 16 -- Power Digit Sum" )

    # Compute Result and Execution Time
    start_time      =  default_timer( )
    result          =  sum( [ int( c ) for c in str( 2**1000 ) ] )
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   The sum of all digits in the number 2^1000:   %d"      %  result )
    print( "   Computation Time:                             %.3fms"  % execution_time )
    return



if __name__ == '__main__':
    problem_16( )