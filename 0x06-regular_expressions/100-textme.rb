#!/usr/bin/env ruby
ary = []
ary.push(ARGV[0].scan(/from:[^\]]*/).join.split(":", 2)[-1])
ary.push(ARGV[0].scan(/to:[^\]]*/).join.split(":", 2)[-1])
ary.push(ARGV[0].scan(/flags:[^\]]*/).join.split(":", 2)[-1])
puts ary.join(',')
