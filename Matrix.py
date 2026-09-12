

class Matrix :
    precision = 3
    spacing = 3
    def __init__(self, theList):
        assert Matrix.isMatrix(theList), "Invalid list for creating matrix"
        self.value = theList
        self.rows = len(theList)
        self.cols = len(theList)

    def printm():
        pass
    
    @staticmethod
    def isMatrix(theList):
        row_len = len(theList[0])
        for row in theList:
            if len(row) != row_len :
                return False
            for i in row:
                if not isinstance(i, int) and not isinstance(i, float):
                    return False
        return True


A = Matrix([[1, 2], [3, 4]])
print(A.rows, A.cols)