#!/usr/bin/ruby

print "Content-Type: text/plain\r\n\r\n"

print "request.env:\r\n"

for k in ENV.keys
  print k + ": " + ENV[k] + "\r\n"
end

