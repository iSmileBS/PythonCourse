import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF

survey = pd.read_csv('immSurvey.csv')
survey.head()

alphas = survey.stanMeansNewSysPooled
sample = survey.textToSend

vec = CountVectorizer()
X = vec.fit_transform(sample)

pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
vec = TfidfVectorizer()
X = vec.fit_transform(sample)
pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas,
random_state=1)

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)
gpr.fit(Xtrain.toarray(), ytrain)

mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

ModelTry1 = np.corrcoef(ytest, mu_s)
print(ModelTry1)

bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)

Xnew = bigram_vectorizer.fit_transform(sample)

Xnewtrain, Xnewtest, ynewtrain, ynewtest = train_test_split(Xnew, alphas,
random_state=1)

rbfnew = ConstantKernel(1.0) * RBF(length_scale=1.0)
gprnew = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gprnew.fit(Xnewtrain.toarray(), ynewtrain)
    
mu_snew, cov_snew = gprnew.predict(Xnewtest.toarray(), return_cov=True)

ModelTry2 = np.corrcoef(ynewtest, mu_snew)
print(ModelTry2)

Improvement = float(str(round(((ModelTry2/ModelTry1)[1,0]-1)*100,2)))
if Improvement > 0 :
    print ("The improvement from first model to second model is " +str(round(((ModelTry2/ModelTry1)[1,0]-1)*100,2)) +" % ")
else :
    print ("The regression from first model to second model is " +str(round(((ModelTry2/ModelTry1)[1,0]-1)*100,2)) +" % ")
    
# Several ngram_range value combinations were tested and (1,2) seems to yield the best result #