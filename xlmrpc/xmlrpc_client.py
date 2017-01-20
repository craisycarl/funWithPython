import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:2500")
print server

print server.system.listMethods()

# multi = xmlrpclib.MultiCall(server)
# multi.pow(2, 9)
# multi.add(5, 1)
# multi.add(24, 11)
# try:
#     for response in multi():
#         print response
# except xmlrpclib.Error, v:
#     print "ERROR", v