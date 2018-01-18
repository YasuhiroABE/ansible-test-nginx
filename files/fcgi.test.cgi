#!/usr/bin/ruby

require 'fcgi'

FCGI.each { |request|
  out = request.out
  out.print "Content-Type: text/plain\r\n\r\n"

  out.print "request.env:\r\n"
  for k in request.env.keys
    out.print k + ": " + request.env[k] + "\r\n"
  end

  request.finish
}
