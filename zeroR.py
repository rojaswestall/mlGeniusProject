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

    diffs = []
    diffs_sqr = []
    for i in range(len(y_pred)):
        diffs.append(abs(y_pred[i] - y_true[i]))
        diffs_sqr.append(abs(y_pred[i] - y_true[i]) ** 2)
    print "Mean Error: {} votes".format(sum(diffs) / num_values)
    print "Mean Squared Error: {} votes^2".format(sum(diffs_sqr) / num_values)


if __name__ == '__main__':
    zeroR("train.csv")
