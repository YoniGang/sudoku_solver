# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:03:30 2020

@author: yonig
"""

grid = [
     [7,8,0,4,0,0,1,2,0],
     [6,0,0,0,7,5,0,0,9],
     [0,0,0,6,0,1,0,7,8],
     [0,0,7,0,4,0,2,6,0],
     [0,0,1,0,5,0,9,3,0],
     [9,0,4,0,6,0,0,0,5],
     [0,7,0,3,0,0,0,1,2],
     [1,2,0,0,0,7,4,0,0],
     [0,4,9,2,0,6,0,0,7]
 ]

# =============================================================================
#                        The Cells class
# =============================================================================
class GridCell:
    def __init__(self, num, is_const, row, col, grid_ref):
        self.num = num
        self.is_const = is_const
        self.row = row
        self.col = col
        self.part = (int(row/3), int(col/3))
        self.grid_ref = grid_ref
    
    def update_num(self, new_num):
        self.num = new_num
    
    def check_row(self):
        return not self.num in self.grid_ref.get_row(self.row, self)
    
    def check_col(self):
        return not self.num in self.grid_ref.get_col(self.col, self)
    
    def check_part(self):
        return not self.num in self.grid_ref.get_part(self.part, self)
    
    def check_validity(self):
        return (self.check_part() 
                and self.check_col() 
                    and self.check_row())
    
    def __str__(self):
        return str(self.num)
    
    def __eq__(self, other):
        return (self.row == other.row and self.col == other.col) if other != None else False
    
# =============================================================================
#                        The Grid class
# =============================================================================
class Grid:
    def __init__(self, grid_list):
        self.grid_cells = self.create_cells(grid_list)
    
    # =============================================================================
    # This function gets list of lists that represent the grid, and translate
    # the list to the Grid class
    # =============================================================================
    def create_cells(self, grid_list):
        grid_cells = []
        for row, row_values in enumerate(grid_list):
            for col, num in enumerate(row_values):
                is_const = True if num != 0 else False
                cell = GridCell(num, is_const, row, col, self)
                grid_cells.append(cell)
                
        return grid_cells
    
    # =============================================================================
    # This function gets a row number, and return all the numbers in the row
    # except the cell that was calling the funtion
    # =============================================================================
    def get_row(self, row_num, except_cell = None):
        return [cell.num for cell in self.grid_cells 
                if cell.row == row_num and cell != except_cell]
    
    # =============================================================================
    # This function gets a col number, and return all the numbers in the col
    # except the cell that was calling the funtion
    # =============================================================================
    def get_col(self, col_num, except_cell = None):
        return [cell.num for cell in self.grid_cells 
                if cell.col == col_num and cell != except_cell]
    
    # =============================================================================
    # This function gets a part tuple, and return all the numbers in the part
    # except the cell that was calling the funtion
    # =============================================================================
    def get_part(self, part, except_cell = None):
        return [cell.num for cell in self.grid_cells 
                if cell.part == part and cell != except_cell]
    
    # =============================================================================
    # This funtion returns all the cells indexes that are not const
    # =============================================================================
    def get_none_const_cells_indexes(self):
        return [ind for ind, cell in enumerate(self.grid_cells)
                if not cell.is_const]
    # =============================================================================
    # This funtion returns list representation of the grid
    # =============================================================================
    def list_repr(self):
        return [self.get_row(i) for i in range(9)]

    # =============================================================================
    # This funtion returns list representation of the grid
    # =============================================================================
    def json_repr(self):
        return {'r' + str(i) : self.get_row(i) for i in range(9)}
            

    # =============================================================================
    # This funtion solve the grid using backtracking algorithm
    # =============================================================================
    def solve_grid(self):
        ind_list = self.get_none_const_cells_indexes() #list of indexes of all not const cells
        i = 0
        while i < len(ind_list):
            #If we got here, that means that we tried all possible solutions
            #and we didnt manage to solve the board, because we returnd to
            #the first none const cell, it was 9 and still there was no solution.
            if i < 0:
#                return False
                 print('The Grid is not solvable. Please try anothe one')
                 break
            # print(i)
            #if we are here, it means that the cell was with the value
            #of 9, and the next cell wasnt valid so we have to get to the prev cell
            if self.grid_cells[ind_list[i]].num == 9:
                self.grid_cells[ind_list[i]].num = 0 #reset the cell
                i -= 2 #take another step back to the prev cell
            else:
                self.grid_cells[ind_list[i]].num += 1
                #check if the number is valid
                if not self.grid_cells[ind_list[i]].check_validity():
                    #check if we tried all possible numbers
                    if self.grid_cells[ind_list[i]].num == 9:
                        self.grid_cells[ind_list[i]].num = 0 #reset the cell
                        i -= 1 #take another step back to the prev cell
                    i -= 1 #take a step back to get to current cell after i + 1
            i += 1 #continue to the next cell (if the current cell is valid)
        return True
            
    # =============================================================================
    # String repr
    # =============================================================================
    def __str__(self):

        final_string = '―――'*9 + '―' + '\n'
        prev_row = 0
        prev_part = (0,0)
        final_string += '| '
        for cell in self.grid_cells:
            if cell.part[0] != prev_part[0]:
                final_string = final_string[:-1]
                final_string += '|'
                final_string += '\n'
                final_string += '―――'*9 + '――'
                prev_part = cell.part
                
            if cell.part[1] != prev_part[1]:
                final_string = final_string[:-1]
                final_string += '|'
                prev_part = cell.part
                
        
            
            if cell.row != prev_row:
                final_string = final_string[:-1]
                final_string += '|'
                final_string += '\n'
                final_string += '| '
                prev_row = cell.row
                # prev_part = (int(cell.row/3), 0)
           
            
            final_string += str(cell) + '  '

        final_string = final_string[:-1] + '|' + '\n'
        final_string += '―――'*9 + '―'
        
        return final_string
        
        
        
if __name__ == '__main__':   
     g = Grid(grid)
     print(g)
     g.solve_grid()
     print(g)
#     l = g.list_repr()