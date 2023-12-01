#!/usr/bin/env ruby
arguments = ARGV.join(' ') 
  log = arguments.scan(/(?:from|to):(\+?\w+)|flags:(-\d+:\d+:?-\d+:\d+:?-?\d)/).flatten.compact
  puts log.join(',') unless log.empty?
