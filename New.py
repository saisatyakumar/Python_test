def find_min_platform(arr, dep):
      arr = [int(h)*60 + int(m) for time in arr for h, m in [time.split(':')]]
      dep = [int(h)*60 + int(m) for time in dep for h, m in [time.split(':')]]
      
      arr.sort()
      dep.sort()
      
      n = len(arr)
      
      platform_need = 0
      max_platform = 0
      i = 0
      j = 0
      
      while i < n and j < n:
            if arr[i] <= dep[j]:
                  platform_need += 1 
                  max_platform = max(max_platform, platform_need)
                  i += 1 
            else:
                  platform_need -= 1 
                  j += 1 
      return max_platform
      
# arr = ['9:00', '9:40', '9:50', '11:00','15:00', '18:00']
# dep = ['9:10', '12:40', '11:20', '11:30','19:00', '20:00']
arr = input().split()
dep = input().split()

print(find_min_platform(arr, dep))