2# Doubling the number.
prompt: str = "Enter the Current Value:   "
def double_num():
    curr_value= input (prompt)
    curr_value= int(curr_value)

    while(curr_value <= 100):
        curr_value = curr_value * 2
        print(curr_value , end=" ")
double_num()