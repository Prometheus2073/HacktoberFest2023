def stooge_sort(array, left, right):
  if left >= right:
    return

  if array[left] > array[right]:
    array[left], array[right] = array[right], array[left]

  third = (right - left) // 2
  stooge_sort(array, left, right - third)
  stooge_sort(array, left + third, right)
  stooge_sort(array, left, right - third)

def main():
  array = [1, 5, 3, 2, 4]
  stooge_sort(array, 0, len(array) - 1)
  print(array)

if __name__ == "__main__":
  main()
