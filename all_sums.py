#Enter Python code here and hit the Run button.#Enter Python code here and hit the Run button.
def get_comb(num_list, i = 0, comb_list = str(), ans = []):
    if i == (len(num_list)):
        ans.append([int(x) for x in comb_list.strip().split()])
        return ans
    get_comb(num_list, i + 1, comb_list +f' {str(num_list[i])}', ans)
    get_comb(num_list, i + 1, comb_list, ans)
    return ans
    
nums = [int(x) for x in input().split()]
print(nums)
all_combs = [comb for comb in get_comb(nums) if comb]
print(all_combs)
sum_list = {sum(comb) for comb in all_combs}
print(sum_list)
