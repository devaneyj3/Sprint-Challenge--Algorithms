from helper import selection_sort
class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            # print(f'self.item: {self._item} > {self._list[self._position]}')
            return 1
        elif self._item < self._list[self._position]:
            # print(f"{self._item} is less than {self._list[self._position]}")
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self): 
        """
        Sort the robot's list.
        """ 
        
        """     [5,4,3,2,1] 
            1. swap the 0 item with none
            2.move right to compare_item
            held item is 5
            3. if compare item returns 1, swap
            held item is 4
                [none, 5,3,2,1]
            4. move right to compare_item
            3. if compare item returns 1, swap
            held item is 3
                [none,5,4,2,1]
            4. move right to compare_item
            3. if compare item returns 1, swap
                held item is 2
                [none,5,4,3,1]
            4. move right to compare_item
            3. if compare item returns 1, swap
            [none,5,4,3,2]
        """
        
        print(int(len(self._list) / 2))
        
    #     def merge(arrA, arrB):
    # merged_arr = arrA + arrB
    # final_arr = selection_sort(merged_arr)
    # print(f'merged_arr: {final_arr}')
    # return merged_arr




# TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr):
#     if len(arr) > 1:
#         middle = int(len(arr) / 2)
#         left_arr = arr[:middle] 
#         right_arr = arr[middle:]
#         merge_sort(left_arr)
#         merge_sort(right_arr)
#         sortedA = selection_sort(left_arr)
#         sortedB = selection_sort(right_arr)
#         arr_merge = merge(sortedA, sortedB)
#         return arr_merge
#     else:
#         return arr
        pass
        # use merge sort for big inputs
        # 1. move robot to left of right to see if there is an item
        # pick up the item at the start of the list
        # self.swap_item()
        # we go right until the end of the list
        # self.set_light_on()
        # # start by swaping the item
        # self.swap_item()
        # # go right and swap items that are greater than the current item held
        # self.go_right()
        # # move left to put item in the left position
        # self.go_left()

    def go_left(self):
        if self.move_left() == True and self.compare_item() == 1:
            # move to the furthest rightmost position
            self.move_left() 
            self.swap_item()
            # print(f'\nposition: {self._position}')
            # print(f'\nitem is now {self._item}')
            self.sort()
    def right_sort(self):
        if self.can_move_right() == False:
            return
        self.swap_item()
        self.move_right()
        if self.compare_item() == -1:
            self.swap_item()
        self.sort()
    # def left_sort(self):
    #     if self.can_move_left() == False:
    #         return
    #     self.swap_item()
    #     self.move_left()
    #     if self.compare_item() == -1:
    #         self.swap_item()
    #     self.sort()
    # def merge(arrA, arrB):
    # merged_arr = arrA + arrB
    # final_arr = selection_sort(merged_arr)
    # print(f'merged_arr: {final_arr}')
    # return merged_arr
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [5, 4, 3, 2, 1]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)