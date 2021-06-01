from titanic.views.controller import Controller
from titanic.templates.plot import Plot

if __name__ == '__main__':
    controller = Controller()
    while 1:
        m = input('0.exit 1-data visualization\n'
                  ' 2-modeling\n'
                  ' 3-machine learning\n'
                  ' 4-machine release')
        if m == '0':
            break
        elif m == '1':
            plot = Plot('train.csv')
            # plot.draw_survived_dead()
            # plot.draw_pclass()
            # plot.draw_sex()
            plot.draw_embarked()
        elif m == '2':
            df = controller.modeling('train.csv', 'test.csv')

        elif m == '3':
            pass
        elif m == '4':
            pass
        else:
            continue