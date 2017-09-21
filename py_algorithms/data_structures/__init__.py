from typing import Any
from typing import Callable
from typing import List
from typing import TypeVar

from .deque import Deque
from .doubly_linked_list_deque import DoublyLinkedListDeque
from .heap import Heap
from .max_heap import MaxHeap
from .min_heap import MinHeap
from .priority_queue import PriorityQueue
from .queue import Queue
from .stack import Stack

T = TypeVar('T')

__all__ = [
    'new_deque',
    'Deque',
    'new_queue',
    'Queue']


def new_deque(collection: List[Any] = ()) -> Deque:
    return DoublyLinkedListDeque(collection)


def new_queue(collection: List[T] = ()) -> Queue[T]:
    return Queue[T](collection)


def new_stack(collection: List[T] = ()) -> Queue[T]:
    return Stack[T](collection)


def new_heap(comparator_f2: Callable[[Any, Any], bool], xs: List[Any] = ()) -> Heap:
    """
    Factory method to construct generic heap
    :param comparator_f2: a morphism to apply in order to compare heap entries
    :param List[T] xs: a list of initial isomorphic values to populate heap
    :return: pointer to Heap interface

    Example of a generic Max heap

    >>> max_heap = new_heap(lambda x, y: (x > y) - (x < y) == 1)
    >>> max_heap.push('Kelly', 1)
    >>> max_heap.push('Ryan', 7)
    >>> max_heap.next_key #=> 'Ryan'
    >>> max_heap.pop()    #=> 7

    """
    return Heap(comparator_f2, xs)


def new_max_heap(xs: List[Any] = ()) -> Heap:
    """
        MAX Heap constructor. https://en.wikipedia.org/wiki/Min-max_heap
        @see #new_heap

    :param xs: optional collection of initial values
    :return: an interface to Heap
    """
    return MaxHeap(xs)


def new_min_heap(xs: List[Any] = ()) -> Heap:
    """
        MIN Heap constructor. https://en.wikipedia.org/wiki/Min-max_heap
        @see #new_heap

    :param xs: optional collection of initial values
    :return: an interface to Heap
    """
    return MinHeap(xs)


def new_priority_queue(queue_vector_f2: Callable[[Any, Any], bool]) -> PriorityQueue:
    """
        >>> from py_algorithms.data_structures import new_priority_queue
        >>>
        >>> pq = new_priority_queue(lambda x, y: (x > y) - (x < y) == 1)
        >>> pq.push('Important', 10)
        >>> pq.push('Not So Important', -2)
        >>> pq.pop() #=> 'Important'

    :param queue_vector_f2: a functor defining queue order
    :return: a PriorityQueue interface
    """
    return PriorityQueue(queue_vector_f2)
