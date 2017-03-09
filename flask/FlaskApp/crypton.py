from werkzeug.security import generate_password_hash, check_password_hash
from timeit import default_timer as timer


pw = "JaggedShoeComputers1"

start = timer()
hashed_pw = generate_password_hash(pw, method='pbkdf2:sha256:750000')
# hashed_pw = generate_password_hash(pw, method='pbkdf2:sha1:1000')
end = timer()

print '\nhashed pw is ' + hashed_pw + ' \nthis took ' + str((end - start)*1000) + 'ms\n'

if check_password_hash(hashed_pw, pw):
    print 'match!'
else:
    print 'Not your password'
    