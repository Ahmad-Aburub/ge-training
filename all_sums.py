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

#other
#Enter Python code here and hit the Run button
import re
A = [int(num) for num in input().split()]
sorted_A = ''.join([str(num) for num in sorted(A)])
output = re.search(r'(?<=11|22|33|44|55|66|77|88|99|00)(\d)(?=11|22|33|44|55|66|77|88|99|00)|(?<=11|22|33|44|55|66|77|88|99|00)(\d)\b|\b(\d)(?=11|22|33|44|55|66|77|88|99|00)', sorted_A)
print(output.group())

#another
#Enter Python code here and hit the Run button
N = int(input())
A = [int(num) for num in input().split()]
uniq = []
for num in A:
    if num not in uniq:
        uniq.append(num)
    else:
        uniq.remove(num)
print(str(uniq[0]))
