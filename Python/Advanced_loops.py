def board(rows,columns):
    max_rows = int(input("enter a row: "))
    max_columns = int(input("enter a column: "))
    if rows <= max_rows and columns <= max_columns:

        for i in range(rows):
            if i%2 == 0:
                for column in range(1,columns):
                     if column %2 == 1:
                        if column != columns-1:
                            print(" ",end="")
                        else:
                            print(" ")
                     else:
                         print("|",end="")
            else:
                print("-" * columns)
        return True
    else:
        print("please enter correct rows or columns")
        return  False

board(5,10)


