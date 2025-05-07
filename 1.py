def analyze_scores(scores):
    average=sum(scores)/len(scores)
    above_or_equal = []
    below = []
    for score in scores:
        if score>=average:
            above_or_equal.append(score)

        else:
            below.append(score)

    return{
        "average score": average,
        "above or equal": above_or_equal,
        "below average": below
    }    

scores =[3,7,11,19,15]
result = analyze_scores(scores)   
print(result) 




    


