def longest_common_prefix(strs)
  return "" if strs.empty?

  prefix = ""
  first_str = strs.first

  first_str.each_char.with_index do |char, index|
    if strs.all? { |str| str[index] == char }
      prefix.concat(char)
    else
      break
    end
  end

  prefix
end

strs = ["flower","flow","flight"]
p longest_common_prefix(strs)

strs = ["dog","racecar","car"]
p longest_common_prefix(strs)
