from intersection import Intersection
from board_graphics import BoardGraphics
import math
from itertools import product


class Intersections:
    def __init__(self, LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE):
        self.center_position_list = []
        self.range_position_dic = {}
        self.eur_dis_dic = {}
        self.get_intersections_center(LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE)

    def get_intersections_center(self, LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE):
        board = BoardGraphics(LINE_X, LINE_Y, WINDOW_WIDTH, LINE_DIS, BOARD_SIZE)
        ls = []
        for i in range(board.size + 1):
            ls.append(board.line_x)
            board.line_x += board.line_dis
        self.center_position_list = list(product(ls, ls))
        
        return self.center_position_list

    def get_intersections_range(self, INTERSECTION_PERCISE):
        intersection = Intersection(INTERSECTION_PERCISE)

        for x, y in self.center_position_list:
            range_tuple = intersection.range_update(x, y)
            self.range_position_dic[(x, y)] = range_tuple
        return self.range_position_dic

    def is_around_intersections(self, mousex, mousey, INTERSECTION_PERCISE):
        inter_x, inter_y = self.find_nearest_intersections(mousex, mousey, INTERSECTION_PERCISE)
        xleft, xright, ytop, ybottom = self.range_position_dic.get((inter_x, inter_y))
        if (xleft < mousex < xright) and (ytop < mousey < ybottom):
            return True
        else:
            return False
        
    def find_nearest_intersections(self, mousex, mousey, INTERSECTION_PERCISE):
        self.get_intersections_range(INTERSECTION_PERCISE)
        for x, y in self.center_position_list:
            self.eur_dis_dic[(x, y)] = math.sqrt((x - mousex) ** 2 + (y - mousey) ** 2)

        center_xy = min(self.eur_dis_dic, key=lambda k: self.eur_dis_dic[k])

        inter_x, inter_y = center_xy
        return inter_x, inter_y
