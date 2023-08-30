def plusMinus(arr)
  numerators = Hash[
    :neg => [],
    :pos => [],
    :zero => [],
  ]
  denom = arr.count
  arr.each do |i|
    case
      i <=> 0
    when -1
      numerators[:neg].push(i)
    when 1
      numerators[:pos].push(i)
    when 0
      numerators[:zero].push(i)
    end
  end

  puts (numerators[:pos].count.to_f / denom.to_f).truncate(6)
  puts (numerators[:neg].count.to_f / denom.to_f).truncate(6)
  puts (numerators[:zero].count.to_f / denom.to_f).truncate(6)
end

arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
# =>
# 0.5
# 0.333333
# 0.166666
