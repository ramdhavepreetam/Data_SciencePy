from sklearn import tree

#[height, width, shoe size ]
X = [[181,84,65],[150,75,63],[184,70,60],[156,58,42],[199,75,54],[188,63,41],[174,53,45],[174,54,63],
    [186,80,55],[155,65,43],[134,50,55],[159,59,49],[198,85,74],[138,62,44],[174,52,46],[173,57,61]]
Y = ['male', 'female', 'male','male','female','male', 'female','male' ,'female','male' ,'female','male','female','female','male','male']

clf = tree.ExtraTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[150,85,70]])

print prediction