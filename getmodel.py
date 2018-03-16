import numpy as np
from sklearn.ensemble import RandomForestClas
from sklearn.externals import joblib
from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import SGDClassifier

def main():

    jumbomani0 = np.load("Modelos/jumbomani/featuresjumbomani0.npy")
    jet0 = np.load("Modelos/jet/featuresjet0.npy")
    chocorramo0 = np.load("Modelos/chocorramo/featureschocorramo0.npy")
    frunasamarillo0 = np.load("Modelos/frunasamarillo/featuresfrunasamarillo0.npy")
    frunasnaranjado0 = np.load("Modelos/frunasnaranjado/featuresfrunasnaranjado0.npy")
    frunasrojo0 = np.load("Modelos/frunasrojo/featuresfrunasrojo0.npy")
    frunasverde0 = np.load("Modelos/frunasverde/featuresfrunasverde0.npy")
    jumboflowblanca0 = np.load("Modelos/jumboflowblanca/featuresjumboflowblanca0.npy")
    jumbomix0 = np.load("Modelos/jumbomix/featuresjumbomix0.npy")

    jumbomani1 = np.load("Modelos/jumbomani/featuresjumbomani1.npy")
    jet1 = np.load("Modelos/jet/featuresjet1.npy")
    chocorramo1 = np.load("Modelos/chocorramo/featureschocorramo1.npy")
    frunasamarillo1 = np.load("Modelos/frunasamarillo/featuresfrunasamarillo1.npy")
    frunasnaranjado1 = np.load("Modelos/frunasnaranjado/featuresfrunasnaranjado1.npy")
    frunasrojo1 = np.load("Modelos/frunasrojo/featuresfrunasrojo1.npy")
    frunasverde1 = np.load("Modelos/frunasverde/featuresfrunasverde1.npy")
    jumboflowblanca1 = np.load("Modelos/jumboflowblanca/featuresjumboflowblanca1.npy")
    jumbomix1 = np.load("Modelos/jumbomix/featuresjumbomix1.npy")

    jumbomani2 = np.load("Modelos/jumbomani/featuresjumbomani2.npy")
    jet2 = np.load("Modelos/jet/featuresjet2.npy")
    chocorramo2 = np.load("Modelos/chocorramo/featureschocorramo2.npy")
    frunasamarillo2 = np.load("Modelos/frunasamarillo/featuresfrunasamarillo2.npy")
    frunasnaranjado2 = np.load("Modelos/frunasnaranjado/featuresfrunasnaranjado2.npy")
    frunasrojo2 = np.load("Modelos/frunasrojo/featuresfrunasrojo2.npy")
    frunasverde2 = np.load("Modelos/frunasverde/featuresfrunasverde2.npy")
    jumboflowblanca2 = np.load("Modelos/jumboflowblanca/featuresjumboflowblanca2.npy")
    jumbomix2 = np.load("Modelos/jumbomix/featuresjumbomix0.npy")

    X = [frunasverde0, jumbomani0, jet0, chocorramo0, frunasamarillo0, frunasnaranjado0, frunasrojo0, jumboflowblanca0,jumbomix0]

    Y = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    clf = SGDClassifier(loss='hinge')
    clf.fit(X,Y)
    joblib.dump(clf, 'finalfantasy1.pkl')


if __name__ == '__main__':
	main()
