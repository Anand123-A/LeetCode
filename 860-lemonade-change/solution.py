// 3 ms | 23.5 MB
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        count_five = 0
        count_ten = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                count_five = count_five +1
            elif bills[i] == 10:
                count_ten = count_ten +1
                if count_five > 0:
                    count_five = count_five -1
                else:
                    return False
            else:
                if count_five > 0 and count_ten > 0:
                    count_five = count_five - 1
                    count_ten = count_ten - 1
                elif count_five >= 3:
                    count_five = count_five -3
                else:
                    return False
        return True

                 
        