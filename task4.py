src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
filtered_list = [src[idx] for idx in range(len(src)) if src[idx] > src[idx - 1]]
print(filtered_list)
