import abc

class SortingAlgorithm(abc.ABC):

    @abc.abstractmethod
    def sort(self, arr: list)-> list:
        pass