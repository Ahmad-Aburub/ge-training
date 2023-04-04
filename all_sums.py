#Enter Python code here and hit the Run button.
def get_comb(num_list, i = 0, comb_list = str(), sum = 0):
    print(type(comb_list))
    if i == (len(num_list)):
        print(comb_list)
        return comb_list
    get_comb(num_list, i + 1, comb_list +f' {str(num_list[i])}', sum + num_list[i])
    get_comb(num_list, i + 1, comb_list, sum)
    
    
    
    
nums = [int(x) for x in input().split()]
print(nums)
get_comb(nums)
