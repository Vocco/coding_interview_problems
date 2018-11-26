"""
Coding interview problem: K-th last element of a singly linked list

Given a singly linked list and an integer 'k', remove the 'k'-th last element
from the list.

Making more than one pass is prohibitively expensive, as the list is extremely
long. Achieve the goal in constant space and in one pass.

Note
----
There are two supporting classes in this module:

    SinglyLinkedNode
    SinglyLinkedList

The solution algorithm is the function find_kth_last.

Examples
--------
    >>> import kth_last_element_linked_list as klell
    >>> linked_list = klell.SinglyLinkedList([5, 4, 6, 8])
    >>> klell.find_kth_last(linked_list, 1).val
    8
    >>> klell.find_kth_last(linked_list, 2).val
    6
    >>> klell.find_kth_last(linked_list, 4).val
    5
"""


class SinglyLinkedNode:
    """
    A node in a singly linked list.

    Attributes
    ----------
    next
        The next node in the singly linked list. If no next node exists, this
        should be None.
    val
        The value of this node.
    """

    def __init__(self, val: 'any'):
        """
        Initializes a new SinglyLinkedNode.

        The new node has the given value and its successor is None.
        """
        self.val = val
        self.next = None


class SinglyLinkedList:
    """
    A singly linked list.

    Attributes
    ----------
    first: SinglyLinkedNode
        The first singly linked node in the sequence.
    """

    def __init__(self, sequence: 'sequence'):
        """
        Generates a new SinglyLinkedList from a sequence.

        The newly created list contains all the elements of the original
        sequence wrapped in SinglyLinkedNode objects.

        Parameters
        ----------
        sequence
            The sequence of items to create a singly linked list from.
        """
        iterator = iter(sequence)

        try:
            self.first = SinglyLinkedNode(next(iterator))
        except StopIteration:
            self.first = None
            return

        cur_node = self.first

        while True:
            try:
                cur_node.next = SinglyLinkedNode(next(iterator))
                cur_node = cur_node.next
            except StopIteration:
                return


def find_kth_last(sll: SinglyLinkedList, k: int) -> SinglyLinkedNode:
    """
    Retrieves the k-th last element from a SinglyLinkedList in one pass.

    To find the last element in the list, use k = 1. Use k = 2 to find the
    second-to-last element, etc.

    Parameters
    ----------
    k
        The distance between the desired element and the end of the list.
    sll
        The list to search through.

    Returns
    -------
    SinglyLinkedNode
        The node on the k-th last position in the singly linked list, or None
        if the given position does not exist in the singly linked list.

    Raises
    ------
    TypeError
        If k is not an integer or sll is not a SinglyLinkedList.
    """
    if not k >= 1:
        return None

    # Part 1
    # Start the 'vanguard' index - this index is k positions to the right of
    # the value we will actually return.
    try:
        vanguard = sll.first
    except AttributeError:
        raise TypeError('sll must be a SinglyLinkedList')

    for i in range(k - 1):
        try:
            vanguard = vanguard.next
        except AttributeError:
            # Encountered the end of the list sooner than expected - k is
            # larger than the number of elements in sll, nothing to return.
            return None

    # As before, an edge case where k is the number of elements in sll + 1.
    if vanguard is None:
        return None

    # Part 2
    # Move the 'vanguard' index to the end, but look at the value that's k
    # positions to the left of it - this will be the k-th last element when
    # vanguard arrives to the end.
    value = sll.first    
    while vanguard.next is not None:
        vanguard = vanguard.next
        value = value.next

    return value
