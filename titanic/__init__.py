from titanic.views.controller import Controller


if __name__ == '__main__':
    controller = Controller()
    while 1:
        m = input('0.exit 1.preprocess')
        if m == '0':
            break
        elif m == '1':
            print(f'----------------  1  -----------------------')
            controller.preprocess('train.csv')
        else:
            continue