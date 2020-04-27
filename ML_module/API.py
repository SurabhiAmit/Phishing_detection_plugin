import sys
import pickle
import numpy as np

#features list
def getMLScore(features,detailed=True):
    features_list = features.split(",")
    X=np.array([features_list],dtype=np.int)

    #NN_API
    file1 = open(r'.\BestModel_NN.pkl', 'rb')
    best_mlp = pickle.load(file1)
    file1.close()
    NN_val = best_mlp.predict(X)[0]
    NN_prob = max(best_mlp.predict_proba(X)[0])
    NN_unsafe_prob= best_mlp.predict_proba(X)[0][0]
    NN_safe_prob = best_mlp.predict_proba(X)[0][1]

    #SVM_API
    file1 = open(r'.\BestModel_SVM.pkl', 'rb')
    best_mlp = pickle.load(file1)
    file1.close()
    SVM_val = best_mlp.predict(X)[0]
    SVM_prob = max(best_mlp.predict_proba(X)[0])
    SVM_unsafe_prob= best_mlp.predict_proba(X)[0][0]
    SVM_safe_prob = best_mlp.predict_proba(X)[0][1]

    #DT_API
    file1 = open(r'.\BestModel_DT.pkl', 'rb')
    best_mlp = pickle.load(file1)
    file1.close()
    DT_val = best_mlp.predict(X)[0]
    DT_prob = max(best_mlp.predict_proba(X)[0])
    DT_unsafe_prob = best_mlp.predict_proba(X)[0][0]
    DT_safe_prob = best_mlp.predict_proba(X)[0][1]

    #Boosting_API
    file1 = open(r'.\BestModel_Boosting.pkl', 'rb')
    best_mlp = pickle.load(file1)
    file1.close()
    Boosting_val = best_mlp.predict(X)[0]
    Boosting_prob = max(best_mlp.predict_proba(X)[0])
    Boosting_unsafe_prob = best_mlp.predict_proba(X)[0][0]
    Boosting_safe_prob = best_mlp.predict_proba(X)[0][1]

    #LDA API
    file1 = open(r'.\BestModel_LDA.pkl', 'rb')
    best_mlp = pickle.load(file1)
    file1.close()
    LDA_val = best_mlp.predict(X)[0]
    LDA_prob = max(best_mlp.predict_proba(X)[0])
    LDA_unsafe_prob = best_mlp.predict_proba(X)[0][0]
    LDA_safe_prob = best_mlp.predict_proba(X)[0][1]

    #safe
    Sum_safe_prob = SVM_safe_prob + DT_safe_prob + Boosting_safe_prob + LDA_safe_prob + NN_safe_prob
    avg_safe_prob = Sum_safe_prob/5
    # unsafe
    Sum_unsafe_prob = SVM_unsafe_prob + DT_unsafe_prob + Boosting_unsafe_prob + LDA_unsafe_prob + NN_unsafe_prob
    avg_unsafe_prob = Sum_unsafe_prob / 5

    if avg_safe_prob > avg_unsafe_prob:
        avg_prob = avg_safe_prob
        final_answer = 1
    else:
        avg_prob = avg_unsafe_prob
        final_answer = -1

    if detailed:
        final_result={"final answer": final_answer, "final_probability" : avg_prob, "NN_ans":NN_val, "NN_probability":NN_prob,
                      "SVM_ans":SVM_val,"SVM_probability":SVM_prob, "DT_ans":DT_val,"DT_probability":DT_prob, "Boosting_ans":Boosting_val,
                      "Boosting_probability":Boosting_prob, "LDA_val":LDA_val, "LDA_probability":LDA_prob}
    else:
        final_result = {"final answer": final_answer, "final_probability" : avg_prob}
    return final_result

if __name__=="__main__":
    getMLScore(features=sys.argv[1],detailed=True)
    #="-1,1,1,1,-1,-1,-1,-1" is an example of sys.argv[1] a parameter.
