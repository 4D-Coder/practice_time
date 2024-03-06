def longest_common_prefix(strs)
  prefix = []
  # unique_value = prefix.uniq.count
  # prefix => ["f", "f", "f"]
  # .uniq => ["f"]
  # .count => 1
  i = 0
  if prefix.uniq.count <= 1
    strs.each do |str|
      prefix.push(str[i])
    end
    i += 1
  end
  prefix.uniq.count > 1 ? "" : prefix.join
end

strs = ["flower","flow","flight"]
p longest_common_prefix(strs)

strs = ["dog","car", "rat"]
p longest_common_prefix(strs)

#   prefix = ""
#   c = 0
#   while c
#       strs.each do |str|
#           str_prefix = str[0..c]
#           if str[0..c] != str_prefix
#               break
#               c = nil
#           end
#           prefix = str_prefix unless prefix.include?(str_prefix)
#       end
#       c += 1
#   end
#   prefix

# Shift to methods you know
