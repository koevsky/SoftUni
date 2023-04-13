def get_primes(nums_list):

    def prime_check(num):
        if num > 1:
            for x in range(num-1, 1, -1):
                if num % x == 0:
                    return False

            return True

        return False

    for num in nums_list:
        if prime_check(num):
            yield num
