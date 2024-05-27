
def main():
    with open('tiny.tortoise', 'r') as tiny_tortoise:
        tortoise_program = tiny_tortoise.readlines()
        for line in tortoise_program:
            print(line.strip())

if __name__ == '__main__':
    main()