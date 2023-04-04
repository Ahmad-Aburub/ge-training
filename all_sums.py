#Enter Python code here and hit the Run button.
def get_comb(num_list, i = 0, comb_list = str(), sum = 0, ans = []):
    if i == (len(num_list)):
        ans.append([int(x) for x in comb_list.strip().split()])
        return ans
    get_comb(num_list, i + 1, comb_list +f' {str(num_list[i])}', sum + num_list[i], ans)
    get_comb(num_list, i + 1, comb_list, sum, ans)
    return ans
    
nums = [int(x) for x in input().split()]
print(nums)
all_combs = get_comb(nums)
print(all_combs)
sum_list = {sum(comb) for comb in all_combs if comb}
print(sum_list)
