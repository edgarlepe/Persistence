import numpy as np

def subject_labels_in_range(start, stop):
    """Returns a list of labels for subjects in the subject column.

    :param start: integer between 2 and 57, inclusive
    :param stop: integer between 2 and 57, inclusive. Should be greater than or
                 equal to start.
    :returns: list of zero-padded subject labels beginning with s{start} to s{stop}
    """
    return [f's{i:03}' for i in range(start, 1 + stop) if i not in [6, 9, 14, 23, 45]]

def persistence_in_dimension(persistence, dimension):
    """Returns the persitence intervals of simplicial complex in a specific
    dimension.

    :param persistence: persistence of the simplex tree.
    :param dimension: specific dimension.
    :returns: 2 dimensional numpy array of birth and death pairs in the
              specified dimension.
    """
    specified_dim = filter(lambda x: x[0] == dimension, persistence)
    specified_dim_pairs = map(lambda x: x[1], specified_dim)
    return np.asarray(list(specified_dim_pairs), dtype=np.float64)