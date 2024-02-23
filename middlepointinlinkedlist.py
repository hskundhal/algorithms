from os import link
import linkedlists
def findmiddlelinkedlist( linkedlist) :
    slow_guy = linkedlist.head
    fast_guy = linkedlist.head
    while fast_guy.next and fast_guy.next.next:
        
        fast_guy = fast_guy.next.next
        slow_guy = slow_guy.next
    return slow_guy

my_linked_list = linkedlists.LinkedList(2)
my_linked_list.append(1)
my_linked_list.append(12)
my_linked_list.append(13)
my_linked_list.append(14)
my_linked_list.append(15)
my_linked_list.print_list()
print(findmiddlelinkedlist(my_linked_list).value)

