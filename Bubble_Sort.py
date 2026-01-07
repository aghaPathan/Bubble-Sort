

class bubble_sort():

    def __init__(self):
        """
        This class is to perform Bubble Sort on a given List/Array
        """
        self.verified = False
        self.getSorted = []

    def _verify_array(self, list_to_sort):
        """
        This method is used for verifing either array contain invalid entries.
        """
        try:
            iter(list_to_sort)
        except TypeError as exc:
            raise ValueError("Please input a valid iterable of numerical values") from exc

        for element in list_to_sort:
            try:
                float(element)
            except (TypeError, ValueError) as exc:
                raise ValueError("Please input valid numerical values") from exc


    def sort(self, list_to_sort):
        """ This method is used to sort the given array
                """
        # Verify
        if self.verified is False:
            self._verify_array(list_to_sort)
            self.verified = True

        # Logic
        bubble = len(list_to_sort)-1
        for element in range(bubble):
            for pointer in range(bubble-element):
                if list_to_sort[pointer] > list_to_sort[pointer+1]:
                    list_to_sort[pointer], list_to_sort[pointer+1] = list_to_sort[pointer+1],list_to_sort[pointer]

        self.getSorted = list_to_sort
        return list_to_sort
