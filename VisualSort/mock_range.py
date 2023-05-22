def main() -> None:
    for i in my_range(5, 100, 2):
        print(i)

range(5, 100, 2)

def my_range(*nums) -> int:
    if len(nums) == 1:
        start: int = 0
        stop = nums[0]
        step = 1
    elif len(nums) == 2:
        start = nums[0]
        stop = nums[1]
        step = 1
    elif len(nums) == 3:
        start = nums[0]
        stop = nums[1]
        step = nums[2]

    while start < stop:
        yield start
        start += step

if __name__ == '__main__':
    main()