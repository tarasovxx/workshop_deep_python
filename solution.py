from copy import deepcopy


class FragileDict:
    def __init__(self, d: dict = None):
        if d is None:
            d = {}
        self._data = deepcopy(d)
        self._lock = True

    def __setitem__(self, key, value):
        if self._lock:
            raise RuntimeError("Protected state")
        self._temp_data[key] = value

    def __getitem__(self, key):
        if self._lock:
            return deepcopy(self._data[key])

        if key in self._temp_data:
            return self._temp_data[key]

        if key not in self._modified:
            self._modified[key] = deepcopy(self._data[key])

        return self._data[key]

    def __contains__(self, key):
        if self._lock:
            return key in self._data
        return key in self._temp_data

    def __enter__(self):
        self._lock = False
        self._temp_data = {}
        self._modified = {}
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Exception has been suppressed.")

            for key in self._data:
                if key in self._modified:
                    self._data[key] = self._modified[key]

            del self._temp_data
            del self._modified
            self._lock = True
            return True

        for key in self._data:
            if key in self._modified:
                item = self._data[key]
                self._data[key] = deepcopy(item)

        for key, value in self._temp_data.items():
            self._data[key] = deepcopy(value)

        del self._temp_data
        del self._modified
        self._lock = True



