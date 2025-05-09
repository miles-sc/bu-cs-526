import heapq

'''
 You are working for a promising new music streaming service “Algo-fy”.
 Algo-fy would like to offer a new ranking feature that will track the top k most streamed songs of the day.

 You’ve been tasked with building a class “AlgoFy” that can track the most streamed songs
 and return an accurate list top k list at any point in time.

 Another team has already developed the song streaming feature: iStream and you will need to integrate with it.
 iStream will send AlgoFy play data as it processes customer requests.
 This data will be batched so the AlgoFy class will need to ingest lists of played songs multiple times

 A song is identified with an integer id number.

 The AlgoFy class will need to have the following methods:
 - Constructor(k): the number of songs to track in the topk
 - streamSongs(List of songIds): Receive a batch of streamed songs => updates internal state
 - getTopK(): return the top k most streamed songs in order

 As an example, the AlgoFy class may see the following usage:
 ranker = new AlgoFy(2)
 ranker.streamSongs([1, 1, 2, 2, 3])
 ranker.streamSongs([3, 3, 3, 1, 2, 1, 3])
 ranker.getTopK() => [3, 1]
 ranker.streamSongs([2, 2, 2, 2, 2])
 ranker.getTopK() => [2, 3]

 You must solve this problem by effectively using the properties of a Priority Queue or Heap.

 You must also provide an explanation of the running time of both getTopK and streamSongs

Code Author: Miles Cameron

Running Time Analysis of get_top_k
--------------------
This method runs in O(N) time, where N is the number of streams in the list.
Each of the N streams needs to update its corresponding dictionary/map entry,
which is an O(1) operation.

Running Time Analysis of stream_songs
--------------------
This method runs in O(N) time.

This method has a couple parts. First I heapify the list using the bottom-up
method starting with the first internal node. As discussed in the course
materials, the run time for bottom-up construction is O(N).

Then, I remove_min k times. Remove_min takes h operations, and since this is
a complete binary tree, h=log(N). So, this process is k*log(N) or just log(N)

Since these two processes are not nested, they are just added together as
O(N+log(N)) which goes to O(N) as N gets large.
'''


class AlgoFy:
    def __init__(self, k):
        self.k = k
        # Create map/dict for recording sond frequencies
        self.stream_map={}

    def stream_songs(self, songIds):
        # Iterate over all new streams
        for id in songIds:
            # Skip any invalid inputs
            if isinstance(id,int):
                # Index existing entries in map
                if id in self.stream_map:
                    self.stream_map[id]+=1
                # Create new map entry if none exists
                else:
                    self.stream_map[id]=1

    def get_top_k(self):

        # Helper function to perform downheap bubbling
        def downheap(heap_list, i):
            # Record indicies of potential left and right childen and a
            #       max_i that will be changed as needed
            max_i=i
            left_i=(2*i)+1
            right_i=(2*i)+2

            # If the left child exists and is larger, it's the new max index
            if left_i<len(heap_list) and \
                                    heap_list[left_i][1]>heap_list[max_i][1]:
                max_i=left_i
            # If the right child exists and is larger, it's the new max index
            if right_i<len(heap_list) and \
                                    heap_list[right_i][1]>heap_list[max_i][1]:
                max_i=right_i

            # If we found a new max, swap the parent with that child
            if i!=max_i:
                temp=heap_list[i]
                heap_list[i]=heap_list[max_i]
                heap_list[max_i]=temp

            # Return new max index for use in parent function
            return max_i

        # Helper function for removing max value and re-heapifying
        def remove_max(heap_list):
            # Single node heap edge case
            if len(heap_list)==1:
                return heap_list.pop()[0]
            # Remove max and set last node as root
            max=heap_list[0]
            heap_list[0]=heap_list.pop()
            i=0
            # Perform downheap restructuring
            while True:
                new_i=downheap(heap_list,i)
                # When downheap no longer results in a change, we're done
                if i==new_i:
                    break
                i=new_i
            # Return the max value
            return max[0]

        #Beginning of main block

        # Convert map to list that we will heapify
        heap_list=list(self.stream_map.items())
        # Start downheaping with last internal index
        last_internal_index=(len(heap_list)-2)//2
        # Work up the free to the root and downheap all
        for i in range(last_internal_index,-1,-1):
            while True:
                new_i=downheap(heap_list,i)
                if i==new_i:
                    break
                i=new_i

        top_k_list=[]
        # Get and return the top k songs
        for i in range(self.k):
            if heap_list:
                top_k_list.append(remove_max(heap_list))

        return top_k_list


