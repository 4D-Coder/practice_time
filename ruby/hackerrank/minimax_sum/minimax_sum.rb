def miniMaxSum(arr)
  counter = 0
  sums = []

  while counter < arr.size
    exclude = arr.delete_at(counter)
    sums.push(arr.sum)
    arr.unshift(exclude)
    counter += 1
  end

  puts "#{sums.min} #{sums.max}"
end


arr = [3, 4, 7, 10, 5]

miniMaxSum(arr)
