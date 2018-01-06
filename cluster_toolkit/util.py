"""
utility functions for the toolkit
"""
import numpy as np

def _modelswap(**kwargs):
    if kwargs is not None:
        keys = kwargs.keys()
        if not keys:
            return np.array([])
        elif 'c' in keys: #NFW profile
            model = np.array([kwargs['c']], order='C')
        elif 'rs' in keys and 'alpha' in keys: #Einasto
            model = np.array([kwargs['rs'], kwargs['alpha']], order='C')
        else:
            raise Exception("ModelError, 1-halo model with arguments %s not supported. Use either NFW with 'c' or Einasto with 'rs' and 'alpha'"%keys)
        return model
    else:
        return np.array([])
if __name__ == "__main__":
    print _modelswap()
    print _modelswap(c=5)
    print _modelswap(rs=.1, alpha=.1)
    try:
        _modelswap(eggs=12, bacon=6)
    except Exception as details:
        print "Handling wrong model:", details
