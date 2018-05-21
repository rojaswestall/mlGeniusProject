from sklearn.metrics import zero_one_loss
import pandas as pd


def zeroR(file):
    data = pd.read_csv(file)

    print data['Total_Votes'].values
    print len(data['Total_Votes'].values)
    num_values = len(data['Total_Votes'].values)

    mean = sum(data['Total_Votes'].values) / num_values
    print mean

    y_pred = [mean] * num_values
    y_true = data['Total_Votes'].values

    print "ZeroR Accuracy%: {}".format(1 - zero_one_loss(y_true, y_pred))
    print "Correct: {}/{}".format(num_values - zero_one_loss(y_true, y_pred, normalize=False), num_values)


if __name__ == '__main__':
    zeroR("data.csv")
