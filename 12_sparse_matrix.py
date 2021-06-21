"""
CS3C, Assignment #2, Sparse Matrices
Ulises Marian
"""
from linkedlist import *

class MatrixEntry:
    def __init__(self, col, val):
        self._col = col
        self._value = val

    def __str__(self):
        return f"{str(self._value)}"

    @property
    def col(self):
        return self._col

    @property
    def value(self):
        return self._value

    def __lt__(self, other):
        return self._value < other

    def __gt__(self, other):
        return self._value > other

    def __eq__(self, other):
        return self._value == other

class SparseMatrix:
    def __init__(self, nrows, ncols, default_value):
        self.nrows = nrows
        self.ncols = ncols
        self.default_value = default_value
        self._rows = LinkedList()
        for num in range(nrows):
            self._rows.add_to_head(OrderedLinkedList())

    def clear(self):
        for row in self._rows:
            for cell in row:
                try:
                    i = row.__iter__()  #returns node. iterate over whole list
                    row.remove(i.__next__())
                except StopIteration:
                    pass

    def get(self, row, col):
        if type(row) is not int or row < 0 or row > self.nrows-1:
            raise IndexError
        if type(col) is not int or col < 0 or col > self.ncols-1:
            raise IndexError
        for i in range(self._rows[row].size):
            entry = self._rows[row].__getitem__(i)
            if entry.col == col:
                return entry.value
        return self.default_value

    def set(self, row, col, value):
        if type(row) is not int or row < 0 or row > self.nrows-1:
            raise IndexError
        if type(col) is not int or col < 0 or col > self.ncols-1:
            raise IndexError
        if value == self.default_value:
             result = self.get(row, col)
             if result != value:
                 entry = MatrixEntry(col, result)
                 self._rows[row].remove(entry)
             else:
                 return
        result = self.get(row, col)
        if result != self.default_value:
            entry = MatrixEntry(col, result)
            self._rows[row].remove(entry)
            entry = MatrixEntry(col, value)
            self._rows[row].add(entry)

        entry = MatrixEntry(col, value)
        self._rows[row].add(entry)

    def get_row(self, row):
        if row < 0 or row > self.nrows - 1:
            raise IndexError
        else:
           return self.if_row_gen(row)

    def if_row_gen(self, row):
        for cell in self._rows[row]:
            yield cell.value

    def get_col(self, col):
        if col < 0 or col > self.ncols - 1:
            raise IndexError
        else:
            return self.if_col_gen(col)

    def if_col_gen(self, col):
        for row in self._rows:
            for entry in row:
                if entry.col == col:
                    yield entry.value


    def __str__(self, starting_row=0, starting_col=0, nrows=None,
                ncols=None):
        row_start = starting_row
        col_start = starting_col
        if nrows is None:
            nrows = self.nrows
        if ncols is None:
            ncols = self.ncols
        row_end = min(self.nrows, starting_row + nrows)
        col_end = min(self.ncols, starting_col + ncols)

        s = ""
        for r in range(row_start, row_end):
            if self._rows[r] == 0:
                s += (str(self.default_value) + " ") * ncols
            else:
                for c in range(col_start, col_end):
                    s += str(self.get(r, c)) + " "

            s += "\n"
        return s

        # s = ""
        # for i, row in enumerate(self._rows):
        #     if len(row) == 0:
        #         s += (str(self.default_value) + " ") * self.ncols
        #         #s += self.get(row, i)
        #     else:
        #          #if len(row) > 1:
        #          for j in range(self.ncols):
        #          #for e, cell in enumerate(self.ncols):
        #              s += str(self.get(i, j)) + " "
        #     s += "\n"
        # return s


def main():
    matrix = SparseMatrix(6, 6, 0)
    matrix.set(2, 2, 20)
    matrix.set(3, 3, 4)
    print(matrix)
    matrix.set(3, 3, 8)
    matrix.set(2, 2, 3)
    print(matrix)
    matrix.set(3, 3, 2)
    print(matrix)


if __name__ == '__main__':
    main()
