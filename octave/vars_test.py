from oct2py import octave

[x, y, z, class_o] = octave.vars(123.33, 'this')
print x, y, z, class_o