"""
DO NOT EDIT BELOW THIS
Below is the unit testing suite for this file.
It provides all the tests that your code must pass to get full credit.
"""


class TestAlgoFy:
    def run_unit_tests(self):
        self.test_example()
        self.test_example_2()
        self.test_many_batches()
        self.test_fewer_than_k()
        self.test_empty()
        """
        The test below will slow down your code if the runtime is inefficient.
        Save this test for last. Once you have somewhat finalized code, uncomment this
        test case and see if your code still runs quickly.
        If it runs too slowly, there's a chance the autograder on Gradescope will
        time out and not be able to grade your code within the allotted time.
        """
        self.test_very_large_k()

    def print_test_result(self, test_name, result):
        color = "\033[92m" if result else "\033[91m"
        reset = "\033[0m"
        print(f"{color}[{result}] {test_name}{reset}")

    def test_answer(self, test_name, result, expected):
        if result == expected:
            self.print_test_result(test_name, True)
        else:
            self.print_test_result(test_name, False)
            print(f"Expected: {expected} \nGot:      {result}")

    def test_example(self):
        ranker = AlgoFy(2)
        ranker.stream_songs([1, 1, 2, 2, 3])
        ranker.stream_songs([3, 3, 3, 1, 2, 1, 3])
        result = ranker.get_top_k()
        expected_answer = [3, 1]

        self.test_answer("test_example", result, expected_answer)

    def test_example_2(self):
        ranker = AlgoFy(2)
        ranker.stream_songs([1, 1, 2, 2, 3])
        ranker.stream_songs([3, 3, 3, 1, 2, 1, 3])
        ranker.get_top_k()
        ranker.stream_songs([2, 2, 2, 2, 2])

        result = ranker.get_top_k()
        expected_answer = [2, 3]

        self.test_answer("test_example_2", result, expected_answer)

    def test_many_batches(self):
        ranker = AlgoFy(5)

        for i in range(1, 10):
            for j in range(1, 15):
                ranker.stream_songs([i, j])
            ranker.get_top_k()
        ranker.stream_songs([3, 1, 1, 1, 2, 3])
        ranker.stream_songs([5, 4, 4, 3, 2, 2, 2, 1, 1])
        result = ranker.get_top_k()
        expected_answer = [1, 2, 3, 4, 5]

        self.test_answer("test_many_batches", result, expected_answer)

    def test_fewer_than_k(self):
        ranker = AlgoFy(4)

        ranker.stream_songs([1, 2, 3, 1, 2, 3, 1, 2, 1])
        result = ranker.get_top_k()
        expected_answer = [1, 2, 3]

        self.test_answer("test_fewer_than_k", result, expected_answer)

    def test_empty(self):
        ranker = AlgoFy(3)

        result = ranker.get_top_k()
        expected_answer = []

        self.test_answer("test_empty", result, expected_answer)

    def test_very_large_k(self):
        ranker = AlgoFy(1000)
        for i in range(1001):
            for j in range(100):
                for z in range(i+1):
                    ranker.stream_songs([i])

        result = ranker.get_top_k()
        expected_answer = list(range(1000,0,-1))
        self.test_answer("test_very_large_k", result, expected_answer)

if __name__ == '__main__':
    test_runner = TestAlgoFy()
    test_runner.run_unit_tests()
