tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printtabel():
    a = 0 

    for x in range(len(tableData)):
        for y in tableData[x]:
            b = len(y)
            if b > a:
                a = b
            else:
                a = a
                
    for x in range(len(tableData[x])):
        print(f"{tableData[0][x].rjust(a)}  {tableData[1][x].rjust(a)}  {tableData[2][x].rjust(a)}")

printtabel()