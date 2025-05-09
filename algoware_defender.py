"""
You are working for a new cybersecurity company “AlgoWare Defender” on a decoding tool.
The decoding tool is meant to help reverse a nefarious one way encoding scheme of letters to digits.

The encoding scheme coverts letter strings into numeric strings by
converting each letter to a digit based on its place in the alphabet.

Here is the encoding table
A : 1
B : 2
…
Z : 26

For example, the string ZAB maps to 2612.

The nefarious part of this scheme is that it is not reversible!

However, if you are given 2612 this could be decoded in multiple ways

26 1 2 = ZAB
2 6 12 = BFL
2 6 1 2 = BFAB
26 12 = ZL

AlgoWare Defender’s decoding tool will have a few components; you are working on the first piece:
determining how many decodings are possible. For example, there are 4 decodings for 2612

You must write a function: findNumDecodings
which when given a string of digits returns the number of possible decodings.

Your program must be efficient and must use dynamic programming.

You must also provide an explanation of the running time of your code

Code Author: Miles Cameron

Running Time Analysis
--------------------
find_num_decodings runs in O(N) time, where N is the length of the string.
We have a limited number of O(1) logical comparisons and assignments to run
for each character in the string. After iterating over each character this is
O(N).
"""


def find_num_decodings(string: str):

    # I SOLVED THIS FIRST USING TRADITIONAL RECUSION, WHICH WAS MORE INTUITIVE
    #   FOR ME. I THEN CONVERTED TO DP. FOR THE SAKE OF SHOWING MY WORK I HAVE
    #   INCLUDED MY ORIGINAL RECURSIVE ALGORITHM BELOW

    # def helper(string):

    #     if len(string)==0:
    #         return 1

    #     single=0
    #     double=0

    #     if int(string[0])!=0:
    #         single=helper(string[1:])

    #     if len(string)>1 and 10<=int(string[0:2])<=26:
    #         double=helper(string[2:])

    #     return single+double

    # return helper(string)

    # Make sure we don't have an empty string
    if string:

        # Initialize memoization data storage
        decodings=[0 for i in range(len(string)+1)]

        # Empty string base case
        decodings[0]=1

        # First value in string base case
        if int(string[0])!=0:
            decodings[1]=1

        # Iterate through the rest of the spots in the string
        for i in range(2,len(string)+1):

            # Prevent crashing by passing over non-numeric characters
            if string[i-1].isnumeric:

                # If the current digit can be decoded as a letter...
                if int(string[i-1])!=0:
                    # ...add the path leading up to that one letter
                    decodings[i]+=decodings[i-1]

                # If the most recent 2 digits can be decoded as a letter...
                if 10<=int(string[i-2:i])<=26:
                    # Add the path leading up to that letter
                    decodings[i]+=decodings[i-2]

        return decodings[len(string)]

    else:
        return 1






class TestFindNumDecodings:
    def run_unit_tests(self):
        self.test_example()
        self.test_empty()
        self.test_single()
        self.test_double()
        self.test_invalid_1()
        self.test_invalid_2()
        self.test_normal_1()
        self.test_normal_2()
        self.test_normal_3()
        self.test_many_ones()

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
        result = find_num_decodings("2612")
        expected_answer = 4

        self.test_answer("test_example", result, expected_answer)

    def test_empty(self):
        result = find_num_decodings("")
        expected_answer = 1

        self.test_answer("test_empty", result, expected_answer)

    def test_single(self):
        result = find_num_decodings("8")
        expected_answer = 1

        self.test_answer("test_single", result, expected_answer)

    def test_double(self):
        result = find_num_decodings("25")
        expected_answer = 2

        self.test_answer("test_double", result, expected_answer)

    def test_invalid_1(self):
        result = find_num_decodings("0")
        expected_answer = 0

        self.test_answer("test_invalid_1", result, expected_answer)

    def test_invalid_2(self):
        result = find_num_decodings("1200")
        expected_answer = 0

        self.test_answer("test_invalid_2", result, expected_answer)

    def test_normal_1(self):
        result = find_num_decodings("123456789")
        expected_answer = 3

        self.test_answer("test_normal_1", result, expected_answer)

    def test_normal_2(self):
        result = find_num_decodings("1011121314151617181920212223242526")
        expected_answer = 86528

        self.test_answer("test_normal_2", result, expected_answer)

    def test_normal_3(self):
        result = find_num_decodings("1232020410105")
        expected_answer = 3

        self.test_answer("test_normal_3", result, expected_answer)

    def test_many_ones(self):
        result = find_num_decodings("1111111111111111111111111111111111111111")
        expected_answer = 165580141

        self.test_answer("test_many_ones", result, expected_answer)


if __name__ == '__main__':
    test_runner = TestFindNumDecodings()
    test_runner.run_unit_tests()
