import numpy as np

def subject_labels_in_range(start: int, stop: int) -> list:
    """Returns a list of labels for subjects in the subject column.

    :param start: integer between 2 and 57, inclusive.
    :param stop: integer between 2 and 57, inclusive. Should be greater than or
                 equal to start.
    :returns: list of zero-padded subject labels beginning with s{start} to s{stop}
    """
    return [f's{i:03}' for i in range(start, 1 + stop) if i not in [6, 9, 14, 23, 45]]

def persistence_in_dimension(persistence: np.ndarray, dimension: int) -> np.ndarray:
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

class TypingDataSplit:
    """Shuffles typing data and labels and splits them into subarrays
    with matching labels.
    
    :param random_state: int or None, default=None. Controls the randomness of
                         the shuffling. Pass an int for reproducible output
                         across multiple function calls.
    :param n_splits: number of subarrays to generate.
    """
    def __init__(self, shuffle: bool=False, random_state: int=None, n_splits: int=4):
        if random_state is None:
            self.rng = np.random.default_rng()
        else:
            self.rng = np.random.default_rng(random_state)
        
        self.shuffle = shuffle
        self.n_splits = n_splits
        
    def split(self, grouped_typing_data: list, labels: list)  -> [list, list]:
        """Shuffles typing data grouped by typist and splits it into
        subarrays. Adds matching labels to subarrays.
        
        :param grouped_typing_data: list of numpy arrays, where each numpy
                                    array contains a typist's typing data.
        :param labels: list of strings where string at index i is the label for
                       the typist at index i in s{grouped_typing_data}.
        :returns: a tuple where the first element is a list of the shuffled
                  subarrays, and the second element is a list of the
                  corresponding labels.
        """
        split_data   = []
        split_labels = []
        
        for data, label in zip(grouped_typing_data, labels):
            extend_data = []
            if self.shuffle is True:
                extend_data = self.rng.permutation(data)
            else:
                extend_data = data

            split_data.extend(np.split(extend_data, self.n_splits))
            split_labels.extend([label] * self.n_splits)
        
        return (split_data, split_labels)