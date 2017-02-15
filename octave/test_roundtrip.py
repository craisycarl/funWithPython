from oct2py import octave
import numpy as np
import pprint


x = np.array([[1, 2], [3, 4]], dtype=float)
out, o_class = octave.roundtrip(x)

pprint.pprint([x, x.dtype, out, o_class, out.dtype])
