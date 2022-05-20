from MergeSort import*

def do_sort(input_file):
  
  file_address_count = dict()
  count = []
  
  data_file = open(input_file)
  for line in data_file.readlines():
    lpn = line.split()[0]
    
    if lpn not in file_address_count:
      file_address_count[lpn] = 1
    else:
      file_address_count[lpn] += 1
    
    for key in file_address_count:
      count.append(file_address_count[key])
    
    mergeSort(count, 0, len(count) - 1)
    
    count.reverse()
    
    for i in range(10):
      for key in file_address_count:
        if count[i] == file_address_count[key]:
          print(key, count[i])
          del file_address_count[key]
          break
          
do_sort("linkbench_short.trc")
